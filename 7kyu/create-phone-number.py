# def create_phone_number(n):
#     first_three = '(' + str(n[0]) + str(n[1]) + str(n[2]) + ') '
#     middle_three = str(n[3]) + str(n[4]) + str(n[5]) + '-'
#     last_four = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
#     return first_three + middle_three + last_four


def create_phone_number(n):
  first_three = ''.join(str(x) for x in n[0:3])
  middle_three = ''.join(str(x) for x in n[3:6])
  last_four = ''.join(str(x) for x in n[6:])
  return '({}) {}-{}'.format(first_three, middle_three, last_four)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

