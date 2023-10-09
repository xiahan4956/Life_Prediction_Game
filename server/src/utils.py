# utils.py
import os
import logging
import time
from dotenv import load_dotenv
load_dotenv()
ANTHROPIC_API_KEY  = os.getenv("ANTHROPIC_API_KEY")
logger = logging.getLogger(__name__)

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

def ask_claude(content):
    client = Anthropic(api_key = ANTHROPIC_API_KEY)    
    prompt=content
    
    while True:
        try:
            response = client.completions.create(
                prompt=prompt,
                model="claude-2",
                temperature = 0,
                max_tokens_to_sample = 1000
            )
            break
        except Exception as e:
            time.sleep(3)
            print(e)
            
    print(response.completion)

    return response.completion
