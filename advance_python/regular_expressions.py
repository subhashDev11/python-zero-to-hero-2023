import re

pattern = r"hello"
text = "hello world"

match = re.search(pattern, text)
print(match.group()) # Output: "hello"


# Matching a string with wildcards:

pattern = r"he..o"
text = "hello world"

match = re.search(pattern, text)
print(match.group()) # Output: "hello"

# Matching a string with character classes:

pattern = r"[aeiou]"
text = "hello world"

match = re.search(pattern, text)
print(match.group()) # Output: "e"

# Matching a string with repetition:

pattern = r"he*llo"
text = "helo world"

match = re.search(pattern, text)
print(match.group()) # Output: "helo"

# Splitting a string with regular expressions:

text = "apple,banana,cherry"
pattern = r","

result = re.split(pattern, text)
print(result) # Output: ['apple', 'banana', 'cherry']
