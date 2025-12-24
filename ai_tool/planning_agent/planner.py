from .features import FEATURES


def detect_task(user_input: str):
    text = user_input.lower()
    for feature in FEATURES:
        for kw in feature["keywords"]:
            if kw in text:
                return feature
    return None


def missing_inputs(input_type: str, user_input: str):
    missing = []
    text = user_input.lower()

    if "image" in input_type and "image" not in text:
        missing.append("Please provide the image.")

    if "video" in input_type and "video" not in text:
        missing.append("Please provide the video.")

    if "audio" in input_type and "audio" not in text:
        missing.append("Please provide the audio.")

    if "text" in input_type and len(user_input.strip()) < 5:
        missing.append("Please provide the text content.")

    return missing


def planning_agent(user_input: str):
    feature = detect_task(user_input)

    if not feature:
        return {
            "case": "insufficient",
            "questions": [
                "I could not clearly understand your request. Can you please rephrase?"
            ]
        }

    missing = missing_inputs(feature["input_type"], user_input)

    if missing:
        return {
            "case": "insufficient",
            "questions": missing
        }

    return {
        "case": "sufficient",
        "task_name": feature["task_name"],
        "input_type": feature["input_type"],
        "output_modality": feature["output_modality"],
        "extracted_constraints": {},
        "required_agents": feature["required_agents"]
    }
