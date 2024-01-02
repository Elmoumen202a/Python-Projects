import pyqrcode
import png

def generate_QRcode(link, filename):
    qr_code = pyqrcode.create(link)
    qr_code.png(filename, scale=5)

if __name__ == "__main__":
    link = "  "  # Add your  link here
    generate_QRcode(link, "output.png")
