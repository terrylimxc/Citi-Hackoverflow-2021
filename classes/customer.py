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
                
    def purchase(self):
        # assume payment made successfully
        successful = True
        if successful:
            for amount in self.cart:
                while self.cart[amount]>0:
                    self.Vouchers.append(Voucher(self.username, amount))
                    self.cart[amount]-=1
    # call updateDatabase(Customer) right after    
    
    
    def get_username(self):
        return self.username
    def get_Vouchers(self):
        return self.Vouchers
    def get_loyaltyPoints(self):
        return self.loyaltyPoints