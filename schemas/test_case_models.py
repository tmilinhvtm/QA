"""Data schemas for Automated Test Specification."""
from typing import List, Optional
from pydantic import BaseModel, Field


class SimulatedStep(BaseModel):
    step_number: int = Field(..., description="Thứ tự bước (1, 2, 3...)")
    action_and_input: str = Field(..., description="Hành động giả lập (UI action, API endpoint, hoặc Mock payload)")
    expected_result: str = Field(..., description="Kết quả mong muốn tương ứng (UI assertion, status code, DB update)")


class TestCaseSpecification(BaseModel):
    test_case_id: str = Field(..., description="Mã định danh test case (e.g. TC_001)")
    requirement_id: str = Field(..., description="Mã requirement liên kết (Foreign key)")
    scenario_name: str = Field(..., description="Tên kịch bản kiểm thử")
    test_type: str = Field(..., description="Loại test: Happy Path, Boundary Value, Negative, Concurrency, State Conflict")
    priority: str = Field(..., description="Độ ưu tiên: P1 (Critical), P2 (High), P3 (Medium)")
    priority_reason: str = Field(..., description="Lý do đánh giá mức độ thích hợp và ưu tiên")
    steps: List[SimulatedStep] = Field(..., min_length=1, description="Các bước thực hiện giả lập")
