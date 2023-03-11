import pygame
from tiles import Tile
from player import Player
from banker import Banker

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.banker = pygame.sprite.GroupSingle()
        tile_size = 64
        for row_index, row in enumerate(layout):
            # print(row_index)
            # print(row)

            for col_index, cell in enumerate(row):
                #print(f'{row_index},{col_index}:{cell}')
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == "X":    
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)

                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

                if cell == "B":
                    banker_sprite = Banker((x,y))
                    self.banker.add(banker_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite  
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(player.rect): #if player collides with a tile
                if player.direction.x < 0: #moving left
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0: #moving right
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        is_colliding_with_tile = False

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(player.rect): #if player collides with a tile
                is_colliding_with_tile = True
                if player.direction.y > 0: #is on top of a rectangle
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_on_ground = True

                elif player.direction.y < 0: #player's  touching bottom of tile
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0



        if is_colliding_with_tile == False:
            player.is_on_ground = False  
        

    def banker_horizontal_movement_collision(self):
            banker = self.banker.sprite  
            banker.rect.x += banker.direction.x * banker.speed

            for sprite in self.tiles.sprites(): #looking through all sprites
                if sprite.rect.colliderect(banker.rect): #if player collides with a tile
                    if banker.direction.x < 0: #moving left
                        banker.rect.left = sprite.rect.right
                    elif banker.direction.x > 0: #moving right
                        banker.rect.right = sprite.rect.left

    def banker_vertical_movement_collision(self):
        banker = self.banker.sprite
        banker.apply_gravity()
        is_colliding_with_tile = False

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(banker.rect): #if player collides with a tile
                is_colliding_with_tile = True
                if banker.direction.y > 0: #moving left
                    banker.rect.bottom = sprite.rect.top
                    banker.direction.y = 0
                    banker.is_on_ground = True

                elif banker.direction.y < 0: #moving right
                    banker.rect.top = sprite.rect.bottom
                    banker.direction.y = 0
        if is_colliding_with_tile == False:
            banker.is_on_ground = False

    def run(self):
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)

        self.banker.update()
        self.banker.draw(self.display_surface)
        
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        self.banker_horizontal_movement_collision()
        self.banker_vertical_movement_collision()


