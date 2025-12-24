FEATURES = [
    {
        "task_name": "image face swapping",
        "input_type": "image",
        "output_modality": "image",
        "required_agents": ["image_processing_agent"],
        "keywords": ["face swap", "swap face", "change face"]
    },
    {
        "task_name": "video face swapping",
        "input_type": "video",
        "output_modality": "video",
        "required_agents": ["video_processing_agent"],
        "keywords": ["face swap video", "swap faces in video"]
    },
    {
        "task_name": "colour image to black and white and vice versa",
        "input_type": "image",
        "output_modality": "image",
        "required_agents": ["image_processing_agent"],
        "keywords": ["black and white", "grayscale", "colorize"]
    },
    {
        "task_name": "voice cloning",
        "input_type": "audio+text",
        "output_modality": "audio",
        "required_agents": ["voice_cloning_agent"],
        "keywords": ["voice clone", "clone voice"]
    },
    {
        "task_name": "rafi voice conversion",
        "input_type": "audio",
        "output_modality": "audio",
        "required_agents": ["voice_conversion_agent"],
        "keywords": ["rafi voice", "convert to rafi"]
    },
    {
        "task_name": "text_to_image",
        "input_type": "text",
        "output_modality": "image",
        "required_agents": ["text_to_image_agent"],
        "keywords": ["generate image", "text to image"]
    },
    {
        "task_name": "text_to_video",
        "input_type": "text",
        "output_modality": "video",
        "required_agents": ["video_gen_agent"],
        "keywords": ["generate video", "text to video"]
    },
    {
        "task_name": "photo_talking_avatar",
        "input_type": "image+audio+text",
        "output_modality": "video",
        "required_agents": ["talking_avatar_agent"],
        "keywords": ["talking photo", "photo talking"]
    },
    {
        "task_name": "action_avatar",
        "input_type": "image+text",
        "output_modality": "video",
        "required_agents": ["action_avatar_agent"],
        "keywords": ["animate avatar", "avatar action"]
    },
    {
        "task_name": "background_changing",
        "input_type": "image+text",
        "output_modality": "image",
        "required_agents": ["background_editor_agent"],
        "keywords": ["change background", "replace background"]
    }
]
