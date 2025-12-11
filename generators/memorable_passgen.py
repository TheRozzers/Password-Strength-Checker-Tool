import random

# Similar to password generators that companies such as Mozilla (in Firefox) use for password segmentation.
DELIMITERS = [
	'-',
	'~',
	'!',
	',',
	'$'
]

# Map of all numerical (visual) equivalents to alphabetical characters.
LEET_MAP = {
	'a': '4',
	'e': '3',
	'i': '1',
	'o': '0',
	's': '5',
	't': '7'
}

# Plan to implement the option to select different settings (such as if the password is numericized or not).
# Formats and structures the entire password.
def FormatPassword(phrases, delimiters):
	result = ""
	for iteration in range(0, len(phrases)):
		current_phrase = NumericizePhrase(phrases[iteration], LEET_MAP)
		result = result + current_phrase

		if not iteration == len(phrases) - 1:
			delimiter = random.choice(delimiters)
			result = result + delimiter
	return result

# Numericize letters of a phrase to obfuscate and add entropy to the final password.
def NumericizePhrase(phrase, leet):
	result = ""
	for character in list(phrase):
		if character.lower() not in leet:
			result = result + character
			continue
		result = result + leet[character.lower()]
	return result

# User-prompted, memorable words.
memorable_words = [
	input("Please enter your first memorable word:\n"),
	input("Please enter your second memorable word:\n"),
	input("Please enter your last memorable word:\n")
]

# Prints the final formatted, memorable password.
formatted_password = FormatPassword(memorable_words, DELIMITERS)
print(formatted_password)