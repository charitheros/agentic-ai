from ai_tool.planning_agent.planner import planning_agent

while True:
    user_input = input("\nUSER > ")
    if user_input.lower() == "exit":
        break

    result = planning_agent(user_input)
    print("\nPLANNER OUTPUT:\n", result)
