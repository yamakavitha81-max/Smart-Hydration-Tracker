Smart Hydration Tracker

Overview

Smart Hydration Tracker is a Python and Streamlit-based web application that calculates daily water intake requirements based on body weight, physical activity, and temperature. It helps users track hydration levels, store daily data, and visualize progress using graphs.

Features

- Calculates daily water requirement based on weight
- Adjusts hydration needs based on activity levels
- Considers temperature impact on water requirement
- Shows hydration percentage and status
- Saves daily data in CSV file
- Displays hydration history using graphs
- Provides hydration tips based on user condition
- Allows downloading hydration history

Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- datetime module
- os module

Project Structure

smart-hydration/
│
├── app.py
├── hydration_data.csv
├── requirements.txt
├── README.md
└── assets/
    └── screenshot.png

Installation and Setup

1. Clone the repository
git clone https://github.com/your-username/smart-hydration-tracker.git

2. Go to project folder
cd smart-hydration-tracker

3. Install dependencies
pip install streamlit pandas matplotlib

4. Run the application
streamlit run app.py

How It Works

1. User enters weight, temperature, and activity details
2. System calculates required water intake
3. User enters water consumed
4. Hydration percentage is calculated
5. Data is stored in CSV file
6. Graph shows hydration history over time

Future Improvements

- Add user login system
- Weekly and monthly analytics dashboard
- Mobile responsive UI
- Automated water intake reminders
- Cloud database integration

Author

Name: Yama Kavitha  
GitHub: https://github.com/your-username  

License

This project is for educational purposes only.
