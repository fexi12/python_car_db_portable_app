@echo off
REM Run the Flask app and open the browser
start chrome http://127.0.0.1:5000  REM Opens your default browser to the Flask app URL
python app.py  REM Make sure app.py contains the app setup

REM Keep the command prompt window open after the script ends
pause