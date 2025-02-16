import os
from openai import OpenAI
from custom_logger import logger
from config import get_config
from dotenv import load_dotenv
from src.session_utils import sessionUtilities
from src.multi_shot_examples import get_exmaples
import os
import random

load_dotenv()

class Utilities:
    def __init__(self):
        logger.debug("initializing utilities")
        self.config = get_config()
        self.session_utils = sessionUtilities()

        self.client = OpenAI()

    
    def get_session_icon(self, session_id):
        icon_name = self.session_utils.get_session_icon(session_id)
        if icon_name is None:
            icons_dir_path = "static/images/session-icons"
            random_icon = random.choice([x for x in os.listdir(icons_dir_path) if x.endswith(".svg")])
            return random_icon
        return icon_name
    
    def get_previous_messages(self, session_id, instructions, component):
        session_data = self.session_utils.get_session_data(session_id)
        messages = [{
                    "role": "system",
                    "content": instructions
                }]
        messages += get_exmaples(instructions)
        for request in session_data:
            for key,val in request.items():
                messages.append(
                    {
                        "role": "user",
                        "content": key
                    }
                )
                messages.append(
                    {
                        "role": "assistant",
                        "content": val[component]
                    }
                )
        return messages

    def invoke_llm(self, messages):
        llm_params = self.config.LLM_PARAMS
        llm_params['messages'] = messages
        llm_params['stream'] = False

        chat_completion = self.client.chat.completions.create(
            **llm_params
        )
        
        return chat_completion.choices[0].message.content