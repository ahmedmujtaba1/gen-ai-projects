import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App | Made By Ahmed Mujtaba")

if 'token' not in st.session_state:
    st.session_state['token'] = ""

def create_user():
    with st.form("Create User"):
        st.write("### Register a New User")
        username = st.text_input("Username", key="register_username")
        password = st.text_input("Password", type="password", key="register_password")
        submit_button = st.form_submit_button("Register")

        if submit_button:
            response = requests.post(f"{BASE_URL}/users/", json={"username": username, "password": password})
            if response.status_code == 200:
                st.success("User created successfully")
            else:
                st.error("Failed to create user")

def login():
    with st.form("Login"):
        st.write("### Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        login_button = st.form_submit_button("Login")

        if login_button:
            response = requests.post(f"{BASE_URL}/token", data={"username": username, "password": password})
            if response.status_code == 200:
                st.session_state['token'] = response.json()["access_token"]
                st.success("Logged in successfully")
            else:
                st.error("Failed to log in")

def logout():
    if st.button("Logout"):
        st.session_state['token'] = ""
        st.experimental_rerun()

def create_todo():
    with st.form("Create Todo"):
        st.write("### Create a New Todo")
        title = st.text_input("Enter Todo Title", key="create_title")
        description = st.text_area("Enter Todo Description", key="create_description")
        submit_button = st.form_submit_button("Add Todo")

        if submit_button and st.session_state['token']:
            headers = {"Authorization": f"Bearer {st.session_state['token']}"}
            response = requests.post(f"{BASE_URL}/todos/", headers=headers, json={"title": title, "description": description})
            if response.status_code == 200:
                st.success("Todo added successfully")
            else:
                st.error("Failed to add todo")

def get_todos():
    todos = ''
    if st.button("Refresh Todos"):
        if st.session_state['token']:
            headers = {"Authorization": f"Bearer {st.session_state['token']}"}
            response = requests.get(f"{BASE_URL}/todos/", headers=headers)
            if response.status_code == 200:
                todos = response.json()
                if todos:
                    for todo in todos:
                        df = pd.DataFrame(todos)
                        st.table(df)
                else:
                    st.write("No todos found.")
            else:
                st.error("Failed to fetch todos")

def update_todo():
    with st.form("Update Todo"):
        st.write("### Update an Existing Todo")
        todo_id = st.number_input("Enter Todo ID to Update", step=1, format="%d", key="update_id")
        new_title = st.text_input("New Title", key="update_title")
        new_description = st.text_area("New Description", key="update_description")
        update_button = st.form_submit_button("Update Todo")

        if update_button and st.session_state['token']:
            headers = {"Authorization": f"Bearer {st.session_state['token']}"}
            response = requests.put(f"{BASE_URL}/todos/{int(todo_id)}", headers=headers, json={"title": new_title, "description": new_description})
            if response.status_code == 200:
                st.success("Todo updated successfully")
            else:
                st.error("Failed to update todo")
def delete_todo():
    with st.form("Delete Todo"):
        st.write("### Delete a Todo")
        todo_id = st.number_input("Enter Todo ID to Delete", step=1, format="%d", key="delete_id")
        delete_button = st.form_submit_button("Delete Todo")

        if delete_button and st.session_state['token']:
            headers = {"Authorization": f"Bearer {st.session_state['token']}"}
            response = requests.delete(f"{BASE_URL}/todos/{int(todo_id)}", headers=headers)
            if response.status_code == 200:
                st.success("Todo deleted successfully")
            else:
                st.error("Failed to delete todo")
if not st.session_state['token']:
    create_user()
    login()
else:
    logout()
    create_todo()
    update_todo()
    get_todos()
    delete_todo()