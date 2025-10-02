import qrcode

url = "https://wadoodabdul.github.io/greeting_card_mafp/index.html"
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("my_website_qr.png")
