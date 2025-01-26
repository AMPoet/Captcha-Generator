from captcha.image import ImageCaptcha
from PIL import Image
import random
import string


def generate_captcha_text(length=6):
    # Fixed syntax error in random.choice
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_and_save_captcha(image_width=280, image_height=90, captcha_length=6, image_path='C:/Users/vivobook/Desktop/captcha.png'):
    # Renamed Image to image_generator to avoid conflict with PIL.Image
    image_generator = ImageCaptcha(width=image_width, height=image_height)
    captcha_text = generate_captcha_text(captcha_length)
    data = image_generator.generate(captcha_text)
    image_generator.write(captcha_text, image_path)
    return captcha_text

if __name__ == '__main__':
    text = generate_and_save_captcha()
    print(f"Generated CAPTCHA text: {text}")
    # Open and show the image
    captcha_image = Image.open('C:/Users/vivobook/Desktop/captcha.png')
    captcha_image.show()