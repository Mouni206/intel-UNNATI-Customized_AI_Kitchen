import random

class Kitchen:
    def __init__(self):
        self.ingredients = {
            'tomato': 5,
            'onion': 3,
            'garlic': 2,
            'chicken': 1,
            'pasta': 1,
            'salt': 10,
            'pepper': 5
        }
    
    def check_ingredients(self, dish):
        recipes = {
            'chicken_pasta': {'chicken': 1, 'pasta': 1, 'tomato': 2, 'onion': 1, 'garlic': 1, 'salt': 1, 'pepper': 1},
            'tomato_soup': {'tomato': 3, 'onion': 1, 'garlic': 1, 'salt': 1, 'pepper': 1}
        }
        if dish in recipes:
            for ingredient, amount in recipes[dish].items():
                if self.ingredients.get(ingredient, 0) < amount:
                    return False, f"Not enough {ingredient}"
            return True, "All ingredients are available"
        else:
            return False, "Recipe not found"
    
    def prepare_dish(self, dish):
        check, message = self.check_ingredients(dish)
        if check:
            recipes = {
                'chicken_pasta': {'chicken': 1, 'pasta': 1, 'tomato': 2, 'onion': 1, 'garlic': 1, 'salt': 1, 'pepper': 1},
                'tomato_soup': {'tomato': 3, 'onion': 1, 'garlic': 1, 'salt': 1, 'pepper': 1}
            }
            for ingredient, amount in recipes[dish].items():
                self.ingredients[ingredient] -= amount
            return "preparing...",f"{dish.replace('_', ' ').title()} is ready!"
        else:
            return message

    def add_ingredients(self, ingredient, amount):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += amount
        else:
            self.ingredients[ingredient] = amount
        return f"Added {amount} pieces of {ingredient} to the kitchen."

    def list_ingredients(self):
        return "Current ingredients:\n" + "\n".join([f"{ingredient}: {amount}" for ingredient, amount in self.ingredients.items()])

class ChatBot:
    def __init__(self):
        self.kitchen = Kitchen()
        self.greetings = ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How can I help?"]
        self.farewells = ["Goodbye!", "See you later!", "Have a great day!"]
    
    def greet(self):
        return random.choice(self.greetings)
    
    def respond(self, user_input):
        user_input = user_input.lower()
        if "prepare" in user_input:
            dish = user_input.replace("prepare ", "").replace(" ", "_")
            return self.kitchen.prepare_dish(dish)
        elif "check" in user_input:
            dish = user_input.replace("check ", "").replace(" ", "_")
            check, message = self.kitchen.check_ingredients(dish)
            return message
        elif "menu" in user_input:
            return "Available dishes: Chicken Pasta, Tomato Soup"
        elif "add" in user_input:
            parts = user_input.split()
            ingredient = parts[1]
            amount = int(parts[2])
            return self.kitchen.add_ingredients(ingredient, amount)
        elif "list" in user_input:
            return self.kitchen.list_ingredients()
        elif "exit" in user_input:
            return random.choice(self.farewells)
        else:
            return "I'm sorry, I don't understand that command."

def main():
    bot = ChatBot()
    print(bot.greet())
    
    while True:
        user_input = input("You: ")
        response = bot.respond(user_input)
        print(f"Bot: {response}")
        if user_input.lower() == "exit":
            break

if __name__ == "__main__":
    main()
