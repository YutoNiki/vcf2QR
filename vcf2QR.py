#vcf2QR
import qrcode
import vobject
from IPython.display import Image,display_png

def generate_qr_code(vcf_file, output_file):
    with open(vcf_file, 'r', encoding='utf-8') as f:
        vcard_data = f.read()

    vcard = vobject.readOne(vcard_data)
    vcard_string = vcard.serialize()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

if __name__ == "__main__":
    vcf_file = "vCard.vcf"
    output_file = "QR.png"
    generate_qr_code(vcf_file, output_file)

display_png(Image('QR.png'))