# Pedigree Agent with FastAPI Backend

This project is a conversational AI agent designed to collect pedigree (family history) information. It is powered by the Google Agent Development Kit (ADK) and served via a FastAPI backend, with a simple web interface for real-time chat.

## How to Run the Application

You will need two separate terminals to run the backend and frontend servers.

### 1. Run the Backend API

In your project's root folder, run the following command:
```bash
python api.py
```
The API will be running on `http://127.0.0.1:8000`.

### 2. Run the Frontend

In a new terminal, navigate to the `frontend` directory and run the following command:
```bash
cd frontend
python -m http.server 3000
```
The frontend will be available at `http://localhost:3000`.

### 3. Start Chatting

- Open your web browser and go to `http://localhost:3000`.
- You can now start a conversation with the pedigree agent.

## Next Steps

Here are some potential next steps to improve the application:

1.  **Implement a Login Screen:**
    - Before the chat interface appears, present the user with a simple login screen.
    - The screen should only require a username to proceed.

2.  **Make the Username Dynamic:**
    - In `main.py`, the `USER_ID` is currently hardcoded as `"user_001"`.
    - Modify the API and the `main_async` function to accept the username from the frontend.
    - This will allow the backend to manage separate conversation histories for different users.

3.  **Store and Display Previous Sessions:**
    - Since conversation history is already being stored in the `sessions.db` file, you can enhance the frontend to display a list of previous conversations for a logged-in user.
    - The user could then click on a past session to view its history or continue the conversation.
