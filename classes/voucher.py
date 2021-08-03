import uuid
import qrcode
class Voucher():
    def __init__(self, username, amount):
        self.username = username                                     # tagged to customer's username
        self.amount = amount
        self.voucherID = uuid.uuid1().hex
    def get_voucherID(self):
        return self.voucherID
    def get_amount(self):
        return self.amount
    def get_username(self):
        return self.username
    def generate_qr(self):
        qr_generator = qrcode.QRCode(version=1,
                                     box_size=10,
                                     border=5)
        input_data = f"{self.username},{self.voucherID},{self.amount}"
        qr_generator.clear()
        qr_generator.add_data(input_data)
        return qr_generator.make_image() 