from pydantic import BaseModel
from typing import List, Optional

class PlanningOutput(BaseModel):
    is_relevant: bool
    task_name: Optional[str]
    input_type: Optional[str]
    required_agents: Optional[List[str]]
    missing_inputs: Optional[List[str]]
    confidence: Optional[float]
    reason: Optional[str]
