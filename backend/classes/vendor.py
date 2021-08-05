class Vendor():
  def __init__(username, password):
    self.username = username
    self.password = password
    # self.role = "Overview" # this is for when you want to retrieve the entire voucher database?
  
  def show_vouchers(self, *filters):
    # displays all the vouchers in the vouchers table across all vendors
    # assume filters are a list of vendorUsernames for the overview to only search for some vendors
    # this is a filter that only shows vendors that are in the filter given
    # can do more complicated stuff like filtering by expiry date or voucher status if we have time and its feasible
    # can remove also if its too difficult
    # returns a list of tuples containing vendorID, voucherID and voucherStatus
    #merged = db.execute('''SELECT vendors.vendorID, vendors.voucherID, vendors.voucherStatus, records1.userID, records1.voucherAmount FROM records LEFT JOIN records1 ON records.voucherID = records1.voucherID'''
    sqlQuery = '''SELECT vendorID, voucherID, voucherStatus, userID, voucherAmount FROM vendors WHERE vendorID = ?'''
    records = db.execute(sqlQuery, (self.username,))
    #secondQuery = '''SELECT userID, voucherID, voucherAmount FROM users WHERE vendorID = ?'''
    #records1 = db.execute(secondQuery, (self.username,))
    #finalrecords = db.execute('''SELECT records.vendorID, records.voucherID, records.voucherStatus, records1.userID, records1.voucherAmount FROM records LEFT JOIN records1 ON records.voucherID = records1.voucherID'''
    ans = []
    if filters:
      records = [record for record in records if record[2] in filters]
      # for this one do we just return the records to the front end or do the backend need to print it out?
      for record in records:
        temp = Voucher(record[3], record[4], record[0])
        temp.voucherID = record[1]
        ans.append(temp)
      return ans
    else:
      for record in records:
        temp = Voucher(record[3], record[4], record[0])
        temp.voucherID = record[1]
        ans.append(temp)
      return ans
  
  #for offering a particular denomination of a voucher on the store
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
          db.commit()
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
          db.commit()
          return "Voucher successfully removed!"
      else:
          return "Voucher is not currently on sale!"
