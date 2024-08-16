from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

def preprocess_img(img):
    # convert to grayscale
    img = img.convert('L')

    # enhence contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)

    # sharpness filter
    img = img.filter(ImageFilter.SHARPEN)

    return img

def img_to_text(image_path):
    image = Image.open(image_path)
    image = preprocess_img(image)

    text = pytesseract.image_to_string(image)

    return text
