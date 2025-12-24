def route_plan(plan):
    if not plan.is_relevant:
        return "reject"

    if plan.confidence is None or plan.confidence < 0.6:
        return "clarification"

    return plan.task_name
