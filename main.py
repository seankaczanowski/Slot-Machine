'''
Classic Slot Machine 1.0

Developed by Sean Kaczanowski
Feb 2019
No copyright

Simple 3 Reel Slot Machine w the following features
- 3 reels
- 4 symbols
- Different Payout Scheme
- Basic Graphic Interface
- Simple Betting Feature
'''

# Title Screen
print('')
print(' +-------------------------+ ')
print(' +-------------------------+ ')
print(' | +---------------------+ | ')
print(' | |   Slot Machine 1.0  | | ')
print(' | +---------------------+ | ')
print(' |  _____   _____   _____  | ')
print(' | |     | |     | |     | | ')
print(' | | >-B | | >-B | | >-B | | ')
print(' | |_____| |_____| |_____| | ')
print(' |                         | ')
print(' | +---------------------+ | ')
print(' | |       JACKPOT!      | | ')
print(' | +---------------------+ | ')
print(' |                         | ')
print(' +-------------------------+ ')
print(' +-------------------------+ ')
print('')
print(' Prize Payout')
print(' + 3 x \'-\' = Bet x 10')
print(' + 3 x \'BAR\' = Bet x 50')
print(' + 3 \'7\' = Bet x 500')
print(' + 3 \'>-B\' = Bet x 1000')
print('')
print(' How to Play')
print(' + Press \'1\', \'2\' or \'5\' to Pull')
print(' + Press \'x\' to Exit')
print('')

import random

# Slot Assign / Random Num Generator / Value
def slot_assign():
  slot = random.randint(1, 10)
  if slot == 1:
    slot = '---'
  elif slot == 2:
    slot = '---'
  elif slot == 3:
    slot = "---"
  elif slot == 4:
    slot = "---"
  elif slot == 5:
    slot = "BAR"
  elif slot == 6:
    slot = "BAR"
  elif slot == 7:
    slot = "BAR"
  elif slot == 8:
    slot = " 7 "
  elif slot == 9:
    slot = " 7 "
  elif slot == 10:
    slot = ">-B"
  return slot

money = 100

#Game Loop
i = 0
while i == 0:

  print('Money: $' + str(money))
  
  # Correct Bet Loop
  j = 0
  while j == 0:
    bet = input('Bet $1/$2/$5: ')
    if bet == '1' or bet == '2' or bet == '5':
      j = 1
    else:
      print('Try Again! Press \'1\', \'2\' or \'5\'')

  bet = int(bet)
  money += - bet
  
  print('')
    
  slot1 = slot_assign()
  slot2 = slot_assign()
  slot3 = slot_assign()

  # Payout Outcomes
  if slot1 == '---' and slot2 == '---' and slot3 == '---':
    payout = 10
    prize = "WINNER!!!!!"
  elif slot1 == 'BAR' and slot2 == 'BAR' and slot3 == 'BAR':
    payout = 50
    prize = "WINNER!!!!!"
  elif slot1 == ' 7 ' and slot2 == ' 7 ' and slot3 == ' 7 ':
    payout = 500
    prize = "WINNER!!!!!"
  elif slot1 == '>-B' and slot2 == '>-B' and slot3 == '>-B':
    payout = 1000
    prize = "JACKPOT!!!!"
  else:
    payout = 0
    prize = "PULL AGAIN!"

  winnings = bet * payout
  money += + winnings

  # Slot Print
  print('')
  print(' +-------------------------+ ')
  print(' +-------------------------+ ')
  print(' | +---------------------+ | ')
  print(' | |   Slot Machine 1.0  | | ')
  print(' | +---------------------+ | ')
  print(' |  _____   _____   _____  | ')
  print(' | |     | |     | |     | | ')
  print(' | | ' + str(slot1) + ' | | ' + str(slot2) + ' | | ' + str(slot3) + ' | |')
  print(' | |_____| |_____| |_____| | ')
  print(' |                         |')
  print(' | +---------------------+ |')
  print(' | |    ' + str(prize) + '      | |')
  print(' | +---------------------+ |')
  print(' |                         |')
  print(' +-------------------------+')
  print(' +-------------------------+')
  print('')
  print('Winnings: $' + str(winnings))
  print('')

  if money <= 0:
    print('BANKRUPT! GAME OVER!')
    exit()

