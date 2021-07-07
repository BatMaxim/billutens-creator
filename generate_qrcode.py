import qrcode


def generate_qrcode(data):
    filename = "user_qr.png"
    img = qrcode.make(data)
    img.save(filename)

