# Flask MongoDB Atlas Application

A Flask web application that demonstrates data submission to MongoDB Atlas with a JSON API endpoint.

## Features

- **API Endpoint**: `/api` route that returns JSON data from a backend file
- **Form Submission**: Frontend form that submits data to MongoDB Atlas
- **Success/Error Handling**: Redirects to success page on successful submission, displays errors on the same page
- **Responsive Design**: Clean, modern UI with CSS styling

## Project Structure

```
flask-tutorial/
├── app.py                 # Main Flask application
├── backend_data.json      # Backend data file for API
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables example
├── templates/
│   ├── index.html        # Main form page
│   └── success.html      # Success page
└── README.md             # This file
```

## Setup Instructions

### 1. Prerequisites
- Python 3.7 or higher
- MongoDB Atlas account and cluster
- Git

### 2. Clone and Setup
```bash
git clone <your-repo-url>
cd flask-tutorial
```

### 3. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Setup
1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` file with your MongoDB Atlas connection string:
```
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority
```

Replace:
- `<username>`: Your MongoDB Atlas username
- `<password>`: Your MongoDB Atlas password
- `<dbname>`: Your database name

### 6. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

### API Endpoint
Access `http://localhost:5000/api` to get JSON data from `backend_data.json`

### Form Submission
1. Visit `http://localhost:5000`
2. Fill out the form with name, email, and message
3. Click "Submit" to save data to MongoDB Atlas
4. On success, you'll be redirected to the success page
5. If there's an error, it will be displayed on the form page

## MongoDB Atlas Setup

1. **Create a Cluster**: Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create a free cluster
2. **Create Database User**: Under "Database Access", create a new user with a strong password
3. **Whitelist IP Address**: Under "Network Access", add your IP address (or 0.0.0.0/0 for all access)
4. **Get Connection String**: Click "Connect" → "Connect your application" → Copy the connection string
5. **Update .env**: Replace the connection string in your `.env` file

## Screenshots

### Form Page
![Form Page](screenshots/form_page.png)

### Success Page
![Success Page](screenshots/success_page.png)

### API Response
![API Response](screenshots/api_response.png)

## Testing

### Test the API Endpoint
```bash
curl http://localhost:5000/api
```

### Test Form Submission
1. Open browser to `http://localhost:5000`
2. Fill out the form and submit
3. Check MongoDB Atlas to verify data was inserted

## Dependencies

- **Flask**: Web framework
- **pymongo**: MongoDB driver for Python
- **python-dotenv**: Environment variable management

## Troubleshooting

### Common Issues

1. **MongoDB Connection Error**:
   - Verify your connection string in `.env`
   - Check if your IP is whitelisted in MongoDB Atlas
   - Ensure your database user has the correct permissions

2. **Module Import Error**:
   - Make sure you're in the virtual environment
   - Run `pip install -r requirements.txt` again

3. **Port Already in Use**:
   - Change the port in `app.py` or stop the conflicting service

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
