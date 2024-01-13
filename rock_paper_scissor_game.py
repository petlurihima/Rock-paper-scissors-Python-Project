import random
user=input("Select 'r' for rock 'p' for paper 's' for scissors:")
computer=random.choice(['r','p','s'])
if (user=='r' and computer=='r') or (user=='p' and computer=='p') or (user=='s' and computer=='s'):
  print("Both are tied")
elif (user=='r' and computer=='s') or (user=='p' and computer=='r') or (user=='s' and computer=='p'):
  print("Congrats,you won")
else:
  print("Sorry,you lost")