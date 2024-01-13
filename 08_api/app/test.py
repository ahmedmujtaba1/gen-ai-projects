import requests

BASE_URL = "http://127.0.0.1:8000" 

def test_create_user():
    url = f"{BASE_URL}/users/"
    data = {"username": "testuser", "password": "testpassword"}
    response = requests.post(url, json=data)
    assert response.status_code == 200, "Failed to create user"
    assert response.json()["username"] == data["username"], "Username mismatch"
    print("[Test] Create User: Passed")

def test_token_generation():
    url = f"{BASE_URL}/token"
    data = {"username": "testuser", "password": "testpassword"}
    response = requests.post(url, data=data)
    assert response.status_code == 200, "Failed to generate token"
    token = response.json()["access_token"]
    assert token is not None, "Token is None"
    print("[Test] Token Generation: Passed")
    return token

def test_create_todo(token):
    url = f"{BASE_URL}/todos/"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": "Test Todo", "description": "Test todo description"}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200, "Failed to create todo"
    assert response.json()["title"] == data["title"], "Todo title mismatch"
    print("[Test] Create Todo: Passed")
    return response.json()["id"]

def test_get_todos(token):
    url = f"{BASE_URL}/todos/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, "Failed to get todos"
    assert isinstance(response.json(), list), "Response is not a list"
    print("[Test] Get Todos: Passed")

def test_update_todo(token, todo_id):
    url = f"{BASE_URL}/todos/{todo_id}"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": "Updated Test Todo", "description": "Updated test description"}
    response = requests.put(url, headers=headers, json=data)
    assert response.status_code == 200, "Failed to update todo"
    assert response.json()["title"] == data["title"], "Updated todo title mismatch"
    print("[Test] Update Todo: Passed")

def test_delete_todo(token, todo_id):
    url = f"{BASE_URL}/todos/{todo_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, "Failed to delete todo"
    print("[Test] Delete Todo: Passed")

# Run the tests
if __name__ == "__main__":
    try:
        # test_create_user()
        token = test_token_generation()
        todo_id = test_create_todo(token)
        test_get_todos(token)
        test_update_todo(token, todo_id)
        # test_delete_todo(token, todo_id)
        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
