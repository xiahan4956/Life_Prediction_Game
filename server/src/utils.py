# utils.py
import os
import anthropic
import logging
import time
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)


def get_msg(pmt,model = "claude-instant-v1") -> str:
    logger.info("Getting message from anthropic")
    client = anthropic.Client(os.environ['ANTHROPIC_API_KEY'])
    
    while True:
        try:
            response = client.completion(
                prompt=pmt,
                stop_sequences = [anthropic.HUMAN_PROMPT],
                model=model,
                max_tokens_to_sample=1000000,
                temperature=1
            )
            logger.info(f"anthropic response received:{response['completion']}")
            break
        except Exception as e:
            logger.error("anthropic error: %s", e)
            time.sleep(3)
            
    return response["completion"]
