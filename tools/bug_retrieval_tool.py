"""Bug retrieval tool for correlating historical bugs with requirements."""
import json
import os
from typing import List, Dict, Any

from config.settings import SPREADSHEET_ID, GOOGLE_ACCOUNT_EMAIL, TAB_BUG_REPO
from schemas.analysis_models import BugCorrelation


class BugRetrievalTool:
    """Satellite Tool for querying and matching bugs from historical repository."""

    def __init__(self, fallback_path: str = "/home/linh/qa-requirement-assistant/config/bug_catalog.json"):
        self.fallback_path = fallback_path
        self._cached_bugs: List[Dict[str, Any]] = []
        self.load_bugs()

    def load_bugs(self) -> List[Dict[str, Any]]:
        """Loads historical bugs from local fallback catalog or cached source."""
        if os.path.exists(self.fallback_path):
            with open(self.fallback_path, "r", encoding="utf-8") as f:
                self._cached_bugs = json.load(f)
        return self._cached_bugs

    def find_related_bugs(self, requirement_text: str) -> List[BugCorrelation]:
        """Identifies correlations between requirement text and known bugs based on domain rules."""
        req_lower = requirement_text.lower()
        results: List[BugCorrelation] = []

        # Knowledge base mapping domain triggers to bugs
        # BUG-001: Cancel / Concurrency / Refund
        if any(w in req_lower for w in ["hủy", "cancel", "refund", "hoàn tiền", "đồng thời", "tiền"]):
            results.append(BugCorrelation(
                bug_id="BUG-001",
                description="Hai request cancel được gửi gần như đồng thời và hệ thống tạo hai refund.",
                reason="Requirement có chức năng hủy đơn hàng sau thanh toán. Nguy cơ race condition khi người dùng nhấn hủy nhiều lần hoặc gửi request đồng thời dẫn đến hoàn tiền 2 lần."
            ))

        # BUG-002: Warehouse / Processing state / Cancel
        if any(w in req_lower for w in ["hủy", "cancel", "processing", "kho", "warehouse", "trạng thái"]):
            results.append(BugCorrelation(
                bug_id="BUG-002",
                description="Người dùng vẫn cancel được order sau khi warehouse đã bắt đầu xử lý.",
                reason="Requirement chặn hủy khi đơn chuyển sang PROCESSING. Cần kiểm tra độ trễ trạng thái (State drift) giữa hệ thống đơn hàng và kho vận."
            ))

        # BUG-003: Voucher / Khuyến mãi / Tài khoản
        if any(w in req_lower for w in ["voucher", "khuyến mãi", "coupon", "tài khoản", "giảm giá"]):
            results.append(BugCorrelation(
                bug_id="BUG-003",
                description="Một user sử dụng cùng voucher cho hai đơn hàng.",
                reason="Requirement liên quan đến kiểm soát sử dụng voucher / tài nguyên dùng một lần. Nguy cơ thiếu Distributed Lock khi áp dụng voucher trên nhiều phiên đồng thời."
            ))

        # BUG-004: Payment / Callback / Webhook
        if any(w in req_lower for w in ["thanh toán", "payment", "callback", "webhook", "thẻ", "credit"]):
            results.append(BugCorrelation(
                bug_id="BUG-004",
                description="Payment callback được gửi hai lần và tạo ra hai order.",
                reason="Requirement tương tác với luồng thanh toán hoặc hoàn tiền qua cổng giao dịch. Cần bảo đảm tính Idempotency khi nhận callback."
            ))

        # BUG-005: Tồn kho / Inventory / Số lượng đặt
        if any(w in req_lower for w in ["tồn kho", "kho", "inventory", "số lượng", "đặt mua", "stock"]):
            results.append(BugCorrelation(
                bug_id="BUG-005",
                description="Order được tạo thành công nhưng tồn kho không bị trừ.",
                reason="Requirement liên quan đến kiểm tra hoặc cập nhật tồn kho khi đặt/hủy hàng. Nguy cơ giao dịch phân tán không đồng nhất (Distributed Transaction failure)."
            ))

        return results
