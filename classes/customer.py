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
        #self.cart = {10: 0,                    # these are the only voucher options
        #             20: 0,
        #             50: 0,
        #             100: 0}
        self.cart = {}
        
    #def add_voucher(self, voucherAmount):
    #    self.cart[voucherAmount]+=1
    #def drop_voucher(self, voucherAmount):
    #    if self.cart[voucherAmount]>0:
    #        self.cart[voucherAmount]-=1
    def add_voucher(self, vendorName, denomination):
        x = (vendorName, denomination)
        if x not in self.cart.keys():
            self.cart[x] = 1
        else:
            self.cart[x] += 1
    def drop_voucher(self, vendorName, denomination):
        x = (vendorName, denomination)
        if self.cart[x] > 1:
            self.cart[x] -= 1
        else:
            del self.cart[x]
                
    def purchase(self):
        # assume payment made successfully
        successful = True
        if successful:
            for amount in self.cart:
                while self.cart[amount]>0:
                    voucher = Voucher(self.username, amount[1], amount[0])
                    self.Vouchers.append(voucher)
                    self.cart[amount]-=1
                    db.execute("insert into users values (userID, userPW, voucherID, voucherAmount, vendorID) values (?, ?, ?, ?, ?)",
                              (self.username, self.password, voucher.voucherID, voucher.amount, voucher.vendor_username))
                    points_earned = amount * 0.1 #this will depend on the calculation we choose to adopt
                    new_points = points_earned + db.execute("SELECT loyaltyPoints WHERE userID=?",
                                                           (self.username))
                    db.execute("UPDATE loyalty SET loyaltyPoints = ? WHERE userID=?", (new_points, self.username))
                    db.execute("insert into vendors values (vendorID, vendorPW, voucherID, voucherStatus, voucherAmount) values (?, ?, ?, ?, ?)",
                              (voucher.vendor_username, "", voucher.voucherID, "Purchased", voucher.amount)
                    db.commit()
        
                     
                    
    # call updateDatabase(Customer) right after    
    
    # this happens after the user clicks use voucher on the interface
    # then somehow the frontend will pass the voucher instance or voucherID over?
    # for now it will just show the qr code since when the vendor scans the qr code, the updates to database are done over there
    def redeem(self, voucher):
        # assume it gives us a voucher class instance
        return voucher.generate_qr()
    def redeem_2(self, amount, vendor_username, voucherID):
        voucher = Voucher(self.username, amount, vendor_username)
        voucher.voucherID = voucherID
        return voucher.generate_qr()
    
    def get_username(self):
        return self.username
    def get_Vouchers(self):
        return self.Vouchers
    def get_loyaltyPoints(self):
        return self.loyaltyPoints
