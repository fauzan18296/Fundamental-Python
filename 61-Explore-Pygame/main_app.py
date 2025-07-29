import pygame

# Init (Game engine nya dijalankan)
pygame.init()
# Variable running game (menjalankan game)
is_run = True

# Membuat display surface object
window_lebar = 600
window_panjang = 500
window = pygame.display.set_mode((window_lebar, window_panjang))

# Object game
# coordinate/posisi
x = 250
y = 250
# ukuran
panjang = 50
lebar = 50
# kecepatan gerak
speed = 10

while is_run:
  pygame.time.delay(10)
  # User input, database input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Keluar dari game!")
      is_run = False
  # Ambil semua keyboard press
  keys = pygame.key.get_pressed()
  
  # Ambil ke kiri
  if keys[pygame.K_LEFT] and x > 0:
    x -= speed
  
  # Ambil ke kanan
  if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
    x += speed
  
  # Ambil ke bawah
  if keys[pygame.K_DOWN] and y < window_panjang - panjang:
    y += speed
  
  # Ambil ke atas
  if keys[pygame.K_UP] and y > 0:
    y -= speed
  
  # Game dynamic
  
  # Update asset
  window.fill((255, 255, 255))
  pygame.draw.rect(window, (255, 120, 0), (x, y, panjang, lebar))
  # Render ke display
  pygame.display.update()

pygame.quit()