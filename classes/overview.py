class Overview():
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
    sqlQuery = '''SELECT vendorID, voucherID, voucherStatus FROM vendors'''
    records = db.execute(sqlQuery)
    if filters:
      records = [record for record in records if record[1] in filters]
      # for this one do we just return the records to the front end or do the backend need to print it out?
      return records
    else:
      return records
