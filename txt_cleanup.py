import string


class Cosmetic:
    def __init__(self, ingredients):
        self.raw_ingredients = ingredients
        self.processed_ingredients = None  # Initialize the attribute

    def preprocess_ingredients(self):
        # Convert to lowercase
        text = self.raw_ingredients.lower()

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Split into a list of ingredients (assuming ingredients are separated by commas)
        ingredient_list = [ingredient.strip() for ingredient in text.split(',')]

        # Join ingredients with a single space and save to self.processed_ingredients
        self.processed_ingredients = ' '.join(ingredient_list)

        return self.processed_ingredients
