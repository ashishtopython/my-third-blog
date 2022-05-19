import time, random
continued = 'no'
print("guess thy number")
guess = input("what do you think the number is between 1-10? ")
number = random.randint(1,10)
if guess.lower() not in ["1","2","3","4","5","6","7","8","9","10"]:
    print("What part of enter a NUMBER between 1-10 do you not understand?")
    quit()
while continued == 'no':
  continue1 = input("type 1 to continue: ")
  if continue1.lower() in ["1","1 to continue",]:
    continued == 'yes'
    if int(guess) == number:
      print("Lucky child")
      print("You just got lucky")
      print("go win the lottery")
      quit() 
    else:
      print("LOL, SO BAD.")
      print("GET GOOD")  
    break
again = input("Do you want to do this again? Say yes, y or no, n: ")
while again.lower() in ['yes', 'y']:
  print("guess thy number")
  guess = input("what do you think the number is between 1-10? ")
  number = random.randint(1,10)
  if guess.lower() not in ["1","2","3","4","5","6","7","8","9","10"]:
    print("What part of enter a NUMBER between 1-10 do you not understand?")
    quit()
  while continued == 'no':
    continue1 = input("type 1 to continue: ")
    if continue1.lower() in ["1","1 to continue",]:
      continued == 'yes'
      if int(guess) == number:
        print("Lucky child")
        print("You just got lucky")
        print("go win the lottery")
        break
      else:
        print("LOL, SO BAD.")
        print("GET GOOD")  
        break
  again = input("Do you want to do this again? Say yes, y or no, n: ")
  
    
