import random

num = random.randint(1,100)
guess = ''
i = 0
while guess != num:  
  guess = input("guess the number :")
  if guess == 'exit':
    break
  else:
    guess = int(guess)
    if guess >= 1 and guess <= 100:
      i += 1
      if guess < num:
        print ("Too Low")
      elif guess > num:
        print ("Too High")
      elif guess == num:
        print ("Right")
    else:
      print ("Wrong input!!!")
print ("Number of guesses : " + str(i))
