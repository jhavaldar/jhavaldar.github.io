#!/usr/local/bin/python
def max(a, b):
  if a > b:
    return a
  else:
    return b

# Calculate the value of the card
def value(card):
  dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
  if card[0] in dict:
    return dict[card[0]]
  else:
    return int(card[0])

def check_flush(cards):
  suit = cards[0][1]
  for card in cards:
    if card[1] != suit:
      return False
  return True

def check_straight(cards):
  temp = cards[0]
  for card in cards[1:len(cards)]:
    if value(card) == value(temp) + 1:
      temp = card
    else:
      return False
  return True

hand_names = {
  0: "High Card",
  1: "One Pair",
  2: "Two Pair",
  3: "Three of a Kind",
  4: "Straight",
  5: "Flush",
  6: "Full House",
  7: "Four of a Kind",
  8: "Straight Flush",
  9: "Royal Flush",
}

def get_pairs(hand):
  dict = {}
  arr = [0]*15
  # Separate them into buckets
  for card in hand:
    arr[value(card)] += 1
  for i in range(0, 15):
    if arr[i] > 0:
      dict[i] = arr[i]
  return dict

def num_pairs(hand):
  arr = [0]*15
  # Separate them into buckets
  for card in hand:
    arr[value(card)] += 1
  arr = sorted(filter(lambda x: x > 0, arr))
  return arr

def rank(hand):
  current_max = 0
  cards = sorted(hand, key= lambda x: value(x))
  pairs = num_pairs(cards)

  # Check for a full house or a four of a kind
  if pairs[-1] == 4:
    current_max = max(current_max, 7)  #Four of a kind
  elif pairs[-1] == 3:
    if pairs[-2] == 2:  #Full House
      current_max = max(6, current_max)
    else: #Three of a kind
      current_max = max(3, current_max)
  elif pairs[-1] == 2:
    if pairs[-2] == 2:  #Two Pairs
      current_max = max(2, current_max)
    else:
      current_max = max(1, current_max)
  # Check if there's a flush, i.e. all cards of the same suit
  if check_flush(cards):
    #Check if its a straight flush
    if check_straight(cards):
      # You have straight; do you have royal?
      if cards[0][0]=="T":
        return 9    # Royal Flush
      else:
        return 8    # Straight Flush
    else:
      current_max = max(5, current_max)
      return current_max
  else: # No flush
    # In this case, if you already have four or full house, return
    if current_max > 5:
      return current_max
    # Check if straight
    if check_straight(cards):
      return 4
    else:
      return current_max
  return current_max

def winner(hand1, hand2):
  rank1 = rank(hand1)
  rank2 = rank(hand2)
  if rank1 > rank2:
    return 1
  elif rank2 > rank1:
    return 2
  else:
    if rank1==7:  #Four of a kind
      # Get the four
      pairs1 = get_pairs(hand1)
      val1 = 0
      pairs2 = get_pairs(hand2)
      va12 = 0
      for elt in pairs1:
        if pairs1[elt] == 4:
          val1 = elt
      for elt in pairs2:
        if pairs2[elt] == 4:
          val2 = elt
      # Compare the values of the fours
      if val1 > val2:
        return 1
      elif val2 > val1:
        return 2
      else:
        return check_higher(hand1, hand2)
    elif rank1==6 or rank1==3: #Full House
    # Get the threes
      pairs1 = get_pairs(hand1)
      val1 = 0
      pairs2 = get_pairs(hand2)
      va12 = 0
      for elt in pairs1:
        if pairs1[elt] == 3:
          val1 = elt
      for elt in pairs2:
        if pairs2[elt] == 3:
          val2 = elt
      # Compare the values of the three
      if val1 > val2:
        return 1
      elif val2 > val1:
        return 2
      else:
        return check_higher(hand1, hand2)
    elif rank1==5 or rank1==4 or rank1==8: #Flush
      return check_higher(hand1, hand2)
    elif rank1==2: #Two Pairs
      #Get the pairs
      pairs1 = get_pairs(hand1)
      val1 = []
      pairs2 = get_pairs(hand2)
      va12 = []
      for elt in pairs1:
        if pairs1[elt] == 3:
          val1.append(elt)
      for elt in pairs2:
        if pairs2[elt] == 3:
          val2.append(elt)
      val1 = sorted(val1, key = lambda x: x)
      val2 = sorted(val2, key = lambda x: x)
      if val1[1] > val2[1]:
        return 1
      elif val1[1] < val2[1]:
        return 2
      else:
        if val1[0] > val2[0]:
          return 1
        else:
          return 2
    elif rank1==1:
      # Get the pair
      pairs1 = get_pairs(hand1)
      val1 = 0
      pairs2 = get_pairs(hand2)
      va12 = 0
      for elt in pairs1:
        if pairs1[elt] == 2:
          val1 = elt
      for elt in pairs2:
        if pairs2[elt] == 2:
          val2 = elt
      # Compare the values of the fours
      if val1 > val2:
        return 1
      elif val2 > val1:
        return 2
      else:
        return check_higher(hand1, hand2)
    else:
      return check_higher(hand1, hand2)

def check_higher(hand1, hand2):
  index = len(hand1) - 1
  cards1 = sorted(hand1, key= lambda x: value(x))
  cards2 = sorted(hand2, key= lambda x: value(x))
  while value(cards1[index]) == value(cards2[index]):
    index -= 1
  if value(cards1[index]) > value(cards2[index]):
    return 1
  else:
    return 2


with open("p054_poker.txt") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)