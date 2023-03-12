#--------------------------------------------------------
# Import and initialize the pygame library
#--------------------------------------------------------

import pygame, os, random, sys
from settings import *
from tiles import Tile
from level import Level
from statemachine import StateMachine, State

pygame.init()
pygame.mixer.init()
#pygame.mixer.music.set_volume(0.01)

#--------------------------------------------------------
# Check if the images are loaded
#--------------------------------------------------------
if not os.path.exists("imgs"):
    print("you do not have imgs folder")

#--------------------------------------------------------
# Sets the bar icon and text for game window
# Defines size for convert()
#--------------------------------------------------------
pygame.display.set_caption('Break the Bank')
gameicon = pygame.image.load("imgs/game_icon.png")
pygame.display.set_icon(gameicon)
size = 80
levels_to_draw = 2

button_hover = pygame.mixer.Sound('audio/sfx/button_hover.mp3')
button_hover.set_volume(1.0)
esc_click = pygame.mixer.Sound('audio/sfx/esc_click.wav')
esc_click.set_volume(1.0)
#--------------------------------------------------------
# Define Drawing States
#--------------------------------------------------------

class CurrentScene(StateMachine):
    scene_main_menu = State("mainMenu", initial = True)
    scene_level_selection = State("Level Selection")
    scene_in_game = State("In Game")
    scene_pause_menu = State("Paused")
    scene_death_menu = State("Death")
    global levels_to_draw
    musicON = True
    # to create new scene, declare, create a variable for it, put it in init on_transition, and update the update var

    go_to_next_scene = scene_main_menu.to(scene_level_selection, cond = "select_stage") | scene_level_selection.to(scene_main_menu, cond = "main_menu") | scene_level_selection.to(
        scene_in_game, cond = "in_game") | scene_in_game.to(scene_main_menu, cond = "main_menu") | scene_in_game.to(
        scene_pause_menu, cond = "pause_menu") | scene_pause_menu.to(scene_in_game, cond = "in_game") | scene_pause_menu.to(scene_level_selection, cond = "select_stage") | scene_in_game.to(
        scene_death_menu, cond = "death_menu")| scene_death_menu.to(scene_level_selection, cond = "select_stage") | scene_death_menu.to(scene_in_game, cond = "in_game")
    
    
    
    update = scene_main_menu.to.itself(on="drawMainMenu") | scene_level_selection.to.itself(on="drawStageSelection") | scene_in_game.to.itself(
        on="drawInGame") | scene_pause_menu.to.itself(on="drawPauseMenu") | scene_death_menu.to.itself(on="drawDeathMenu")

    def __init__(self):
        # self.calls = []
        self.select_stage = False
        self.main_menu = False
        self.in_game = False
        self.pause_menu = False
        self.death_menu = False
        self.curr_screen = screen.copy()
        self.current_level = ""
        self.current_level_parems = ""
        super().__init__()
        print("DEF INIT")

    def on_transition(self):
        self.select_stage = False
        self.main_menu = False
        self.in_game = False
        self.pause_menu = False
        self.death_menu = False
        # print("ON_TRANSITION")

    def checkChange(self):
        if self.select_stage | self.main_menu | self.in_game | self.pause_menu | self.death_menu:
            return True


    #-------------MAIN MENU-------------
    def drawMainMenu(self):
        if self.musicON is True:
            bgm_ch.play(menuMusic, loops=-1, fade_ms=100)
            self.musicON = False
            print("bgm_ch play menuMusic")
        mainMenu.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isOver(mouse):
                    button_hover.play()
                    self.select_stage = True
                    print("TRIGGERED start game")
                if quit_button.isOver(mouse):
                    button_hover.play()
                    sys.exit()
                    pygame.quit()
            if event.type == pygame.KEYDOWN: #temp to get coords
                if event.key == pygame.K_RETURN:
                    print(mouse)

    #-------------STAGE SELECTION-------------
    def drawStageSelection(self):
        if self.musicON is False:
            bgm_ch.play(selectMusic, loops=-1, fade_ms=100)
            self.musicON = True
            print("bgm_ch play selectMusic")
        stageSelection.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (stage_placeholderbutton_1.isOver(mouse) and 1<=levels_to_draw):
                    button_hover.play()
                    print("TRIGGERED stage selection -> in game")
                    self.current_level = level_map
                    self.current_level_parems = level_param
                    self.level = Level(self.current_level, self.current_level_parems, screen, "./imgs/stage1_lobby.png")
                    self.in_game = True
                if (stage_placeholderbutton_2.isOver(mouse) and 2<=levels_to_draw):
                    button_hover.play()
                    print("TRIGGERED stage selection -> in game")
                    self.current_level = level_map_1
                    self.current_level_parems = level1_param
                    self.level = Level(self.current_level, self.current_level_parems, screen, "./imgs/stage1_lobby.png")
                    self.in_game = True
                if (stage_placeholderbutton_3.isOver(mouse) and 3<=levels_to_draw):
                    button_hover.play()
                    print("TRIGGERED stage selection -> in game")
                    self.current_level = level_map_1
                    self.current_level_parems = level1_param
                    self.level = Level(self.current_level, self.current_level_parems, screen, "./imgs/stage1_lobby.png")
                    self.in_game = True
                if (stage_placeholderbutton_4.isOver(mouse) and 4<=levels_to_draw):
                    button_hover.play()
                    print("TRIGGERED stage selection -> in game")
                    self.current_level = level_map_1
                    self.current_level_parems = level1_param
                    self.level = Level(self.current_level, self.current_level_parems, screen, "./imgs/stage1_lobby.png")
                    self.in_game = True
                if (stage_placeholderbutton_5.isOver(mouse) and 5<=levels_to_draw):
                    button_hover.play()
                    print("TRIGGERED stage selection -> in game")
                    self.current_level = level_map_1
                    self.current_level_parems = level1_param
                    self.level = Level(self.current_level, self.current_level_parems, screen, "./imgs/stage1_lobby.png")
                    self.in_game = True
                if (stage_placeholderbutton_6.isOver(mouse) and 6<=levels_to_draw):
                    button_hover.play()
                    print("TRIGGERED stage selection -> in game")
                    self.current_level = level_map_1
                    self.current_level_parems = level1_param
                    self.level = Level(self.current_level, self.current_level_parems, screen, "./imgs/stage1_lobby.png")
                    self.in_game = True
                if quit_mainmenu_button.isOver(mouse):
                    button_hover.play()
                    self.main_menu = True


    #-------------IN GAME-------------
    def drawInGame(self):
        # game_stage()
        if self.musicON is True:
            bgm_ch.play(wipMusic, loops=-1, fade_ms=100)
            self.musicON = False
            print("bgm_ch play wipMusic")
        screen.fill('black')
        
        keep_running, outcome = self.level.run()
        if not keep_running:
            if outcome == "loss":
                self.curr_screen = screen.copy()
                self.death_menu = True 
            else:
                self.curr_screen = screen.copy()
                self.pause_menu = True 
                
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # put physics stuff here to remember when unpausing
                    esc_click.play()
                    self.curr_screen = screen.copy()
                    self.pause_menu = True
                # if event.key == pygame.K_RETURN:
                #     button_hover.play()
                #     self.main_menu = True

    #-------------PAUSE MENU-------------
    def drawPauseMenu(self):
        if self.musicON is False:
            bgm_ch.pause()
            self.musicON = True
            print("====pause menu stop music")
        screen.blit(self.curr_screen,(0,0))
        pauseMenu.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.isOver(mouse):
                    button_hover.play()
                    self.in_game = True
                if quit_button.isOver(mouse):
                    button_hover.play()
                    self.musicON = False
                    self.select_stage = True
                if restart_button.isOver(mouse):
                    self.level = Level(self.current_level, self.current_level_parems, screen, "./imgs/stage1_lobby.png")
                    self.in_game = True
                    self.musicON = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # go back to game
                    esc_click.play()
                    self.in_game = True


    #-------------DEATH MENU-------------
    def drawDeathMenu(self):
        if self.musicON is False:
            bgm_ch.pause()
            self.musicON = True
            print("====pause menu stop music")
        screen.blit(self.curr_screen,(0,0))
        deathMenu.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.isOver(mouse):
                    button_hover.play()
                    self.musicON = False
                    self.select_stage = True
                if restart_button.isOver(mouse):
                    self.level = Level(self.current_level, self.current_level_parems, screen, "./imgs/stage1_lobby.png")
                    self.in_game = True
                    self.musicON = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # go back to game
                    esc_click.play()
                    self.select_stage = True


#--------------------------------------------------------
# Define Drawing Scenes
#--------------------------------------------------------


class Scene():
    def __init__(self, screen, background, buttonArray, transparency = False):
        self.screen = screen
        self.buttons = buttonArray
        # self.states = stateArray
        self.background = background
        self.transparency = transparency

    def update(self):
        if self.transparency:
            # screen.blit(self.screen,(0,0))
            backgroundphoto = pygame.image.load(self.background)
            backgroundphoto = pygame.transform.scale(backgroundphoto, (size*16,size*9))
            backgroundphoto.set_alpha(250)
            screen.blit(backgroundphoto, (0,0))
            for individualButton in range(len(self.buttons)):
                self.buttons[individualButton].draw(screen)
        else:
            # print(self.buttons)
            backgroundphoto = pygame.image.load(self.background).convert()
            backgroundphoto = pygame.transform.scale(backgroundphoto, (size*16,size*9))
            screen.blit(backgroundphoto,(0,0))
            for individualButton in range(len(self.buttons)):
                self.buttons[individualButton].draw(self.screen)
            

#--------------------------------------------------------
# Define buttons
#--------------------------------------------------------
class button():
    def __init__(self, x,y,width,height, text='', color = None,image=None, hovering_image=None, amplifier=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = image
        self.hovering_image = hovering_image
        self.amplifier = amplifier

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if self.color != None:
            if outline:
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        
        if self.image != None:
            if self.amplifier == None:
                if not self.isOver(pygame.mouse.get_pos()):
                    image = pygame.image.load(self.image)
                    rect_image = image.get_rect()
                    
                    image = pygame.transform.scale(image, ((rect_image.width/(237.5*16))*size*16,(rect_image.height/(237.5*9))*size*9))
                    
                else:
                    image = pygame.image.load(self.hovering_image)
                    rect_image = image.get_rect()
                    image = pygame.transform.scale(image, ((rect_image.width/(237.5*16))*size*16,(rect_image.height/(237.5*9))*size*9))
            else:
                if not self.isOver(pygame.mouse.get_pos()):
                    image = pygame.image.load(self.image)
                    rect_image = image.get_rect()
                    #print(rect_image)
                    image = pygame.transform.scale(image, ((rect_image.width/(self.amplifier*16))*size*16,(rect_image.height/(self.amplifier*9))*size*9))
                else:
                    image = pygame.image.load(self.hovering_image)
                    rect_image = image.get_rect()
                    image = pygame.transform.scale(image, ((rect_image.width/(self.amplifier*16))*size*16,(rect_image.height/(self.amplifier*9))*size*9))
            win.blit(image, (self.x, self.y))


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if self.image == None:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
                
            return False
        elif self.amplifier == None:
            image = pygame.image.load(self.image)
            rect_image = image.get_rect()
            if pos[0] > self.x and pos[0] < self.x + (rect_image.width/(237.5*16))*size*16:
                if pos[1] > self.y and pos[1] < self.y + (rect_image.height/(237.5*9))*size*9:
                    return True
            
            return False
        else:
            image = pygame.image.load(self.image)
            rect_image = image.get_rect()
            if pos[0] > self.x and pos[0] < self.x + (rect_image.width/(self.amplifier*16))*size*16:
                if pos[1] > self.y and pos[1] < self.y + (rect_image.height/(self.amplifier*9))*size*9:
                    return True
            
            return False

#--------------------------------------------------------
# Load background music
#--------------------------------------------------------
menuMusic = pygame.mixer.Sound("audio\stage1_bgm_spookydarkpad.mp3") ; menuMusic.set_volume(1.0)
selectMusic = pygame.mixer.Sound("audio\maintheme_syndicate.mp3"); selectMusic.set_volume(0.4)
wipMusic = pygame.mixer.Sound("audio\wip\duskwalkinloop.wav"); wipMusic.set_volume(0.4)

bgm_ch = pygame.mixer.Channel(0)
bgm_ch.set_volume(0.3)
bgm_ch.play(menuMusic, loops = -1, fade_ms = 500)


#--------------------------------------------------------
# Set up the drawing window
#--------------------------------------------------------
screen = pygame.display.set_mode([size*16, size*9])
# screen = pygame.transform.scale(backgroundphoto,[859, 727])
width = screen.get_width()
height = screen.get_height()

# tile_size = 45
# height = len(level_map) * tile_size
# width = len(level_map[0])
# print(width)


start_button = button(width/2.807,height/1.6,20,100,'',None,"imgs/buttons/slice_start.png","imgs/buttons/hovering_slice_start.png")
quit_button = button(width/2.2,height/1.3,20,100,'',None,"imgs/buttons/slice_quit.png", "imgs/buttons/hovering_slice_quit.png")
quit_mainmenu_button = button(width/20,height/20,20,100,'',None,"imgs/buttons/slice_quit.png", "imgs/buttons/hovering_slice_quit.png")
audio_button = button(width/2.015748,height/1.15,20,100,'',None,"imgs/buttons/slice_audio.png", "imgs/buttons/hovering_slice_audio.png")
accessibility_button = button(width/2.4063063,height/1.15,20,100,'',None,"imgs/buttons/slice_cb.png", "imgs/buttons/hovering_slice_cb.png")
continue_button = button(width/2.4288,height/2.1951219, 20, 100, '', None, "imgs/buttons/slice_continue.png","imgs/buttons/hovering_slice_continue.png",160)
restart_button = button(width/2.4015,height/1.75182, 20, 100, '', None, "imgs/buttons/slice_restart.png","imgs/buttons/hovering_slice_restart.png",160)
tutorial_button = button(width/2.424242,height/1.50627, 20, 100, '', None, "imgs/buttons/slice_tutorial.png","imgs/buttons/hovering_slice_tutorial.png",160)
pause_title = button(width/3.12195,height/11.6129, 20, 100, '', None, "imgs/slice_paused.png","imgs/slice_paused.png",160) #bad code 
death_title = button(width/5.62195,height/6.6129, 20, 100, '', None, "imgs/slice_gameover.png","imgs/slice_gameover.png",160) #bad code 

# TODO: placeholders for Stage Selection Menu
stage_placeholderbutton_1 = button(width/18,height/3,0,20,'',None,"imgs/stage_placeholderbutton.png","imgs/stage_placeholderbutton_hover.png")
stage_placeholderbutton_2 = button(width/18+1*(width/3),height/3,0,20,'',None,"imgs/stage_placeholderbutton.png","imgs/stage_placeholderbutton_hover.png")
stage_placeholderbutton_3 = button(width/18+2*(width/3),height/3,0,20,'',None,"imgs/stage_placeholderbutton.png","imgs/stage_placeholderbutton_hover.png")
stage_placeholderbutton_4 = button(width/18,height/3+(height/3),0,20,'',None,"imgs/stage_placeholderbutton.png","imgs/stage_placeholderbutton_hover.png")
stage_placeholderbutton_5 = button(width/18+1*(width/3),height/3+(height/3),0,20,'',None,"imgs/stage_placeholderbutton.png","imgs/stage_placeholderbutton_hover.png")
stage_placeholderbutton_6 = button(width/18+2*(width/3),height/3+(height/3),0,20,'',None,"imgs/stage_placeholderbutton.png","imgs/stage_placeholderbutton_hover.png")

# notify_msg = button( width/2+50, height/2, 250, 100,"PRESS ENTER TO GO BACK TO MAIN MENU FOR NOW",(255, 0, 255), None, None)


overallScreen = CurrentScene()


levels_list = [stage_placeholderbutton_1 ,stage_placeholderbutton_2 ,stage_placeholderbutton_3 ,stage_placeholderbutton_4 ,stage_placeholderbutton_5 ,stage_placeholderbutton_6 ]
stageSelection_list = [quit_mainmenu_button]
# print(range(len(levels_list)))
def drawAmount(current_levels):
    for x in range(0,6):
        if x <= current_levels:
            stageSelection_list.append(levels_list[x])


drawAmount(levels_to_draw-1)

# Draw buttons 
pauseMenu = Scene(overallScreen.curr_screen, "imgs/pause_bg_light.png", [continue_button, restart_button, tutorial_button, pause_title, quit_button, audio_button, accessibility_button], True)
InGame = Scene(screen, "imgs/in_game.png", [])
mainMenu = Scene(screen, "imgs/start_bare.png", [start_button,quit_button,audio_button,accessibility_button])
stageSelection = Scene(screen, "imgs/stage_select.png", stageSelection_list)
deathMenu = Scene(overallScreen.curr_screen, "imgs/pause_bg_light.png", [restart_button, tutorial_button, death_title, quit_button, audio_button, accessibility_button], True)

        

#--------------------------------------------------------
#Define Booleans for stage states
#--------------------------------------------------------
running = True #game run state
main_menu_music = True
#--------------------------------------------------------
# Main Game Loop
# - Clock tick needs to be contained here
# - Game state is controlled here44
#--------------------------------------------------------


while running:
    timer = pygame.time.Clock()
    timer.tick(60)
    
    overallScreen.update()
    if overallScreen.checkChange():
        overallScreen.go_to_next_scene()

    #-------------PAUSE MENU-------------
   
    pygame.display.update()
                #for finding location of button
                # if event.key == pygame.K_RIGHT:
                #     xIMG = xIMG+1
                # if event.key == pygame.K_LEFT:
                #     xIMG = xIMG-1
                # if event.key == pygame.K_DOWN:
                #     yIMG = yIMG+1
                # if event.key == pygame.K_UP:
                #     yIMG = yIMG-1
                # if event.key == pygame.K_RETURN:
                #     print("x: " +str(xIMG) + " y: " +str(yIMG))
                # if event.key == pygame.K_SPACE:
                #     # print("width: " + str(width/mouse[0]))
                #     # print("height: " + str(height/mouse[1]))
                #     print(pygame.mouse.get_pos())


    # Fill the background with white
    
    
    # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
    #         pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
            
    # else:
    #     pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
    # screen.blit(text , (width/2+50,height/2))


# Done! Time to quit.
pygame.quit()
sys.exit()
