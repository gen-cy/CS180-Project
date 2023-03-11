import pygame, copy

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, size, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        # self.uncollected_image = pygame.image.load(img).convert_alpha()
        # self.collected_image = pygame.image.load(img).convert_alpha()
        self.right_img = pygame.transform.flip(self.image, True, False)
        self.left_img = pygame.image.load(img).convert_alpha()
        
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.collected = False
        self.gravity = 0.4
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
        
    def collect_item(self, pos):
        self.collected = True   
        # self.image = self.collected_image
        # self.rect = self.image.get_rect(topright = pos)
        self.gravity = 0
    
    def drop_item(self, pos):
        self.collected = False
        # self.image = self.uncollected_image
        # self.rect = self.image.get_rect(topleft = pos)
        self.gravity = 0.4
        
    def update(self, pos, direction):           #only called if player is holding the item
        if direction >= 0:
            self.image = self.right_img
            self.rect.topright = pos
        elif direction < 0:
            self.image = self.left_img
            self.rect.topleft = pos
        
            

        
class JanitorItem(Item):
    def __init__(self, pos, size, img):
        super().__init__(pos, size, img)
        
        
class BankerItem(Item):
    def __init__(self, pos, size, img):
        super().__init__(pos, size, img)
        
        