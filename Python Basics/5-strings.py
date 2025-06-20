# working with strings

import re
first = "Hello"
second = "World"
print(first + " " + second)  # concatenation

test = "Hello World bla bla"
print(test[1:3])  # first character
print(test[1:])  # from first character to end
print(test[:5])  # from start to fifth character
print(test[-1])  # last character

print(f"I am {first} and I am {second}")

# split
words = test.split(" ")  # splits the string into a list of words
print(words)

# join
joined = " ".join(words)  # joins the list of words into a single string
print(joined)

# replace
replaced = test.replace("bla", "foo")  # replaces "bla" with "foo"
print(replaced)

# remove spaces
stripped = "  asd aasd dddd   ".strip()  # removes leading and trailing spaces
print(stripped)

# using RegExp
pattern = r"\b\w{3}\b"  # matches words with exactly 3 characters
# explanation of the pattern: # \b - word boundary, # \w - any word character (alphanumeric + underscore), {3} - exactly 3 occurrences
matches = re.findall(pattern, test)  # finds all matches in the string
print(matches)

# search
search_result = re.search(r"World", test)  # searches for "World" in the string
if search_result:
    print("Found:", search_result.group())  # prints the matched string
else:
    print("Not found")

# replace all digits with *
# replaces all digits with "*"
replaced_all = re.sub(r"\d", "*", "123123 123 asd asd asd 12 3123 asd asda ")
print(replaced_all)


def clean_text(text):
    """Function to clean text by removing extra spaces and punctuation."""
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Example usage of clean_text function
cleaned_text = clean_text("  Hello,   World!  This is a test.  ")
print("Cleaned text:", cleaned_text)
