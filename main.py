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
#print(len(deck))

players = [Player(), Player(), Player()]
dealer = poker.Dealer(deck)
#dealer.distribute(players[0])
#dealer.distribute(players[1])
#dealer.distribute(players[2])
print("*********HANDS*****************")
dealer.distribute(players)
players[0].printHand()
players[1].printHand()
players[2].printHand()

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