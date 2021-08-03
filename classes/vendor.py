class Vendor():
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def scanQR(self, value):                   # input should be "jacky,cf7788eff41511ebb4939cb6d0216836,50"
        customerUsername, voucherID, amount  = value.split(',')    
        self.useVoucher(customerUsername,voucherID)
            
    # this is called by the vendor when customer uses a voucher - requires username to search for customer in customer database
    # expires the voucher with matching voucherID
    def useVoucher(self,customerUsername,voucherID):
        return
        
        # should update customer database/ remove the voucher