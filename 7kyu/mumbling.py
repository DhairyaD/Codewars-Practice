# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    count = 1
    result = ''
    for letter in s:
      upper = letter.upper()
      lower = letter.lower() * (count - 1)
      result += letter.upper() + letter.lower() * (count - 1) + '-'
      count += 1
    return result[:-1]


print(accum('abcd'))
print(accum('ZpglnRxqenU'))
