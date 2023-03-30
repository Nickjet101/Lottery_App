import random




def Lucky_Winner():
      while 1:
             Username = input("Enter your Name, ")
             Users_Number = int(input("Enter your Lottery Number 0 to 50, "))
             Numbers = random.randint(0, 50)
             if Numbers == 30:
                    print("congratulations", Username, "You won")
             else:
                    print("Sorry!", Username, "you lost, please try again.")



Lucky_Winner()