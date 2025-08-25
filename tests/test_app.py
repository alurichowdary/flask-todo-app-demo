import pytest
from app import app, db, Task

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client

def test_add_task(client):
    rv = client.post("/", data={"task": "Write tests"}, follow_redirects=True)
    assert rv.status_code == 200
    assert b"Write tests" in rv.data

def test_complete_task(client):
    # add task first
    client.post("/", data={"task": "Finish homework"}, follow_redirects=True)
    task = Task.query.first()
    client.get(f"/complete/{task.id}", follow_redirects=True)
    assert Task.query.first().completed is True

def test_delete_task(client):
    client.post("/", data={"task": "Clean room"}, follow_redirects=True)
    task = Task.query.first()
    client.get(f"/delete/{task.id}", follow_redirects=True)
    assert Task.query.first() is None
