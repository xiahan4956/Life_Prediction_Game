from flask import Flask, request, jsonify, session
from src.get_style import generate_style
from src.get_attribute import generate_attribute
from src.get_feature import generate_feature, choose_feature
from src.get_dead_age import generate_dead_age
from src.predict import life_predict
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'a3cJNmd0cf50nfdPc40sfnA0nfd9vnA3Bn0anfd'


@app.route('/api/potential_game_style', methods=['GET'])
def get_potential_game_style():
    '''
    Endpoint: /api/potential_game_style
    Method: GET
    Description: 返回可供选择的游戏风格
    No input required.
    Returns: 
        JSON
        {
            "potential_game_style": ["style1", "style2", ...]
        }
    '''
    
    styles = generate_style()
    return jsonify({"potential_game_style": styles})


@app.route('/api/selected_game_style', methods=['POST'])
def post_selected_game_style():
    '''
    Endpoint: /api/selected_game_style
    Method: POST
    Description: 接受游戏风格,返回角色的特征
    Input:  {"selected_game_style": "<selected_game_style>"}
    Returns: 
        {
            "potential_features": ["feature1", "feature2", ...]
        }
    '''
    
    try:
        selected_game_style = request.json["selected_game_style"]     
        session["game_style"] = selected_game_style
        
        # 生成potential_feature
        potential_features = generate_feature(selected_game_style)
        
        #将potential_feature返回
        return jsonify({"potential_features": potential_features})
        
    except KeyError:
        return jsonify({"error":"please check `selected_game_style`"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/distributed_attribute', methods=['POST'])
def post_distributed_attribute():
    '''
    Endpoint: /api/distributed_attribute
    Method: POST
    Description: 接受属性,计算玩家的死亡时间
    Input: 
        {
          health: <value>,
          family: <value>,
          intelligence: <value>,
          beauty: <value>,
        }
    Returns:
            {"msg": "attribute received"}
    '''
    attributes = request.json
    session["attributes"] = attributes
    
    # 生成死亡年龄
    session["dead_age"] = generate_dead_age(attributes)
    
    return jsonify({"msg": "attribute received"})


@app.route('/api/selected_features', methods=['POST'])
def post_selected_features():
    '''
    Endpoint: /api/selected_features
    Method: POST
    Description: 接受玩家选择的角色特性,用于最终预测
    Input: {"selected_features": "<selected_features>"}
    Returns: {"status": "success"}
    '''
    selected_features = request.json["selected_features"]
    session["features"] = selected_features
    
    return jsonify({"msg": "features received"})

@app.route('/api/predict', methods=['POST'])
def post_predict():
    '''
    Endpoint: /api/predict
    Method: POST
    Description: 返回一次预测结果
    Input:  
        prediction_history :<prediction_history:str>
    Returns:
                {"prediction": current_prediction,
                 "continue_request": continue_request
                }
    '''
    data = request.json
    prediction_history = data.get('prediction_history', '')

    # 生成预测结果
    current_prediction, prediction_history, next_start_age = life_predict(
                                                            sytle = session['game_style'], 
                                                            attribute=session['attributes'], 
                                                            player_feature= session['features'],
                                                            dead_age = session['dead_age'],
                                                            start_age = session.get('start_age', 0),
                                                            prediction_history = prediction_history
                                                        )
    #增加下次开始的年龄
    session["start_age"] = next_start_age
    
    # 给一个继续请求的标注
    continue_request = bool(next_start_age)
    session["continue_request"] = continue_request
    

    return jsonify({"prediction": current_prediction,
                    "continue_request": continue_request,
                    "next_start_age": next_start_age,
                    "prediction_history": prediction_history
                    })
    

@app.route('/api/restart', methods=['GET'])
def get_restart():
    '''
    Endpoint: /api/restart
    Method: GET
    Description: 进行Restart操作,清空session
    No input required.
    Returns: JSON object containing redirect url.
    '''
    session.clear()
    return jsonify({"redirect": "/game_start"})

if __name__ == '__main__':
    app.run(host='192.168.0.100', port=5000, debug=True)
