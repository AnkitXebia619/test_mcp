# Flask Application Demo

A simple Flask web application with basic routing and templates.

## Features

- Home page
- About page
- Contact form with form submission
- Responsive design with CSS styling
- Thank you page after form submission

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/AnkitXebia619/test_mcp.git
   cd test_mcp
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

```
python app.py
```

The application will be available at http://127.0.0.1:5000/

## Project Structure

```
.
├── app.py                  # Main Flask application file
├── requirements.txt        # Python dependencies
├── static/                 # Static files
│   └── css/
│       └── style.css       # CSS stylesheets
└── templates/              # HTML templates
    ├── index.html          # Home page
    ├── about.html          # About page
    ├── contact.html        # Contact form
    └── thank_you.html      # Thank you page
```

## Deployment

For production deployment, consider:

1. Setting `debug=False` in app.py
2. Using a production WSGI server like Gunicorn
3. Setting up a reverse proxy with Nginx or Apache

Example Gunicorn command:
```
gunicorn app:app
```