import axios, { AxiosResponse } from "axios";

const BASE_URL: string = "http://127.0.0.1:8000";

async function createUser(username: string, password: string): Promise<void> {
  try {
    const response: AxiosResponse = await axios.post(`${BASE_URL}/users/`, {
      username,
      password,
    });
    console.log("User created successfully");
  } catch (error: any) {
    console.error("Error creating user:", error.message);
  }
}

async function login(username: string, password: string): Promise<string> {
  try {
    const response: AxiosResponse = await axios.post(
      `${BASE_URL}/token`,
      `username=${username}&password=${password}`,
      {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      }
    );
    console.log("Logged in successfully");
    return response.data.access_token;
  } catch (error: any) {
    console.error("Error logging in:", error.message);
    return "";
  }
}

async function createTodo(
  token: string,
  title: string,
  description: string
): Promise<void> {
  try {
    const response: AxiosResponse = await axios.post(
      `${BASE_URL}/todos/`,
      { title, description },
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );
    console.log("Todo added successfully");
  } catch (error: any) {
    console.error("Error adding todo:", error.message);
  }
}

async function getTodos(token: string): Promise<void> {
  try {
    const response: AxiosResponse = await axios.get(`${BASE_URL}/todos/`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    console.log("Todos:", response.data);
  } catch (error: any) {
    console.error("Error fetching todos:", error.message);
  }
}

async function updateTodo(
  token: string,
  todoId: number,
  title: string,
  description: string
): Promise<void> {
  try {
    const response: AxiosResponse = await axios.put(
      `${BASE_URL}/todos/${todoId}`,
      { title, description },
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );
    console.log("Todo updated successfully");
  } catch (error: any) {
    console.error("Error updating todo:", error.message);
  }
}

async function deleteTodo(token: string, todoId: number): Promise<void> {
  try {
    const response: AxiosResponse = await axios.delete(
      `${BASE_URL}/todos/${todoId}`,
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );
    console.log("Todo deleted successfully");
  } catch (error: any) {
    console.error("Error deleting todo:", error.message);
  }
}

async function main(): Promise<void> {
  try {
    await createUser("testUser", "testPass");
    const token: string = await login("testUser", "testPass");
    if (token) {
      await createTodo(token, "Sample Title", "Sample Description");
      await getTodos(token);
      await updateTodo(token, 1, "Updated Title", "Updated Description");
      await deleteTodo(token, 1);
    }
  } catch (error: any) {
    console.error("Error in main:", error.message);
  }
}

main();
