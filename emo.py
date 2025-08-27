import json
with open('emojis.json', 'r', encoding='utf-8') as file:
    # Load the JSON data
    data = json.load(file)

# Function to search for emoji by name
def find_emoji(emoji_name):
    for obj in data:
        if emoji_name in obj["emojis"]:
            emoji_class = obj["class"]
            emoji_character = obj["emojis"][emoji_name]
            return emoji_class, emoji_character
    return None, None

# Get input from the user
emoji_name = input("Enter the name of the emoji: ")

# Find the emoji and print its class and character
emoji_class, emoji_character = find_emoji(emoji_name)
print(type(emoji_character))
if emoji_class is not None:
    print(f"Class: {emoji_class}")
    print(f"Emoji: {emoji_character}")
else:
    print("Emoji not found.")
