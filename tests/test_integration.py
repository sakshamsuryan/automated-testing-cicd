from app import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Application is running"


def test_add_endpoint():
    client = app.test_client()
    response = client.get("/add?a=5&b=3")

    assert response.status_code == 200
    assert response.json["result"] == 8
