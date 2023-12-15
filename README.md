# War of Elements Project Documentation

## Introduction

The **War of Elements** project is the culmination of the "Computer Analyst" course, serving as the final assignment for the Computer Analyst degree at the National University of Río Cuarto. This documentation provides a comprehensive overview of the project, detailing its purpose, functionality, and implementation.

## Step by step to run the application

Here is a step-by-step guide on how to set up the project:

1. **Create a virtual environment**: This helps to keep the dependencies required by different projects separate by creating isolated Python virtual environments for them. This is done using the command:
    ```bash
    python3 -m venv venv
    ```

2. **Install the required packages**: The `requirements.txt` file contains a list of items to be installed using pip install like so:
    ```bash
    pip3 install -r requirements.txt
    ```

3. **Run the API**: This starts the backend server. Open a console and run the following command:
    ```bash
    python3 run.py
    ```

4. **Move to the client directory and install npm packages**: This installs the necessary npm packages for the frontend in the client directory:
    ```bash
    cd client
    npm install
    ```

5. **Start the client**: This starts the frontend application:
    ```bash
    npm start
    ```

6. **Create a .env file**: This file will store environment variables. These are often used to store sensitive information such as API keys, and in this case, they are used to store the `SECRET_KEY`, `FLASK_APP`, and `GOOGLE_CLIENT_ID`. You can create a `.env` file in the root directory and add the following lines to it:
    ```bash
    SECRET_KEY=<your-secret-key>
    FLASK_APP='run.py'
    GOOGLE_CLIENT_ID=<your-google-client-id>
    ```
Please replace 'your-secret-key' and 'your-google-client-id' with your actual keys. For the `GOOGLE_CLIENT_ID`, you need to create a project and link it to localhost:3000. [You can follow the guide here.](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid)
To generate a secure secret key, you can use a password generator like [RandomKeyGen](https://randomkeygen.com/).

## Project Overview

### Objective

The primary goal of the War of Elements project is to demonstrate the skills and knowledge acquired throughout the university degree. It serves as a comprehensive showcase of the participants’ ability to design and develop a software application using an agile methodology.

### Scope

The project is a simulation where it’s possible to choose a team, set the spawn (dispersion area of cells), and the size of the board. The simulation begins and ends with a winning team after a series of battles and fusions between cells.

### Technologies Used

The project leverages a variety of technologies:

- **Frontend:** The user interface is built using Javascript and React is employed for dynamic and responsive UI components.

- **Backend:** The backend is powered by a API developed with Flask. The logic layer is implemented in Python. 

- **Database:** SQLite is used as the database, and ORM used is SQLAlchemy, utilized for managing the database. 

- **Authentication:** Google OAuth is used for user authentication.

- **Testing:** Pytest is used for unit testing and behave is used for integration testing of the logic layer.

- **Serialization:** Marshmallow is used for efficiently storing simulations in the database.

## Conclusion

The War of Elements project showcases the culmination of theoretical knowledge and practical skills acquired during the "Proyecto" course. It stands as a testament to the participant's ability to design and implement a complex software application. This documentation serves as a guide to understanding the project's objectives, functionalities, and the technologies employed in its development.

[Canva presentation to have a preview of the features](https://www.canva.com/design/DAF1rrNywsw/5jYv1NlfB84hT9RjLG8Mtg/edit)