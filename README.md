# Chat Web Application

Chat is a real-time web chat application built with Flask and Socket.IO. It provides a seamless and interactive platform for users to communicate with each other through individual chat rooms.

## Project Structure

```
Chat_Web_App/
    myapp/
        static/
            images/
            auth.css
            chat.css
            index.js
            styles.css
        templates/
            auth.html
            base.html
            chat.html
            visualize.html
        __init__.py
        config.py
        database.py
        views.py
    .gitignore
    gunicorn_config.py
    README.md
    requirements.txt
    server.py
```

## Getting Started

To run the Chat web application locally, follow these steps:

1. Clone the repository:https://github.com/aarshad11199/chat

   ```bash
   git clone 
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:

   - Create a `.env` file in the project root.
   - Add the following lines to the `.env` file:

     ```env
     SECRET_KEY=your_secret_key_here
     DATABASE_URL=sqlite:///database.db
     ```
4.Create database of name:chat

5. Run the server:

   ```bash
   python server.py
   ```


Visit `http://localhost:5000` in your web browser to access Chat.

## Features

- **User Authentication:** Secure user registration and login with password hashing.
- **Real-time Chat:** Instant messaging in individual chat rooms.
- **Dynamic Chat List:** Automatically updates the chat list with new messages.
- **Responsive Design:** Works seamlessly on desktop and mobile devices.
- **Visualize User Registration Trends** Visualize the user registration data using Pandas and Matplotlib. This feature aims to analyze the number of users registered on the app over time and present the findings in a graphical format.

## Project Architecture

### `__init__.py`

Initialization of the Flask application, configuration, and extension setup.

### `config.py`

Configuration settings for the Flask application, including the secret key and database URI.

### `database.py`

Database models and schema definition using SQLAlchemy. Includes user, chat, and message models.

### `views.py`

Blueprint for route views, including login, registration, chat, and visualization routes.

### `gunicorn_config.py`

Gunicorn's configuration file for deployment settings.

### `server.py`

Entry point for running the server. Initializes the Flask application and Socket.IO communication events.


## DOCKER Instructions
##Build and Start the Containers: Run the following to build and start the containers:

bash
Copy code
docker-compose up --build
Access the Application:

Open a browser and go to http://localhost:5000 to access the chat app.