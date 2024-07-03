# World Bank Dashboard

## Overview

This project is a web application dashboard that visualizes data from the World Bank API. The dashboard is built with a Flask backend and a Bootstrap frontend, and it is deployed using Adaptable.io's free tier.

## Features

- **Interactive Charts**: Displays GDP and Population data for the US and Germany from 2011 to 2021.
- **Key Metrics**: Shows interesting metrics such as GDP Growth, Life Expectancy, Unemployment Rate, and Internet Users for the US and Germany.
- **Responsive Design**: Uses Bootstrap to ensure the dashboard is mobile-friendly and looks good on all devices.

## Tech Stack

- **Backend**: Flask
- **Frontend**: Bootstrap
- **Deployment**: Adaptable.io
- **Version Control**: GitHub / Git

## Prerequisites

- Python 3.6 or higher
- Flask
- Requests
- Chart.js (included in the frontend via CDN)

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/NikoHems/worldbank_dashboard.git
   cd worldbank_dashboard
   ```

2. **Create and Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

Before running the application, you need to set up your environment variables. Create a `.env` file in the root directory and add the following:
```
FLASK_APP=run.py
FLASK_ENV=development
```

## Running the Application

1. **Start the Flask Development Server**
   ```sh
   flask run
   ```

2. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:5000/`.

## Deployment

1. **Push to GitHub**
   Make sure all your changes are committed and pushed to GitHub:
   ```sh
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. **Deploy on Adaptable.io**
   Follow the instructions on Adaptable.io to link your GitHub repository and deploy your application. Ensure the start command is set to:
   ```sh
   gunicorn run:app
   ```

## Project Structure

```
worldbank_dashboard/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── dashboard.html
│   │   ├── index.html
│   └── services/
│       └── worldbank_api.py
├── static/
│   ├── css/
│   ├── js/
│       └── chart.min.js
├── .env
├── .gitignore
├── requirements.txt
├── Procfile
└── run.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
