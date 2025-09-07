import pygame

# ---init---
pygame.init()

# variable
isRun = True

# membuat display surfce object
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 5
# ---init---

while isRun:
    # ---user input, database input---
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            print('break')
            isRun = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0 :
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - panjang :
        x += speed
    if keys[pygame.K_UP] and y > 0 :
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - lebar :
        y += speed
    # ---user input, database input---

    # ---update asset---
    window.fill((40,44,52))
    pygame.draw.rect(
        window,
        (255,0,0),
        (x,y,lebar,panjang)
    )
    # ---update asset---

    # ---render ke display---
    pygame.display.update()
    
    # delay otomatis supaya fps nya 120
    clock.tick(120)
    # ---render ke display---

pygame.quit()