import cv2 as cv
class Vendor():
    def __init__(self,username,password,voucherspurchased):
        self.username = username
        self.password = password
        self.voucherspurchased = voucherspurchased
    
    def scanQR(self, qr_image):
        im = cv.imread(qr_image)
        det = cv.QRCodeDetector()
        retval, points, straight_qrcode = det.detectAndDecode(im)
        customerUsername, voucherID, amount, vendorUsername  = retval.split(',')    
        self.useVoucher(customerUsername,voucherID,vendorUsername)
            
    # this is called by the vendor when customer uses a voucher - requires username to search for customer in customer database
    # expires the voucher with matching voucherID
    def useVoucher(self,customerUsername,voucherID,vendorUsername):
        if voucherID in self.voucherspurchased:
            self.voucherspurchased.remove(voucherID)
            db.execute('''DELETE FROM users WHERE userID=? AND voucherID=?''', (customerUsername, voucherID))
            db.execute('''UPDATE vendors SET voucherStatus = "Redeemed" where vendorID=? AND voucherID=?''', (vendorUsername, voucherID))
            db.commit()
            return "Voucher successfully redeemed!"
        else:
            return "Not a valid voucher"        
        # should update customer database/ remove the voucher
     
    def postVoucher(self, denomination):
        x = db.execute("")
        y = x.rowcount() > 0
        #need to check if the denomination + vendor name is already in the database
        if not y:
            db.execute("insert into vouchers values (vendorname, denomination) values (?, ?)",
                      (self.username, denomination))
            return "Voucher successfully added!"
        else:
            return "Voucher is already on sale!"
        
    def removeVoucher(self, denomination):
        x = db.execute("")
        y = x.rowcount()>0
        #need to check if the denomination + vendor name is in the database
        if y:
            db.execute("delete from vouchers where vendorname = ? and denomination = ?", (self.username, denomination))
            return "Voucher successfully removed!"
        else:
            return "Voucher is not currently on sale!"
                       
