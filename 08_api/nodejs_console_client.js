"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const axios_1 = __importDefault(require("axios"));
const BASE_URL = "http://127.0.0.1:8000";
function createUser(username, password) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield axios_1.default.post(`${BASE_URL}/users/`, {
                username,
                password,
            });
            console.log("User created successfully");
        }
        catch (error) {
            console.error("Error creating user:", error.message);
        }
    });
}
function login(username, password) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield axios_1.default.post(`${BASE_URL}/token`, `username=${username}&password=${password}`, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            });
            console.log("Logged in successfully");
            return response.data.access_token;
        }
        catch (error) {
            console.error("Error logging in:", error.message);
            return "";
        }
    });
}
function createTodo(token, title, description) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield axios_1.default.post(`${BASE_URL}/todos/`, { title, description }, {
                headers: { Authorization: `Bearer ${token}` },
            });
            console.log("Todo added successfully");
        }
        catch (error) {
            console.error("Error adding todo:", error.message);
        }
    });
}
function getTodos(token) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield axios_1.default.get(`${BASE_URL}/todos/`, {
                headers: { Authorization: `Bearer ${token}` },
            });
            console.log("Todos:", response.data);
        }
        catch (error) {
            console.error("Error fetching todos:", error.message);
        }
    });
}
function updateTodo(token, todoId, title, description) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield axios_1.default.put(`${BASE_URL}/todos/${todoId}`, { title, description }, {
                headers: { Authorization: `Bearer ${token}` },
            });
            console.log("Todo updated successfully");
        }
        catch (error) {
            console.error("Error updating todo:", error.message);
        }
    });
}
function deleteTodo(token, todoId) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield axios_1.default.delete(`${BASE_URL}/todos/${todoId}`, {
                headers: { Authorization: `Bearer ${token}` },
            });
            console.log("Todo deleted successfully");
        }
        catch (error) {
            console.error("Error deleting todo:", error.message);
        }
    });
}
function main() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            yield createUser("testUser", "testPass");
            const token = yield login("testUser", "testPass");
            if (token) {
                yield createTodo(token, "Sample Title", "Sample Description");
                yield getTodos(token);
                yield updateTodo(token, 1, "Updated Title", "Updated Description");
                yield deleteTodo(token, 1);
            }
        }
        catch (error) {
            console.error("Error in main:", error.message);
        }
    });
}
main();
