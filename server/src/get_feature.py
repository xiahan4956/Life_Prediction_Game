import logging
import json
import random

from src.utils import ask_claude
from prompt.feature import generate_feature_pmt, generate_feature_exeample

logger = logging.getLogger(__name__)

def generate_feature(style):
    logger.info("Generating features")
    user_pmt = generate_feature_pmt.format(style=style)
    ai_resp = generate_feature_exeample

    pmt = f"\n\nHuman: {user_pmt} \n\nAssistant: {ai_resp} \n\nHuman:Your format is right! Let's try again! {user_pmt}  \n\nAssistant: This is a json return:\n\n"

    while True:
        try:
            feature = ask_claude(pmt)
            if json.loads(feature):
                logger.info("Feature generated successfully")
                break

        except json.JSONDecodeError as e:
            logger.error("Getting feature causes json error: %s", e)

    return json.loads(feature)



def choose_feature(features:list):
    logger.info("Choosing features from dictionary")
    # 从features中随机选择3个feature
    chosen_features = random.sample(features, 3)
    
    logger.info(f"*****Features chosen successfully {str(chosen_features)}******")

    return chosen_features
