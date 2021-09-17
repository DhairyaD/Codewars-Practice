# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics") == true
# is_isogram("aba") == false
# is_isogram("moOse") == false  # -- ignore letter case


def is_isogram(string):
  d = {}

  for letter in string:
    letter = letter.lower()
    d[letter] = d.get(letter, 0) + 1
  
  for value in d.values():
    if value > 1:
      return False
  return True


# Shorter version

# def is_isogram(string):
#     return len(string) == len(set(string.lower()))



print(is_isogram('moOse'))
print(is_isogram(''))

