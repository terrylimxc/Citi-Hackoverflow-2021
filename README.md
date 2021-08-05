# Citi-Hackoverflow-2021
Source code for Web Application for Citi Hackathon 2021

## Setup:
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

## How to use:
1. Create a Vendor account. The Secret codes for the respective organisations could be found in access_codes.txt
2. Create new Vouchers to be sold in the **Sell Vouchers** tab on the webpage.
3. (Optional) You can create more Vendor accounts to have a bigger variety of vouchers in the database.
4. Create a User acccount.
5. Buy vouchers available in the marketplace in the **Buy Vouchers** tab on the webpage. Click checkout to view selected vouchers.
6. Click buy to confirm order.
7. View newly bought vouchers under the **My Vouchers** tab.
8. You can also view your current *Loyalty Points* and *Number of Vouchers* in the **Home** tab.
9. You can use your vouchers by clicking on the Use button for the voucher in the **My Voucher** tab. The QR code for that voucher would be generated.
