import requests
import tkinter as tk
from tkinter import ttk

notAllowed = [
  "Garlic",
  "Onion",
  "Onions",
  "Artichoke",
  "Asparagus",
  "Baked beans",
  "Beetroot, fresh",
  "Black eyed peas",
  "Broad beans",
  "Butter beans",
  "Cassava",
  "Cauliflower",
  "Celery - greater than 5cm of stalk",
  "Choko",
  "Falafel",
  "Haricot beans",
  "Kidney beans",
  "Kelp / Kombu",
  "Lima beans",
  "Leek bulb",
  "Mange Tout",
  "Mixed vegetables",
  "Mung beans",
  "Mushrooms",
  "Peas, sugar snap",
  "Pickled vegetables",
  "Red kidney beans - over 85g",
  "Savoy Cabbage - over 1/2 cup",
  "Soy beans / soya beans",
  "Split peas",
  "Scallions / spring onions (bulb / white part)",
  "Shallots",
  "Taro",
  "Apples including pink lady and granny smith",
  "Apricots",
  "Avocado",
  "Bananas, ripe",
  "Blackberries",
  "Blackcurrants",
  "Boysenberry",
  "Cherries",
  "Currants",
  "Custard apple",
  "Feijoa",
  "Figs",
  "Goji berries",
  "Grapefruit - over 80g",
  "Guava, unripe",
  "Juniper Berry, dried",
  "Lychee",
  "Mango",
  "Nectarines - over 1/2 a nectarine",
  "Paw paw, dried",
  "Peaches",
  "Pears",
  "Persimmon",
  "Pineapple, dried",
  "Plums",
  "Pomegranate",
  "Prunes",
  "Raisins - over 1 tbsp / 13g",
  "Sea buckthorns",
  "Sultanas",
  "Tamarillo",
  "Tinned fruit in apple / pear juice",
  "Watermelon",
  "Chorizo if garlic added",
  "Sausages",
  "Wheat containing products such as (be sure to check labels):",
  "Biscuits / cookies including chocolate chip cookies",
  "Bread, wheat - over 1 slice",
  "Breadcrumbs",
  "Cakes",
  "Cereal bar, wheat based",
  "Croissants",
  "Crumpets",
  "Egg noodles",
  "Muffins",
  "Pasta, wheat over 1/2 cup cooked",
  "Udon noodles",
  "Wheat bran",
  "Wheat cereals",
  "Wheat flour",
  "Wheat germ",
  "Wheat noodles",
  "Wheat rolls",
  "Almond meal",
  "Amaranth flour",
  "Barley including flour",
  "Bran cereals",
  "Bread:",
  "Granary bread",
  "Multigrain bread",
  "Naan",
  "Oatmeal bread",
  "Pumpernickel bread",
  "Roti",
  "Sourdough with kamut",
  "Cashews",
  "Chestnut flour",
  "Cous cous",
  "Einkorn flour",
  "Freekeh",
  "Gnocchi",
  "Granola bar",
  "Muesli cereal",
  "Muesli bar",
  "Pistachios",
  "Rye",
  "Rye crispbread",
  "Semolina",
  "Spelt flour",
  "Agave",
  "Caviar dip",
  "Fructose",
  "Fruit bar",
  "Gravy, if it contains onion",
  "High fructose corn syrup (HFCS)",
  "Hummus / houmous",
  "Honey",
  "Jam, mixed berries",
  "Jam, strawberry, if contains HFCS",
  "Molasses",
  "Pesto sauce",
  "Quince paste",
  "Relish / vegetable pickle",
  "Stock cubes",
  "Sugar free sweets containing polyols - usually ending in -ol or isomalt",
  "Sweeteners and corresponding E number:",
  "Inulin",
  "Isomalt (E953 / 953)",
  "Lactitol (E966 / 966)",
  "Maltitol (E965 / 965)",
  "Mannitol (E241 / 421)",
  "Sorbitol (E420 / 420)",
  "Xylitol (E967 / 967)",
  "Tzatziki dip",
  "Wasabi",
  "FOS - fructooligosaccharides",
  "Inulin",
  "Oligofructose",
  "Beer - if drinking more than one bottle",
  "Cordial, apple and raspberry with 50-100% real juice",
  "Cordial, orange with 25-50% real juice",
  "Fruit and herbal teas with apple added",
  "Fruit juices in large quantities",
  "Fruit juices made of apple, pear, mango",
  "Kombucha",
  "Malted chocolate flavored drink",
  "Meal replacement drinks containing milk based products e.g. Ensure, Slim Fast",
  "Orange juice in quantities over 100ml",
  "Quinoa milk",
  "Rum",
  "Sodas containing High Fructose Corn Syrup (HFCS)",
  "Soy milk made with soy beans - commonly found in USA",
  "Sports drinks",
  "Tea:",
  "Black tea with added soy milk",
  "Chai tea, strong",
  "Dandelion tea, strong",
  "Fennel tea",
  "Chamomile tea",
  "Herbal tea, strong",
  "Oolong tea",
  "Wine - if drinking more than one glass",
  "Whey protein, concentrate unless lactose free",
  "Whey protein, hydrolyzed unless lactose free",
  "Buttermilk",
  "Cheese, ricotta",
  "Cream",
  "Custard",
  "Gelato",
  "Ice cream",
  "Kefir",
  "Milk",
  "Cow milk",
  "Goat milk",
  "Evaporated milk",
  "Sheep's milk",
  "Sour cream - over 2tbsp",
  "Yoghurt",
  "Carob powder / carob flour"
]

ingredients_list = ["strIngredient1", "strIngredient2", "strIngredient3", "strIngredient4", "strIngredient5",
                    "strIngredient6", "strIngredient7", "strIngredient8", "strIngredient9", "strIngredient10",
                    "strIngredient11", "strIngredient12", "strIngredient13", "strIngredient14", "strIngredient15",
                    "strIngredient16", "strIngredient17", "strIngredient18", "strIngredient19", "strIngredient20"]


def extractIngredients(response, ingredients_list, notAllowed):
    allowed_ingredients = []
    for ingredient_key in ingredients_list:
        ingredient_value = response['meals'][0][ingredient_key]
        if ingredient_value not in notAllowed:
            allowed_ingredients.append(ingredient_value)
    return ', '.join(allowed_ingredients)


def fetch_recipe():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php").json()
    if extractIngredients(response=response, ingredients_list=ingredients_list, notAllowed=notAllowed):
        # Populate the GUI fields with the recipe information
        name_var.set(response['meals'][0]['strMeal'])
        ingredients_var.set(extractIngredients(response=response, ingredients_list=ingredients_list, notAllowed=notAllowed))
        preparation_text.config(state="normal")
        preparation_text.delete("1.0", tk.END)
        preparation_text.insert(tk.END, response['meals'][0]['strInstructions'])
        preparation_text.config(state="disabled")
        youtube_link_var.set(response['meals'][0]['strYoutube'])
        result_label.config(text="Recipe Found!")
    else:
        result_label.config(text="Not this one, sorry!")


# GUI setup
root = tk.Tk()
root.title("Recipe Finder")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.grid(row=0, column=0, columnspan=2, pady=10)

find_button = tk.Button(frame, text="Find Me a Recipe", command=fetch_recipe)
find_button.grid(row=1, column=0, columnspan=2, pady=10)

# Variables to store recipe information
name_var = tk.StringVar()
ingredients_var = tk.StringVar()
youtube_link_var = tk.StringVar()

# Labels to display recipe information
name_label = tk.Label(frame, text="Name of Meal:")
name_label.grid(row=2, column=0, pady=5, sticky="w")

ingredients_label = tk.Label(frame, text="Ingredients:")
ingredients_label.grid(row=3, column=0, pady=5, sticky="w")

preparation_label = tk.Label(frame, text="Preparation:")
preparation_label.grid(row=4, column=0, pady=5, sticky="w")

youtube_link_label = tk.Label(frame, text="YouTube Link:")
youtube_link_label.grid(row=5, column=0, pady=5, sticky="w")

# Entry widgets to display recipe information
name_entry = tk.Entry(frame, textvariable=name_var, state="readonly", width=50)
name_entry.grid(row=2, column=1, pady=5, sticky="w")

ingredients_entry = tk.Entry(frame, textvariable=ingredients_var, state="readonly", width=50)
ingredients_entry.grid(row=3, column=1, pady=5, sticky="w")

preparation_text = tk.Text(frame, height=5, width=50, wrap="word")
preparation_text.insert("1.0", "Preparation information will be displayed here.")
preparation_text.config(state="disabled")
preparation_text.grid(row=4, column=1, pady=5, sticky="w")

youtube_link_entry = tk.Entry(frame, textvariable=youtube_link_var, state="readonly", width=50)
youtube_link_entry.grid(row=5, column=1, pady=5, sticky="w")

root.mainloop()