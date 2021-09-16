# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") = > true
# XO("xooxx") = > false
# XO("ooxXm") = > true
# XO("zpzpzpp") = > true // when no 'x' and 'o' is present should return true
# XO("zzoo") = > false

def xo(s):
  if 'x' not in s and 'o' not in s:
    return True

  x_count, o_count = 0, 0

  for letter in s:
    if letter.lower() == 'x':
      x_count += 1
    if letter.lower() == 'o':
      o_count += 1
  
  return x_count == o_count


print(xo('xxxoo'))
