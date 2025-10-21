ifLearnAbout = input('Do you want to know how DCCE++ letters are determined?(yes/no): ')

if ifLearnAbout == 'yes':
  print('DCCE++ Numerical Digits In Order From Least To Greatest: 9, 7, 4, 0, 8, 5, 2, 1, 3, 6')
  print('A letter or word is determined by a digit divided by a digit (can be in a set)')
  print('The difference between the digits multiplied by the numerator is equal to the starting number. The numerator multiplied by the denominator is equal to the amount of times the starting number is repeated. This value divided by the denominator * 2, multiplied by the numerator, is the amount of times the starting number repeats after each unique digit. This value if it is one of the DCCE++ Numerical Digits is removed, the numerator and denominator are too unless they are the starting number. If we were figuring out 7/4, this would be described as 4 boxed 7. This string of numbers for 1 box determines a letter in a word. Spaces are logically placed.')
  print('A = 0 boxed 8; B = 7 boxed 4; C = 5 boxed 2; D = 9 boxed 7; E = 0 boxed 4; WIP')
