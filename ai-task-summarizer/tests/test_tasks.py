def test_create_task(client):
    res = client.post("/tasks", json={
        "title": "Test Task",
        "description": "This is a valid task description."
    })
    assert res.status_code == 201
    assert "summary" in res.json()

def test_get_task_not_found(client):
    res = client.get("/tasks/999")
    assert res.status_code == 404
