import pygame
import random

class Fishfood(pygame.sprite.Sprite):
    
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
    
    def reset_pos(self):
        self.rect.y = random.randrange(-300,-20)
        self.rect.x = random.randrange(0,screen_width)
    
    def update(self):
        self.rect.y += 1
        if self.rect.y > 410:
            self.reset_pos()

class Player(Fishfood):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

pygame.init()
screen_width = 700
screen_height = 400

screen = pygame.display.set_mode((screen_width,screen_height))
food_list = pygame.sprite.Group()
AllFoodList = pygame.sprite.Group()

for i in range(200):
    food = Fishfood("brown",20,15)
    food.rect.x = random.randrange(screen_width)
    food.rect.y = random.randrange(screen_height)
    food_list.add(food)
    AllFoodList.add(food)

player = Player("orange",30,10)
AllFoodList.add(player)
done = False

clock = pygame.time.Clock()
score = 0

while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
    screen.fill("light blue")
    AllFoodList.update()
    foodhitlist=pygame.sprite.spritecollide(player,food_list,False)
    for i in foodhitlist:
        score += 1
        print(score)
        i.reset_pos()
        player.rect.x += 10
        player.rect.y += 10
    AllFoodList.draw(screen)
    clock.tick(20)
    pygame.display.flip()

pygame.QUIT