# Install The Module By "pip install pillow"
from PIL import Image

# Open Image
orginal = Image.open("Belgin_Android.png")

# Image rotate & show
orginal.rotate(45).show()
