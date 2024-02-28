import pygame
import poker
# for testing...
from player import Player

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()
running = True

deck = poker.Deck()
deck.shuffle()
print(deck)
print(len(deck))

p1 = Player()
p2 = Player()
p3 = Player()
dealer = poker.Dealer(deck)
print("***********************************")
dealer.distribute(p1)
dealer.distribute(p2)
dealer.distribute(p3)
p1.printHand()
p2.printHand()
p3.printHand()

print(deck)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

print('hello')