import pygame

black = 0, 0, 0

pygame.init()
def get_image(sheet,framex,framey,flipped,width,height,scale,color):
    image = pygame.Surface((width,height))
    image.blit(sheet,(0,0),(framex * width,framey*height,width,height))
    image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    image = pygame.transform.flip(image,flipped,False)
    image.set_colorkey(color)
    return image

class DrawGame():
    #sprite_sheet_image = pygame.image.load('images/hero.png').convert_alpha()
    #ground = pygame.image.load('images/grass-tile.png').convert()
    #ground2 = pygame.image.load('images/grass-tile-2.png').convert()
    #ground3 = pygame.image.load('images/olive2.png').convert()
    #frame_n = get_image(sprite_sheet_image,1, 1, False, 16, 16,3,black)
    #frame_s = get_image(sprite_sheet_image,1, 2, False, 16, 16,3,black)
    #frame_o = get_image(sprite_sheet_image,1, 0, False, 16, 16,3,black)
    #frame_e = get_image(sprite_sheet_image,1, 0, True, 16, 16,3,black)    
    tilesize = 48

    def __init__(self,screen):
        global tilesize, grass,grass1,grass2,grass3, terrain, olive1,olive2,olive3, frame_n, frame_s, frame_o, frame_e, sprite_sheet_image
        self.screen = screen
        sprite_sheet_image = pygame.image.load('images/hero.png').convert_alpha()
        grass = pygame.image.load('images/grass-tile.png').convert()
        grass1 = pygame.image.load('images/grass1.png').convert()
        grass2 = pygame.image.load('images/grass2.png').convert()
        grass3 = pygame.image.load('images/grass3.png').convert()
        terrain = pygame.image.load('images/grass-tile-2.png').convert()
        olive1 = pygame.image.load('images/olive1.png').convert()
        olive2 = pygame.image.load('images/olive2.png').convert()
        olive3 = pygame.image.load('images/olive3.png').convert()
        frame_n = get_image(sprite_sheet_image,1, 1, False, 16, 16,3,black)
        frame_s = get_image(sprite_sheet_image,1, 2, False, 16, 16,3,black)
        frame_o = get_image(sprite_sheet_image,1, 0, False, 16, 16,3,black)
        frame_e = get_image(sprite_sheet_image,1, 0, True, 16, 16,3,black) 
        tilesize = 48
        

    def draw_map(self,matrix,playerpos,items):
        global tilesize, grass,grass1,grass2,grass3, terrain,olive1,olive2,olive3 
        groundrect = pygame.Rect(0, 0,tilesize,tilesize)

        start_x = playerpos[0]-5
        end_x = playerpos[0]+6
        start_y =playerpos[1]-5
        end_y = playerpos[1]+6
        rect_x = 0
        rext_y = 0
        #print_matrix(map['matrix'])
        #print(start_x, end_x, start_y, end_y)
        
        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                groundrect.x = rect_x * tilesize
                groundrect.y = rext_y * tilesize
                if i>=0 and i<len(matrix) and j>=0 and j<len(matrix[i]):
                    if matrix[i][j].type == "O":
                        if matrix[i][j].situation == 0:
                            self.screen.blit(olive1, groundrect)
                        elif matrix[i][j].situation == 1:
                            self.screen.blit(olive1, groundrect)
                        elif matrix[i][j].situation == 2:
                            self.screen.blit(olive2, groundrect)
                        elif matrix[i][j].situation == 3:
                            self.screen.blit(olive3, groundrect)
                    elif matrix[i][j].type == "T":
                        self.screen.blit(terrain, groundrect)
                    elif matrix[i][j].type == "G":
                        if matrix[i][j].situation == 0:
                            self.screen.blit(grass, groundrect)
                        elif matrix[i][j].situation == 1:
                            self.screen.blit(grass1, groundrect)
                        elif matrix[i][j].situation == 2:
                            self.screen.blit(grass2, groundrect)
                        elif matrix[i][j].situation == 3:
                            self.screen.blit(grass3, groundrect)
                    # draw items
                    for item in items:
                        if item.position[0] == i and item.position[1] == j and item.visible:
                            self.screen.blit(item.image, groundrect)
                else:
                    pygame.draw.rect(self.screen, [0,0,0], groundrect)

                rext_y += 1
            rext_y = 0
            rect_x += 1

    def draw_player(self,dir):
        global frame_n, frame_s, frame_o, frame_e, tilesize
        position = 5*tilesize, 5*tilesize
        if dir == 'n':
            self.screen.blit(frame_n, position)
        elif dir == 's':
            self.screen.blit(frame_s, position)
        elif dir == 'o':
            self.screen.blit(frame_o, position)
        elif dir == 'e':
            self.screen.blit(frame_e, position)
        else:
            self.screen.blit(frame_s, position)

    #draw inventory
    def draw_inventory(self,player,pickup=True):
        groundrect = pygame.Rect(11*tilesize, 10*tilesize,tilesize,tilesize)
        if(pickup):
            self.screen.blit(player.inventory.image, groundrect)
        else:
            pygame.draw.rect(self.screen, [0,0,0], groundrect)

    def positionallowed(self,matrix,x,y):
        
        if x<0 or x>=len(matrix) or y<0 or y>=len(matrix[x]):
            return False

        if matrix[x][y].type == "T" or matrix[x][y].type == 'G':
            return True
        else:
            return False
