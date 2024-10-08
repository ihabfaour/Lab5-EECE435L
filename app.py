from flask import Flask, request, jsonify
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)



if __name__ == "__main__":
    # Create the database table
    create_db_table()
    app.run(debug=True)