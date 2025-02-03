def reverseStr(s):
  return ' '.join([x[::-1] for x in s.split(' ')])

string = input()
reverseStr(string)