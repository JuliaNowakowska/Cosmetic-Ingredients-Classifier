from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def preprocess_img(self):
        """Preprocessing the image to make it easier for conversion."""
        # Convert to grayscale
        img = self.image.convert('L')

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)

        # Apply sharpness filter
        img = img.filter(ImageFilter.SHARPEN)

        return img

    def img_to_text(self):
        """Convert the preprocessed image to text."""
        preprocessed_image = self.preprocess_img()
        text = pytesseract.image_to_string(preprocessed_image)
        return text


if __name__ == "__main__":
    image_path = '/path/to/image.png'
    processor = ImageProcessor(image_path)
    text = processor.img_to_text()
    print(text)
