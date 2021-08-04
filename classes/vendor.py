import cv2 as cv
class Vendor():
    def __init__(self,username,password,voucherIDs):
        self.username = username
        self.password = password
        # voucherIDs is a list of voucherIDs only
        self.voucherIDs = voucherIDs
        # because we have unlimited vouchers should we update our list of voucherIDs in useVoucher?
    
    def scanQR(self, qr_image):
        im = cv.imread(qr_image)
        det = cv.QRCodeDetector()
        retval, points, straight_qrcode = det.detectAndDecode(im)
        customerUsername, voucherID, amount, vendorUsername  = retval.split(',')    
        self.useVoucher(customerUsername,voucherID,vendorUsername)
            
    # this is called by the vendor when customer uses a voucher - requires username to search for customer in customer database
    # expires the voucher with matching voucherID
    def useVoucher(self,customerUsername,voucherID,vendorUsername):
        if voucherID in self.voucherIDs:
            self.voucherIDs.remove(voucherID)
            db.execute('''DELETE FROM users WHERE userID=? AND voucherID=?''', (customerUsername, voucherID))
            db.execute('''UPDATE vendors SET voucherStatus = "Redeemed" where vendorID=? AND voucherID=?''', (vendorUsername, voucherID))
            db.commit()
            return "Voucher successfully redeemed!"
        else:
            return "Not a valid voucher"        
        # should update customer database/ remove the voucher
    
    # check with hon zheng which might be a better fit for our use 
    # for this one our voucherIDs might be obsolete
    def useVoucher_2(self, customerUsername, voucherID, vendorUsername):
        sqlQuery = '''SELECT * FROM vendors WHERE voucherID=? AND vendorUsername=?'''
        query = db.execute(sqlQuery, (voucherID, vendorUsername))
        voucherDetails = query.fetchone()
        # by here, we should expect to only have one row if the voucher exists right?
        if query.rowcount() > 0 and voucherDetails[3] == "Purchased":
            db.execute('''DELETE FROM users WHERE userID=? AND voucherID=?''', (customerUsername, voucherID))
            db.execute('''UPDATE vendors SET voucherStatus = "Redeemed" where vendorID=? AND voucherID=?''', (vendorUsername, voucherID))
            db.commit()
            # do we have to return the voucher amount or the frontend will keep track of it?
            return "Voucher successfully redeemed!"
        else:
            return "Not a valid voucher"             
        
    
    # for offering a particular denomination of a voucher on the store
    def postVoucher(self, denomination):
        # change x and y to something more interpretable?
        sqlQuery = '''SELECT * FROM vouchers WHERE vendorID = ? AND denomination =?'''
        # need to check if self.username is correct 
        x = db.execute(sqlQuery, (self.username, denomination))
        y = x.rowcount() > 0
        #need to check if the denomination + vendor name is already in the database
        if not y:
            db.execute("insert into vouchers values (vendorID, denomination) values (?, ?)",
                      (self.username, denomination))
            return "Voucher successfully added!"
        else:
            return "Voucher is already on sale!"
    # for removing a particular denomination of a voucher from the store    
    def removeVoucher(self, denomination):
        sqlQuery = '''SELECT * FROM vouchers WHERE vendorID = ? AND denomination = ?'''
        x = db.execute(sqlQuery, (self.username, denomination)
        y = x.rowcount()>0
        #need to check if the denomination + vendor name is in the database
        if y:
            db.execute("delete from vouchers where vendorID = ? and denomination = ?", (self.username, denomination))
            return "Voucher successfully removed!"
        else:
            return "Voucher is not currently on sale!"
                       
