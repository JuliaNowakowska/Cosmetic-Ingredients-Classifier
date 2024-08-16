from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import string

class Cosmetic():
    def __init__(self, path):
        self.ingredients_image = path
        self.ingredients = None

    def preprocess_image(self):
        """
        Enhancing the photo to make the conversion easier
        """
        try:
            img = Image.open(self.ingredients_image)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at path {self.ingredients_image} was not found.")

        # Convert to grayscale
        img = img.convert('L')

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(img)
        contrast_enhancement = 2
        img = enhancer.enhance(contrast_enhancement)

        # Apply sharpness filter
        img = img.filter(ImageFilter.SHARPEN)
        return img

    def get_ingredients(self):
        """Converting the preprocessed image to list of ingredients"""
        ingredients_image = self.preprocess_image()
        ingredients_text = pytesseract.image_to_string(ingredients_image)

        return ingredients_text

    def preprocess_ingredients(self):
        """
        Cleaning extracted text to get a list of ingredients.
        """
        text = self.get_ingredients()

        # Remove newlines and extra spaces
        text = text.replace('\n', ' ').replace('\r', ' ')
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Split into a list of ingredients (assuming ingredients are separated by commas)
        ingredient_list = [ingredient.strip() for ingredient in text.split(',')]
        # Join ingredients with a single space and save to self.processed_ingredients
        self.ingredients = ' '.join(ingredient_list)

        return

if __name__ == "__main__":
    image_path = '/path/to/image.png'
    cosmetic = Cosmetic(image_path)
    cosmetic.preprocess_ingredients()
    print(cosmetic.ingredients)