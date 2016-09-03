import highlow
import random

# print highlow.apple(highlow.apple(guess)) 

def start_game():
  guess_cntr=0
  print "starting new game"
  x=int(random.random()*100+1)
  rnd_num=x
  while True:
    print "take a guess:"
    guess = int(raw_input())
    guess_cntr=guess_cntr+1
    rnd_num=x
    if guess>rnd_num:
      print "too high"
    elif guess<rnd_num:
      print "too low"
    else:
      print "congratulations"
      print "It took you %d guesses" % (guess_cntr) 
      break

  start_game()

def main():
  start_game()

main()	