import qrcode
import cv2


def qr_generator(username, company, denomination):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data("{},{},{}".format(username, company, denomination))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    return img


def qr_decoder(img):
    im = cv2.imread(img)
    det = cv2.QRCodeDetector()
    values, points, straight_qrcode = det.detectAndDecode(im)
    return values