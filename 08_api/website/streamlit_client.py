import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App | Made By Ahmed Mujtaba")

def create_user():
    with st.form("Create User"):
        st.write("### Register a New User")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
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
                st.success("Logged in successfully")
                return response.json()["access_token"]
            else:
                st.error("Failed to log in")
    return ""

def create_todo(token):
    with st.form("Create Todo"):
        st.write("### Create a New Todo")
        title = st.text_input("Enter Todo Title", key="create_title")
        description = st.text_area("Enter Todo Description", key="create_description")
        submit_button = st.form_submit_button("Add Todo")

        if submit_button and token:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.post(f"{BASE_URL}/todos/", headers=headers, json={"title": title, "description": description})
            if response.status_code == 200:
                st.success("Todo added successfully")
            else:
                st.error("Failed to add todo")

def delete_todo(token):
    with st.form("Delete Todo"):
        st.write("### Delete a Todo")
        todo_id = st.number_input("Enter Todo ID to Delete", step=1, format="%d", key="delete_id")
        delete_button = st.form_submit_button("Delete Todo")

        if delete_button and token:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.delete(f"{BASE_URL}/todos/{int(todo_id)}", headers=headers)
            if response.status_code == 200:
                st.success("Todo deleted successfully")
            else:
                st.error("Failed to delete todo")

if __name__ == "__main__":
    create_user()
    token = login()
    create_todo(token)
