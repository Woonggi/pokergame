class Player(object):
  def __init__(self):
    self.hand = []

  def printHand(self):
    print(self.hand[0], self.hand[1])