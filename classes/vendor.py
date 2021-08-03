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
        customerUsername, voucherID, amount  = retval.split(',')    
        self.useVoucher(customerUsername,voucherID)
            
    # this is called by the vendor when customer uses a voucher - requires username to search for customer in customer database
    # expires the voucher with matching voucherID
    def useVoucher(self,customerUsername,voucherID):
        if voucherID in self.voucherspurchased:
            self.voucherspurchased.remove(voucherID)
            db.execute('''DELETE FROM users WHERE userID=? AND voucher=?''', (customerUsername, voucherID))
            db.commit()
            return "Voucher successfully redeemed!"
        else:
            return "Not a valid voucher"        
        # should update customer database/ remove the voucher
