## Web Application Vulnerability Scanner:

This project is a simple web vulnerability scanning system.

## Features
- Detects common security vulnerabilities
- Assigns severity levels (Critical, High, Medium, Low)
- Displays results in a dashboard
- Sends automated email alerts for high risk vulnerabilities

## Technologies Used
- Python
- Flask
- Requests Library
- SMTP (Email Alert)

## Project Files
scanner.py – scans the target website for vulnerabilities  
dashboard.py – displays the scan results in a dashboard  
email_alert.py – sends email alerts when critical vulnerabilities are found  

## How to Run

Step 1: Install required libraries
pip install requests flask

Step 2: Run scanner
python scanner.py

Step 3: Run dashboard
python dashboard.py

Step 4: Run email alert
python email_alert.py

## Output
The scanner identifies vulnerabilities and assigns secerity levels.  
The dashboard visualizes the risk level.  
The email alert sends notifications for high and critical vulnerabilities.

## Author
Elakkiyaa Viswanathan
