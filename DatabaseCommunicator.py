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
        return Customer(username, password, voucherIDs, loyaltyPoint)
	

def retrieveVendor(username, password):
	# Search vendor database and return vendor class
	dataQuery = '''SELECT * FROM vendor WHERE userID=? AND userPW=?'''
        records = db.execute(dataQuery, (username, password))
        voucherspurchased = [record[2] for record in records]
        return Vendor(username, password, voucherspurchased)
        
# takes the Customer and updates customer database
def updateCustomer(Customer):        
    return  

