# code to initialise customer database
# contains 4 tables
# loyalty for storing loyalty points of user (col names: userID, loyaltyPoints)
#users for storing details of users and their vouchers they own (col names: userID, userPW, voucherID, voucherAmount, vendorID)
#vendors for allowing vendors to check vocuhers they have issued along with the voucher's information (col names: vendorID, vendorPW, voucherID, voucherStatus, voucherAmount)
#vouchers for keeping track of the types of vouchers that are currently on sale (col names: vendorname, denomination)

# need to confirm if vendorname = vendorID and standardise, and ask if we shd change denomination type to int

import sqlite3

conn = sqlite.connect('database.db')
db = conn.cursor()

db.execute('''create table loyalty (userID text, loyaltyPoints int)''')
db.execute('''create table users (userID text, userPW text, voucherID text, voucherAmount int, vendorID text)''')
db.execute('''CREATE TABLE vendors (vendorID text, vendorPW text, voucherID text, voucherStatus text, voucherAmount int)''') #the 2 status names will be Purchased and Redeemed
db.execute('''CREATE table vouchers (vendorname text, denomination text)''') # shd we change denomination type to int?

db.commit()
db.close()
