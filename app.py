from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# MongoDB Atlas connection - lazy initialization
client = None
db = None
collection = None

def get_mongodb_collection():
    """Lazy initialization of MongoDB connection"""
    global client, db, collection
    
    # Reload environment variable to get latest value
    load_dotenv()
    mongo_uri = os.getenv('MONGO_URI')
    
    if not mongo_uri or not mongo_uri.startswith('mongodb+srv://'):
        raise ValueError("MongoDB connection string not configured properly. Please update .env file with your MongoDB Atlas credentials.")
    
    if client is None:
        try:
            client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
            # Test connection
            client.admin.command('ping')
            db = client['flask_app_db']
            collection = db['submissions']
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB Atlas: {str(e)}")
    
    return collection

@app.route('/api')
def api_route():
    """API route that returns JSON list from backend file"""
    try:
        with open('backend_data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify([])
    except json.JSONDecodeError:
        return jsonify([])

@app.route('/')
def index():
    """Home page with the form"""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    """Handle form submission to MongoDB Atlas"""
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Validate required fields
        if not name or not email:
            flash('Name and email are required fields', 'error')
            return render_template('index.html')
        
        # Get MongoDB collection (lazy initialization)
        mongo_collection = get_mongodb_collection()
        
        # Insert into MongoDB
        submission = {
            'name': name,
            'email': email,
            'message': message,
            'created_at': '2024-01-01'  # Simplified date
        }
        
        mongo_collection.insert_one(submission)
        
        return redirect(url_for('success'))
        
    except ValueError as e:
        flash(f'Configuration error: {str(e)}', 'error')
        return render_template('index.html')
    except ConnectionError as e:
        flash(f'Connection error: {str(e)}', 'error')
        return render_template('index.html')
    except Exception as e:
        flash(f'Error submitting data: {str(e)}', 'error')
        return render_template('index.html')

@app.route('/success')
def success():
    """Success page displayed after successful submission"""
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
