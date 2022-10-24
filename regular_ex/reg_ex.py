import re

pattern = "pattern to be searched"
content = "content pattern to be searched to check pattern to be searched"

# .match - checks if pattern is present at start
print(re.match("content", content))

# .search - checks if pattern is anywhere in the content (first occurrence)
print(re.search("pattern to be searched", content))

# .findall - checks for the pattern is anywhere in the content (all occurrence)
print(re.findall("pattern", content))

# .sub - checks for the pattern in content and replace with second argument (all occurrence)
print(re.sub("pattern", "replace_string", content))

# the dot '.' meta character can be used as a wild card (eg: c.t is any word with c then any letter then t)
print(re.findall("b.", content))

# character class - [A-Z][a-z][0-9] - used to represent a specific type of possible characters
print(re.match("[a-z]", content))
