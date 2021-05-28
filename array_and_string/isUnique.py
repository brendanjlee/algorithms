def isUnique(string):
  _dict = []
  for letter in string:
    if letter in _dict:
      return False
    _dict.append(letter)
  return True


# test
words  = ['generalized', 'something', 'abcdefg', 'parameter']

for word in words:
  isu = isUnique(word)
  if isu:
    print('--{}-- has no repating letters'.format(word))
  else:
    print('--{}-- has repeating letters'.format(word))
