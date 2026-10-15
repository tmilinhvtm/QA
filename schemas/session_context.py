"""Session Context and State Machine representation."""
from enum import Enum
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

from schemas.analysis_models import AnalysisResult
from schemas.test_case_models import TestCaseSpecification


class SessionState(str, Enum):
    IDLE = "IDLE"
    PHASE_1_ANALYSIS = "PHASE_1_ANALYSIS"
    WAITING_TESTER_PHASE_1 = "WAITING_TESTER_PHASE_1"
    PHASE_2_TEST_GEN = "PHASE_2_TEST_GEN"
    WAITING_TESTER_PHASE_2 = "WAITING_TESTER_PHASE_2"
    SYNCED = "SYNCED"


class SessionContext(BaseModel):
    session_id: str
    requirement_id: Optional[str] = None
    current_state: SessionState = SessionState.IDLE
    created_at: datetime = Field(default_factory=datetime.utcnow)
    raw_requirement: Optional[str] = None
    analysis: Optional[AnalysisResult] = None
    test_cases: List[TestCaseSpecification] = Field(default_factory=list)
    chat_history: List[dict] = Field(default_factory=list)
