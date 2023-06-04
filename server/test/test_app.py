#打印当前目录
import os
print(os.getcwd())

import pytest
from app import app
from flask import session

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_potential_game_style(client):
    rv = client.get('/api/potential_game_style')
    assert rv.status_code == 200
    assert isinstance(rv.json['potential_game_style'], list)


def test_selected_game_style(client):
    rv = client.post('/api/selected_game_style', json={'selected_game_style': 'Cyber punk'})
    assert rv.status_code == 200
    assert 'potential_features' in rv.json

def test_distributed_attribute(client):
    data = {
            "health": 10,
            "family": 8,
            "intelligence": 7,
            "beauty": 6
        }
    rv = client.post('/api/distributed_attribute', json=data)
    assert rv.status_code == 200
    assert rv.json['msg'] == 'attribute received'


def test_selected_features(client):
    rv = client.post('/api/selected_features', json={"selected_features": ["冷血杀手:战斗力强,但是人际关系薄弱","黑客专家:电脑高手,但是身体虚弱"]})
    assert rv.status_code == 200
    assert rv.json['msg'] == 'features received'

def test_get_predict(client):
    with client.session_transaction() as session:
        session['game_style'] = 'Cyber punk'
        session['attributes'] = {
            "health": 10,
            "family": 8,
            "intelligence": 7,
            "beauty": 6
        }
        session['dead_age'] = 33
        session['features'] = ["冷血杀手:战斗力强,但是人际关系薄弱","黑客专家:电脑高手,但是身体虚弱"]
    
    rv = client.post('/api/predict', json={"prediction_history": ""})
    assert rv.status_code == 200
    assert 'prediction' in rv.json
    assert 'prediction_history' in rv.json
    assert 'continue_request' in rv.json



def test_restart(client):
    rv = client.get('/api/restart')
    assert rv.status_code == 200
    assert rv.json['redirect'] == '/game_start'

