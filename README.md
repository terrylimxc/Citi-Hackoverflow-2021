# Citi-Hackoverflow-2021
Source code for Web Application for Citi Hackathon 2021

## How to use:
1. Clone/Download the repository
2. Using the Command Line Interface, cd to the repository folder and run the following commands
  - For Windows:
    - `python -m venv auth`
    - `auth\Scripts\activate.bat`
    - `pip install -r requirements.txt`
    - `set FLASK_APP=project`
    - `flask run`
  - For Mac/Linux:
    - `python -m venv auth`
    - `source auth/bin/activate`
    - `pip install -r requirements.txt`
    - `export FLASK_APP=project`
    - `flask run`
 3. Open the localhost link in your preferred web browser (Best with **Responsive Design Mode** enabled)

<p align="center">
  <img src="https://user-images.githubusercontent.com/49337598/128386962-ec9f74b9-a0da-4348-8f9d-16f03866c64a.png" width="600" height="300">
</p>

## Packages required:
* Flask == 2.0.1
* Flask_Login == 0.5.0
* Flask_QRcode == 3.0.0
* Flask_SQLAlchemy == 2.5.1
* Werkzeug == 2.0.1
* opencv_python == 4.5.3.56
* qrcode == 7.2
