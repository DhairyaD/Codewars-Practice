# Complete the solution so that it reverses all of the words within the string passed in .

# Example:

# "The greatest victory is that which requires no battle" - -> "battle no requires which that is victory greatest The"


def reverse_words(s):
    temp, s = s.split()[::-1], ''
    for word in temp:
        s += word + ' '
    return s.rstrip()

print(reverse_words('hello world!'))