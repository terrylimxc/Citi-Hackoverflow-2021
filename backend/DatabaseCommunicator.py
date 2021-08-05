from classes.vendor import Vendor
from classes.customer import Customer
from classes.voucher import Voucher

def retrieveCustomer(username, password):
	# Search customer database and return customer class
	userDataQuery = '''SELECT * FROM users WHERE userID=? AND userPW=?'''
        loyaltyDataQuery = '''SELECT loyaltyPoint FROM loyalty WHERE userID=? AND userPW=?'''
        records = db.execute(userDataQuery, (username, password))
        loyaltyPoint = db.execute(loyaltyDataQuery, (username, password))
        voucherList = []
	for record in records:
		voucherID = record[2]
		voucher = Voucher(username, record[3], record[4])
		voucher.voucherID = voucherID
		voucherList.append(voucher)
        return Customer(username, password, voucherList, loyaltyPoint[0])
	

def retrieveVendor(username, password):
	# Search vendor database and return vendor class
	dataQuery = '''SELECT * FROM vendors WHERE vendorID=?'''
	# removed searching by vendorPW cause Customer purchase will not insert vendorPW
        records = db.execute(dataQuery, (username,))
        voucherIDs = [record[2] for record in records]
        return Vendor(username, password, voucherIDs)
        
# takes the Customer and updates customer database
def updateCustomer(Customer):        
    return  

