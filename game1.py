import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("falling circle")

x = 250
y = 150
width = 40
height = 50
velocity = 15
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

run = True
while run:
	 pygame.time.delay(100)

	 for event in pygame.event.get():
	 	if event.type == pygame.QUIT:
	 		run = False

	 keys = pygame.key.get_pressed()
	 
	 if keys[pygame.K_LEFT]:
	 	x -= velocity
	 if keys[pygame.K_RIGHT]:
	 	x += velocity
	 if keys[pygame.K_UP]:
	 	y -= velocity
	 if keys[pygame.K_DOWN]:
	 	y += velocity



     win.fill((black))

	 pygame.draw.circle(win, (blue), (x, y), 20, 3)
	 pygame.display.update()


pygame.quit() 
