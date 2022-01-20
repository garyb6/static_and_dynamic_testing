### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# line 21 invalid syntax for defining card.value, should be == 
# line 23, colon missing after else

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card   
  else:
    return card2
# line 28 - should be def instead of dif, no comma between card1 and card2 parameters. 
# line 29 and 31 - indentation errors, shouldn't be in line with the function.  
# lin30 - card is not defined. 


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total

# line39: total not defined and not returned on line 42. Should be included in return statement, not added on. 
