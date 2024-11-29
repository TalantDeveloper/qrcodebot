import qrcode
from PIL import Image

# Data to encode in the QR Code
data = "https://example.com"

# Create a QR Code instance
qr = qrcode.QRCODE(
    version=1,  # Controls the size of the QR Code (1 = 21x21, 40 = 177x177)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # Size of each box in the QR Code grid
    border=4,  # Border size
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Generate the QR Code image
qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the icon (must be a smaller image)
icon = Image.open("icon.png")  # Replace with the path to your icon
icon_size = 80  # Desired size of the icon in the QR Code

# Resize the icon to fit into the QR Code
icon = icon.resize((icon_size, icon_size), Image.ANTIALIAS)

# Calculate position to place the icon at the center
qr_width, qr_height = qr_image.size
icon_width, icon_height = icon.size
x = (qr_width - icon_width) // 2
y = (qr_height - icon_height) // 2

# Paste the icon onto the QR Code (with transparency support if needed)
qr_image.paste(icon, (x, y), mask=icon)

# Save or display the resulting QR Code
qr_image.save("qr_with_icon.png")
qr_image.show()