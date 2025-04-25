# Flask Mini Project Management App

This is a Flask-based web application, one of my first Flask toss arounds, this is for managing projects and their associated tasks. It allows users to create, view, and manage projects and tasks with ease.

## Features
- Create and manage projects with titles, descriptions, statuses, and due dates.
- Add tasks to projects with details like title, description, status, priority, and due dates.
- View project details along with associated tasks.
- Pagination for project lists.
- Custom error pages for 404 and 500 errors.

## Prerequisites
- Python 3.8 or higher
- Flask and its dependencies
- SQLite (default database)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/AlphaC137/FMP
   cd FMP
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (optional):
   - `SECRET_KEY`: A secret key for Flask sessions.
   - `DATABASE_URI`: The URI for the database (default is SQLite).
   - [Learn How](templates/setup_env.md)

5. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```bash
   flask run
   ```

7. Open your browser and navigate to `http://127.0.0.1:5000`.

## File Structure
- `app.py`: Main application file.
- `templates/`: Contains HTML templates for the application.
- `instance/projects.db`: SQLite database file.
- `README.md`: Project documentation.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to fork this repository and submit pull requests for improvements or bug fixes.