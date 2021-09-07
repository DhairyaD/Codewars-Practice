def no_space(x):
  s = ''
  for c in x:
    if c != ' ':
      s += c
  return s


def no_space_using_replace(x):
  return x.replace(' ', '')




print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
print(no_space_using_replace('8 j 8   mBliB8g  imjB8B8  jl  B'))
