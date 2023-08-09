import pandas as pd
import random
import mysql.connector
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

#Data Serialization and Deserialization
def serialize_data_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def deserialize_data_from_excel(filename):
    df = pd.read_excel(filename)
    data = df.to_dict(orient='records')
    return data

#Inserting Data into the Database
def batch_insert_employees(employees):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ashirvad',
        database='techville_db'
    )

    cursor = connection.cursor()
    query = "INSERT INTO Employee (employee_id, name, designation, salary) VALUES (%s, %s, %s, %s)"
    values = [(employee['employee_id'], employee['name'], employee['designation'], employee['salary']) for employee in employees]

    cursor.executemany(query, values)
    connection.commit()

    cursor.close()
    connection.close()

def batch_insert_companies(companies):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ashirvad',
        database='techville_db'
    )

    cursor = connection.cursor()
    query = "INSERT INTO Company (company_id, company_name, location, founded_year) VALUES (%s, %s, %s, %s)"
    values = [(company['company_id'], company['company_name'], company['location'], company['founded_year']) for company in companies]

    cursor.executemany(query, values)
    connection.commit()

    cursor.close()
    connection.close()

class UploadData(Resource):
    def post(self):
        try:
            employee_file = request.files['employee_file']
            company_file = request.files['company_file']

            # Save uploaded files
            employee_filename = 'employee_data.xlsx'
            company_filename = 'company_data.xlsx'
            employee_file.save(employee_filename)
            company_file.save(company_filename)

            # Deserialize data from Excel files
            deserialized_employees = deserialize_data_from_excel(employee_filename)
            deserialized_companies = deserialize_data_from_excel(company_filename)

            # Insert data into the database using batch insert
            batch_insert_employees(deserialized_employees)
            batch_insert_companies(deserialized_companies)

            return {'message': 'Data uploaded and inserted successfully.'}, 201
        except Exception as e:
            return {'message': 'Error uploading and inserting data.', 'error': str(e)}, 500

api.add_resource(UploadData, '/upload')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
