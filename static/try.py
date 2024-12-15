import pygame

pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load(r"F:\Stageone\F-Project-main\F-Project-main\Dataset\SER self Audio.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
finally:
    pygame.mixer.quit()
    pygame.quit()