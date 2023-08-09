# FlaskHR_Excel_to_MySQL Employee and Company Management App

This is a Flask-based web application that allows users to upload Excel files containing employee and company data. The data is processed and inserted into a MySQL database. The application provides a REST API for data upload and insertion.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Built With](#built-with)
- [License](#license)

## Getting Started

### Prerequisites

Before running this application, make sure you have the following installed:

- Python (3.6 or higher)
- MySQL Server
- Pip (Python package manager)

### Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/techville-app.git
   cd techville-app
   ```

2. Install the required Python packages using pip:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure the environment variables:
   - Create a `.env` file in the project directory.
   - Add the following environment variables:
     ```
     DATABASE_URL=your_mysql_database_url
     SECRET_KEY=your_secret_key
     ```

4. Run the application:
   ```sh
   python app.py
   ```

## Usage

- Access the application by opening your web browser and navigating to http://localhost:5000.
- Use the provided form to upload Excel files containing employee and company data.

## API Endpoints

- **POST /upload**: Upload employee and company data Excel files and insert the data into the database.

## Deployment

This application can be deployed on platforms like Heroku or Render. Follow the deployment guides for the platform of your choice.

## Built With

- Flask - Web framework
- pandas - Data manipulation
- mysql-connector-python - MySQL database connection
- flask-restful - Building RESTful APIs
- gunicorn - Web server



Replace placeholders such as `your-username`, `your_mysql_database_url`, and `your_secret_key` with the appropriate values. Customize the content to match your application's features and functionalities.
