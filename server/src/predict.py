# prediction.py
import logging
from src.utils import get_msg

logger = logging.getLogger(__name__)

def life_predict(sytle:str,
                 attribute:dict,
                 player_feature:list,
                 dead_age:int,
                 start_age = 0,
                 prediction_history = "" ,
                 ) -> str: 
    # 添加logging记录
    logging.info('Starting life prediction')

    from prompt.prediction import predict_pmt    
    # 预测到玩家去世的年龄,每5年预测一次
    
    if not isinstance(start_age, int):
        start_age = 0
    
    end_age = start_age + 5
    logging.info(f"===== -----current age:{start_age}-{end_age}---- =========")
    
    # 生成预测的prompt        
    pmt = predict_pmt.format(
                        atrributes=str(attribute),
                        features=str(player_feature),
                        history=prediction_history,
                        start_age=start_age,
                        end_age=end_age,
                        style=sytle,
                        dead_age = dead_age)

    pmt = f"\n\nHuman:{pmt} \n\nAssistant:Here is the simulated result of the player\'s life:<json>"

    # 生成预测
    current_prediction = get_msg(pmt)
    
    # 整理数据
    prediction_history = prediction_history + current_prediction + "\n"

    # 添加logging记录
    logging.info('Finished life prediction')
       
    # 返回下次预测的起始年龄
    next_start_age = end_age + 1
    if next_start_age > dead_age:
        next_start_age = None
    
    
    return current_prediction,prediction_history,next_start_age
