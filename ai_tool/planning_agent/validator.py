def validate_plan(output: str) -> PlanningOutput:
    data = json.loads(output)
    return PlanningOutput(**data)
