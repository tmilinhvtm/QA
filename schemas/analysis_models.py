"""Data schemas for Requirement & Risk Analysis."""
from typing import List, Optional
from pydantic import BaseModel, Field


class BugCorrelation(BaseModel):
    bug_id: str = Field(..., description="ID của bug trong kho lịch sử (e.g. BUG-001)")
    description: str = Field(..., description="Mô tả tóm tắt của bug")
    reason: str = Field(..., description="Lý do chi tiết vì sao bug này liên quan đến requirement")


class AnalysisResult(BaseModel):
    requirement_id: Optional[str] = Field(None, description="Mã định danh requirement (e.g. REQ_001)")
    requirement_text: str = Field(..., description="Văn bản requirement gốc từ BA")
    business_rules: List[str] = Field(..., min_length=1, description="Danh sách các quy tắc nghiệp vụ bóc tách được")
    questions_for_ba: List[str] = Field(..., min_length=1, description="Danh sách các câu hỏi chất vấn BA / PO")
    possible_risks: List[str] = Field(..., min_length=1, description="Các rủi ro kỹ thuật tiềm ẩn")
    related_bugs: List[BugCorrelation] = Field(default_factory=list, description="Danh sách bug lịch sử liên quan kèm lý do")
    key_decisions_log: List[str] = Field(default_factory=list, description="Các quyết định và ghi chú trao đổi với Tester")
