import pygame, sys, math
pygame.init()
dt = 1


screen = (1920, 1080)
FOV = 60
distance_from_screen = (screen[0]/2)/(math.tan(FOV/2))

player = [250, 250]
size = 75
map =   [['_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','0','0','0','0','0','0','0','0','0','0','0','_'],
        ['_','0','0','_','0','0','0','0','0','0','0','0','_'],
        ['_','0','0','0','0','0','0','0','_','0','_','0','_'],
        ['_','0','0','_','_','0','0','0','0','_','0','0','_'],
        ['_','0','0','_','0','0','0','0','_','0','_','0','_'],
        ['_','0','0','_','0','0','0','0','0','0','0','0','_'],
        ['_','0','0','0','0','0','0','0','0','0','0','0','_'],
        ['_','0','0','0','0','0','0','0','0','0','0','0','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_']]
WIDTH = len(map[0])*size
HEIGHT = len(map)*size
speed = 2*dt
angle = 0
ROT_SPEED = dt*math.pi/180
#prev_pos = [250,250]
WALLS =[]
W = False
A = False
S = False
D = False
anglep = False
anglem = False
temporaryX = []
temporaryY = []
c = []
ray = []
prev_player = []


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
#WALLS
playerRect = pygame.Rect(player[0], player[1], 1, 1)
for i in range(len(map)):
        for j in range(len(map[0])):
            #pygame.draw.rect(screen, 'black', pygame.Rect(j*size, i*size, size, size))
            if map[i][j] == '_':
                #pygame.draw.rect(screen, 'white', pygame.Rect(j*size, i*size, size, size),2)
                WALLS.append(pygame.Rect(j*size, i*size, size ,size))
                try:
                    if map[i-1][j-1] == '_':
                        WALLS.append(pygame.Rect(j*size-size/20, i*size-size/20, size/10, size/10))
                    if map[i-1][j+1] == '_':
                        WALLS.append(pygame.Rect((j+1)*size-size/20, i*size-size/20, size/10, size/10))
                except:
                    pass
            
def draw_map():
    for i in range(len(map)):
        for j in range(len(map[0])):
            #pygame.draw.rect(screen, 'black', pygame.Rect(j*size, i*size, size, size))
            #pygame.draw.rect(screen, 'orange', pygame.Rect(j*size, i*size, size, size),2)
            pass
            if map[i][j] == '_':
                pass
                #pygame.draw.rect(screen, 'white', pygame.Rect(j*size, i*size, size, size),2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                W = True
            if event.key == pygame.K_a:
                A = True
            if event.key == pygame.K_s:
                S = True
            if event.key == pygame.K_d:
                D = True
            if event.key == pygame.K_LEFT:
                anglep = True
            if event.key == pygame.K_RIGHT:
                anglem = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                W = False
            if event.key == pygame.K_a:
                A = False
            if event.key == pygame.K_s:
                S = False
            if event.key == pygame.K_d:
                D = False
            if event.key == pygame.K_LEFT:
                anglep = False
            if event.key == pygame.K_RIGHT:
                anglem = False

    
    if W:
        prev_player = player[:]
        player[0] += math.cos(angle)*speed
        player[1] += math.sin(angle)*speed
        playerRect = pygame.Rect(player[0], player[1], 1, 1)
        if playerRect.collidelist(WALLS) != -1:
            player = prev_player[:]
    if S:
        prev_player = player[:]
        player[0] += -math.cos(angle)*speed
        player[1] += -math.sin(angle)*speed
        playerRect = pygame.Rect(player[0], player[1], 1, 1)
        if playerRect.collidelist(WALLS) != -1:
            player = prev_player[:]
    if A:
        prev_player = player[:]
        player[1] += -math.cos(angle)*speed
        player[0] += math.sin(angle)*speed
        playerRect = pygame.Rect(player[0], player[1], 1, 1)
        if playerRect.collidelist(WALLS) != -1:
            player = prev_player[:]
    if D:
        prev_player = player[:]
        player[1] += math.cos(angle)*speed
        player[0] += -math.sin(angle)*speed
        playerRect = pygame.Rect(player[0], player[1], 1, 1)
        if playerRect.collidelist(WALLS) != -1:
            player = prev_player[:]

    pygame.draw.circle(screen, 'blue', center=(player[0], player[1]), radius=20)
    FOV = math.pi/3
    RESOLUTION = (WIDTH,HEIGHT)
    NUM_OF_RAYS = RESOLUTION[1]/2
    rays = []
    start_angle = angle-FOV/2
    finalrays = []
    for ray in range(int(NUM_OF_RAYS)):
        #rays.append([math.cos(start_angle) * math.sqrt(WIDTH**2+HEIGHT**2)+player[0],math.sin(start_angle) * math.sqrt(WIDTH**2+HEIGHT**2)+player[1]])
        '''for i in rays:
        pygame.draw.line(screen, 'green', (player[0], player[1]), (i[0], i[1]))'''
        sin_a = math.sin(start_angle)
        cos_a = math.cos(start_angle)
        tan_a = math.tan(start_angle)

        playerdepthx = player[0]%size
        playerdepthy = player[1]%size
        playertilex = player[0]//size
        playertiley = player[1]//size


        elojelx = 0
        elojely = 0
        if cos_a > 0:
            xvert = player[0]+(size-playerdepthx)
            yhor = player[1]+(xvert-player[0])*(tan_a+0.00001)
            elojelx = 1
            #pygame.draw.line(screen, 'green', (player[0], player[1]), (xvert, yhor))#ennél 270°-nál nem műkszik
        else:
            xvert = player[0]-playerdepthx-0.00001
            yhor = player[1]-(player[0]-xvert)*(tan_a+0.00001)
            elojelx = -1
            #pygame.draw.line(screen, 'green', (player[0], player[1]), (xvert, yhor)) #this looks good
        if sin_a > 0:
            yvert = player[1]+(size-playerdepthy)
            xhor = player[0]+(yvert-player[1])/(tan_a+0.00001)
            elojely = 1
            #pygame.draw.line(screen, 'green', (player[0], player[1]), (xhor, yvert))
        else:
            yvert = player[1] -playerdepthy-0.00001
            xhor = player[0]-(player[1]-yvert)/(tan_a+0.00001)
            elojely = -1
            #pygame.draw.line(screen, 'green', (player[0], player[1]), (xhor, yvert))
        #eddig jó
        #xtengely
        x = elojelx*size
        y = x*(tan_a+0.00001)
        xstart = xvert
        ystart = yhor
        finalx = []
        finaly = []
        for _ in range(20):
            xdepth = 5000
            try:
                if map[int(ystart//size)][int(xstart//size)] == '_':
                    finalx.append([xstart, ystart])
                    xdepth = math.sqrt((player[0]-xstart)**2+(player[1]-ystart)**2)+0.00001
                    break
                xstart += x
                ystart += y
            except:
                pass
        #ytengely
        y = elojely*size
        x = y/(tan_a+0.00001)
        xstart = xhor
        ystart = yvert
        for _ in range(20):
            ydepth = 5000
            try:
                if map[int(ystart//size)][int(xstart//size)] == "_":
                    finaly.append([xstart, ystart])
                    ydepth = math.sqrt((player[0]-xstart)**2+(player[1]-ystart)**2)+0.00001
                    break
                xstart += x
                ystart += y
            except:
                pass
        try:
            if xdepth < ydepth:
                finalrays.append([finalx[0][0],finalx[0][1]])
                #pygame.draw.line(screen, 'green', (player[0], player[1]), (finalx[0][0], finalx[0][1]))
            else:
                finalrays.append([finaly[0][0], finaly[0][1]])
                #pygame.draw.line(screen, 'green', (player[0], player[1]), (finaly[0][0], finaly[0][1]))
        except:
            pass
        WALL = size*10
        PLAYER = 500
        VFOV = 2.5*FOV

        screen_ray = RESOLUTION[1]/2*math.tan((math.pi-VFOV)/2)
        ray_distance = math.sqrt((player[0]-finalrays[ray][0])**2+(player[1]-finalrays[ray][1])**2)#*math.cos(angle-(ray*FOV/NUM_OF_RAYS))
        lambdaa = screen_ray/ray_distance
        if lambdaa > 1:
            lambdaa = 1
        ray_height = RESOLUTION[1]/lambdaa
#1 irányba műkszik??
#nem nő szépen lassan
        felso_limit = (WALL-PLAYER)*math.tan((math.pi-VFOV)/2)
        also_limit = PLAYER*math.tan((math.pi-VFOV)/2)
        if ray_distance < felso_limit and ray_distance <also_limit:
            pygame.draw.line(screen, 'white',(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),0),(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),RESOLUTION[1]),3)
        elif ray_distance>felso_limit and ray_distance < also_limit:
            felso_hossz = ray_distance-felso_limit
            PLAFON = felso_hossz*math.tan(VFOV/2)
            pygame.draw.line(screen, 'lightblue',(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),0),(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),PLAFON*lambdaa),3)
            pygame.draw.line(screen, 'white',(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),PLAFON*lambdaa),(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),RESOLUTION[1]),3)
        else:
            felso_hossz = ray_distance-felso_limit
            PLAFON = felso_hossz*math.tan(VFOV/2)
            also_hossz = ray_distance-also_limit
            TALAJ = also_hossz*math.tan(VFOV/2)
            pygame.draw.line(screen, 'lightblue',(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),0),(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),PLAFON*lambdaa),3)
            pygame.draw.line(screen, 'white',(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),PLAFON*lambdaa),(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),(PLAFON*lambdaa)+WALL*lambdaa),3)
            pygame.draw.line(screen, 'brown',(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),(PLAFON*lambdaa)+WALL*lambdaa),(RESOLUTION[0]*ray*(FOV/NUM_OF_RAYS),RESOLUTION[1]),3)


        start_angle += FOV/NUM_OF_RAYS
    
    #3d
    
    


    prev_pos = [player[0], player[1]]
    if anglep:
        angle += -ROT_SPEED 
        angle += -ROT_SPEED
        angle %= math.tau
        #angle %= math.tau
    if anglem:
        angle += ROT_SPEED 
        angle += ROT_SPEED
        angle %= math.tau

    pygame.display.flip()
    dt = clock.tick(0)/1000
    pygame.display.set_caption(str(round(clock.get_fps(),2)))
    draw_map()
