import json
from fastapi.testclient import TestClient
from tensflow import app

client = TestClient(app)

def test_predict_airplane():
    filename = "./tests/fixtures/airplane.jpg"
    response = client.post("/predict", files={"file": ("airplane.jpg", open(filename, "rb"), "image/jpeg")})
    predict_response = json.loads(response.content)
    assert response.status_code == 200
    assert any('airplane' in d for d in predict_response)
    assert any('image_url' in d for d in predict_response)


def test_predict_bicycle():
    filename = "./tests/fixtures/bicycle.jpeg"
    response = client.post("/predict", files={"file": ("bicycle.jpeg", open(filename, "rb"), "image/jpeg")})
    predict_response = json.loads(response.content)
    assert response.status_code == 200
    assert any('bicycle' in d for d in predict_response)
    assert any('image_url' in d for d in predict_response)
    tear_down()

    
def test_predict_bird():
    filename = "./tests/fixtures/bird.jpg"
    response = client.post("/predict", files={"file": ("bird.jpg", open(filename, "rb"), "image/jpeg")})
    predict_response = json.loads(response.content)
    assert response.status_code == 200
    assert any('bird' in d for d in predict_response)
    assert any('image_url' in d for d in predict_response)
    tear_down()

    
# удаление тестовых файлов
def tear_down():
    import os
    files = [f for f in os.listdir('./static') if os.path.isfile(os.path.join('./static', f))]
    for file in files:
        if file == '.keep':
            continue
        os.remove(f'./static/{file}')
