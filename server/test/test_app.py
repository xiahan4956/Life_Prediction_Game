import pytest
from flask import json
from app import app  # 你的Flask应用的名字

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_get_potential_game_style(client):
    response = client.get('/api/potential_game_style')
    assert response.status_code == 200
    assert isinstance(json.loads(response.data)['potential_game_style'], list)

def test_post_selected_game_style(client):
    data = {"selected_game_style": "style1"}
    response = client.post('/api/selected_game_style', json=data)
    assert response.status_code == 200
    assert isinstance(json.loads(response.data)['potential_features'], list)

def test_post_distributed_attribute(client):
    data = {"health": 1, "family": 2, "intelligence": 3, "beauty": 4}
    response = client.post('/api/distributed_attribute', json=data)
    assert response.status_code == 200
    assert 'dead_age' in json.loads(response.data)

def test_post_predict(client):
    data = {
        "game_style": "style1",
        "attributes": {"health": 1, "family": 2, "intelligence": 3, "beauty": 4},
        "features": {"feature1": 1, "feature2": 2},
        "dead_age": 75,
        "start_age": 20,
        "prediction_history": "prediction1"
    }
    response = client.post('/api/predict', json=data)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert 'prediction' in response_data
    assert 'continue_request' in response_data
    assert 'next_start_age' in response_data
    assert 'prediction_history' in response_data

def test_get_restart(client):
    response = client.get('/api/restart')
    assert response.status_code == 200
    assert json.loads(response.data)['redirect'] == "/game_start"
