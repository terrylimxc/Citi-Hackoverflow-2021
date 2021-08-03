from .voucher import Voucher

class Customer():
    def __init__(self, 
                 username:str, 
                 password:str, 
                 Vouchers:list , 
                 loyaltyPoints: int): 
        self.username = username
        self.password = password
        self.Vouchers = Vouchers
        self.loyaltyPoints = loyaltyPoints
        self.cart = {10: 0,                    # these are the only voucher options
                     20: 0,
                     50: 0,
                     100: 0} 
        
    def add_voucher(self, voucherAmount):
        self.cart[voucherAmount]+=1
    def drop_voucher(self, voucherAmount):
        if self.cart[voucherAmount]>0:
            self.cart[voucherAmount]-=1
                
    def purchase(self, vendorUsername):
        # assume payment made successfully
        successful = True
        if successful:
            for amount in self.cart:
                while self.cart[amount]>0:
                    voucher = Voucher(self.username, amount, vendorUsername)
                    self.Vouchers.append(voucher)
                    self.cart[amount]-=1
                    db.execute("insert into users values (userID, userPW, voucher) values (?, ?, ?)",
                              (self.username, self.password, voucher.voucherID))
                    points_earned = amount * 0.1 #this will depend on the calculation we choose to adopt
                    db.execute("insert into loyalty values (userID, loyaltyPoints) values (?, ?)",
                              (self.username, points_earned))
                    db.execute("insert into vendor values (userID, userPW, voucherspurchased) values (?, ?, ?)",
                              (voucher.vendor_username, "", voucher.voucherID)
                    db.execute("insert into overview values (userID, userPW, vouchersID, voucherstatus, vendorUsername) values (?, ?, ?)",
                              ("", "", voucher.voucherID, "Purchased", voucher.vendor_username))          
                     
                    
    # call updateDatabase(Customer) right after    
    
    
    def get_username(self):
        return self.username
    def get_Vouchers(self):
        return self.Vouchers
    def get_loyaltyPoints(self):
        return self.loyaltyPoints
