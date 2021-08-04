from classes.vendor import Vendor
from classes.customer import Customer
from classes.voucher import Voucher

def retrieveCustomer(username, password):
	# Search customer database and return customer class
	userDataQuery = '''SELECT * FROM users WHERE userID=? AND userPW=?'''
        loginDataQuery = '''SELECT loyaltyPoint FROM loyalty WHERE userID=? AND userPW=?'''
        records = db.execute(userDataQuery, (username, password))
        loyaltyPoint = db.execute(loginDataQuery, (username, password))
        voucherIDs = [record[2] for record in records]
        return Customer(username, password, voucherIDs, loyaltyPoint[0])
	

def retrieveVendor(username, password):
	# Search vendor database and return vendor class
	dataQuery = '''SELECT * FROM vendors WHERE vendorID=? AND vendorPW=?'''
        records = db.execute(dataQuery, (username, password))
        voucherIDs = [record[2] for record in records]
        return Vendor(username, password, voucherIDs)
        
# takes the Customer and updates customer database
def updateCustomer(Customer):        
    return  

