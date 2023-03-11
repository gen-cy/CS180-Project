import pygame
from tiles import Tile
from player import Player
from banker import Banker
from obstacle import PointObstacle
from obstacle import InteractObstacle
from obstacle import InteractBox
from enemy import Roomba
from item import JanitorItem, BankerItem

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.banker = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.levers = pygame.sprite.Group()
        tile_size = 46
        for row_index, row in enumerate(layout):
            # print(row_index)
            # print(row)

            cols_skipped = 0
            for col_index, cell in enumerate(row):
                #print(f'{row_index},{col_index}:{cell}')
                x = (col_index - cols_skipped) * tile_size
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
                    
                if cell == "E":
                    roomba_sprite = Roomba((x, y), 300, self.player)
                    self.enemies.add(roomba_sprite)
                
                if cell == "J":
                    janitor_item_sprite = JanitorItem((x, y), (tile_size * 2, tile_size), "./imgs/key.png")
                    self.items.add(janitor_item_sprite)
                
                if cell == "B":
                    banker_item_sprite = BankerItem((x, y), (tile_size * 2, tile_size), "./imgs/key.png")
                    self.items.add(banker_item_sprite)
                    
                if cell == "C":
                    point = PointObstacle((x,y), tile_size)
                    self.points.add(point)
                
                if cell == "O":
                    obstacle = InteractObstacle((x, y + tile_size), tile_size, tile_size * 5)
                    if col_index + 1 < len(row) and layout[row_index][col_index + 1].isnumeric():
                        col_index += 1
                        cols_skipped += 1
                        uniqueID = layout[row_index][col_index]
                        obstacle.obstacleID = int(uniqueID)
                    self.obstacles.add(obstacle)   
                           
                if cell == "L":
                    lever = InteractBox((x,y))
                    if col_index + 1 < len(row) and layout[row_index][col_index + 1].isnumeric():
                        col_index += 1
                        cols_skipped += 1
                        uniqueID = layout[row_index][col_index]
                        lever.leverID = int(uniqueID)
                    self.levers.add(lever)

    def horizontal_movement_collision(self):
        player = self.player.sprite  
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites(): #looking through all sprites
            if sprite.rect.colliderect(player.rect): #if player collides with a tile
                if player.direction.x < 0: #moving left
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0: #moving right
                    player.rect.right = sprite.rect.left
                    
      
        for sprite in self.obstacles.sprites(): # Players can't overlap obstacles (x axis)
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
            
        
        for sprite in self.levers.sprites(): # Players can't overlap levers (x axis)
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for item in self.items:
            item.apply_gravity()
        

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
                    
            for item in self.items.sprites():
                if sprite.rect.colliderect(item.rect): #if player collides with a tile
                
                    if item.direction.y > 0: #moving left
                        item.rect.bottom = sprite.rect.top
                        item.direction.y = 0

                    elif item.direction.y < 0: #moving right
                        item.rect.top = sprite.rect.bottom
                        item.direction.y = 0
                        
        for sprite in self.obstacles.sprites(): # Players can't overlap obstacles (y axis)
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    
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
    
    # For later: generalize key for player/objects that can make them disappear
    def obstacle_behavior(self):
        player = self.player.sprite

        for sprite in self.points.sprites(): # looking through all point locations
            if sprite.rect.colliderect(player.rect): # if player collides, remove
                print('Point collection')
                sprite.kill()

        for sprite in self.obstacles.sprites(): # looking through all obstacles
            if sprite.rect.left == player.rect.right or sprite.rect.right == player.rect.left: # if the player is next to the obstacle
                if sprite.obstacleID == 0: # if the obstacle is not tied to a lever
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: # if key is pressed
                            if event.key == pygame.K_k: # and it is the interact button, remove
                                print('Obstacle collision, removed')
                                sprite.kill()
                #else:
                    #print('Special obstacle id ' + str(sprite.obstacleID))

    def lever_flip(self):
        player = self.player.sprite

        for sprite in self.levers.sprites(): # looking through all obstacles
            if sprite.rect.left == player.rect.right or sprite.rect.right == player.rect.left: # if the player is next to the obstacle
                if sprite.flipUse == 1: # levers can only be used once
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN: # if key is pressed
                            if event.key == pygame.K_k: # and it is the interact button
                                for spriteOb in self.obstacles.sprites():
                                    if spriteOb.obstacleID == sprite.leverID: # delete the corresponding object to lever ID
                                        print('Lever flipped, corresponding obstacle of id ' + str(spriteOb.obstacleID) + ' has been removed')
                                        spriteOb.kill()
                                        break
                                sprite.flipUse = 0 # Lever no longer works
                                sprite.update() # Update lever sprite
                #else:
                    #print('Lever id ' + str(sprite.leverID) + ' is deactivated')
                    

    def run(self):
        self.tiles.draw(self.display_surface)
        
        self.obstacles.draw(self.display_surface)

        self.points.draw(self.display_surface)

        self.levers.draw(self.display_surface)
        
        for enemy in self.enemies:
            sight_rect = enemy.update()
            #pygame.draw.rect(self.display_surface, "white", sight_rect)   #comment out to not draw the sight rect
            for player in self.player:
                if enemy.detect_player(player.rect, self.tiles):
                    print("detected")
        self.enemies.draw(self.display_surface)
        
        self.player.update(self.items)
        self.player.draw(self.display_surface)
        
        self.banker.update()
        self.banker.draw(self.display_surface)
        
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        self.banker_horizontal_movement_collision()
        self.banker_vertical_movement_collision()
        
        self.obstacle_behavior()
        self.lever_flip()
        
        for item in self.items:
            self.display_surface.blit(item.image, item.rect)
