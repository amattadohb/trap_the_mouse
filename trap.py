import pygame
from pygame.locals import *
from pygame.mouse import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Catch the Mouse')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Load sprites
    sprites = ()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # get a list of all sprites that are under the mouse cursor
                clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
                # do something with the clicked sprites...


        # wait for user to click on square
        # break tile that user clicked on
        # move mouse


        screen.blit(background, (0, 0))
        pygame.display.flip()



def load_png(name):
    fullname = os.path.join('icon', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

class Mouse(pygame.sprite.Sprite):

    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = init_pos
        self.image, self.rect = load_png('mouse.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update(self):
        pass

    def move_up(self):
        self.pos[1] = self.pos[1] - 1

    def move_down(self):
        self.pos[1] = self.pos[1] + 1

    def move_right(self):
        self.pos[0] = self.pos[0] + 1

    def move_left(self):
        self.pos[0] = self.pos[0] - 1


class Tile(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('tile.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()


if __name__ == '__main__': main()