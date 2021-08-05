# code to initialise customer database
# contains 4 tables
# loyalty for storing loyalty points of user (col names: userID, loyaltyPoints)
#users for storing details of users and their vouchers they own (col names: userID, userPW, voucherID, voucherAmount, vendorID)
#vendors for allowing vendors to check vocuhers they have issued along with the voucher's information and the buyer (col names: vendorID, vendorPW, voucherID, voucherStatus, voucherAmount, userID)
#vouchers for keeping track of the types of vouchers that are currently on sale (col names: vendorname, denomination)

import sqlite3

conn = sqlite.connect('database.db')
db = conn.cursor()

db.execute('''create table loyalty (userID text, loyaltyPoints int)''')
db.execute('''create table users (userID text, userPW text, voucherID text, voucherAmount int, vendorID text)''')
db.execute('''CREATE TABLE vendors (vendorID text, vendorPW text, voucherID text, voucherStatus text, voucherAmount int, userID text)''') #the 2 status names will be Purchased and Redeemed
db.execute('''CREATE table vouchers (vendorID text, denomination int)''')

db.commit()
db.close()
