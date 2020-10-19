import random
while True:
  while True:
    x=input("Guess the number from 1-10!:")
    try:
      int(x)
      if int(x)<=10 and int(x)!=0:
        break
      else:
        print("Invalid input!")
    except ValueError:
      print("Invalid input!")
  i=random.choice([1,2,3,4,5,6,7,8,9,10])
  print("You guessed:",x)
  print("The number was:",i)
  if int(x)==int(i):
    print("You won! Yay!")
  else:
    print("You lost!")
  while True:
    y=input("Play again? (y/n)")
    if y=="n":
      playagain=0
      print("Thanks for playing!")
      break
    else:
      if y=="y":
        playagain=1
        print("Let's play one more time!")
        break
      else:
        print("Invalid input!")
  if playagain==0:
    break
