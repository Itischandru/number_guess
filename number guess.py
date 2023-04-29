import random
number=input('Enter A Number : ')
if number.isdigit():
  number=int(number)
  if number<=0:
    print('enter number grater then 0 next time.')
    quit()
else:
  print('please enter a number next time.')
  quit()

number=random.randrange(0,number)
chance=0
while True:
  chance +=1
  guess=input('make a guess :')
  if guess.isdigit():
    guess=int(guess)
  else:
    print('type a number next time.')
    continue
  if guess==number:
    print('you got a right number :)')
    break
  else:
    print('you got wrong!')

print('you got the answer in',chance,'chance')
