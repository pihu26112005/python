import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']

#syntax : re.sub( pattern , new word , text)
new_text = re.sub(pattern, "dog", text)

print(new_text)
# Output: "The dog is in the dog."