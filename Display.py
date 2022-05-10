import pygame
import pygame_menu
pygame.init()
width = 1200
height = 650
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Palindromic Tree")
screen.fill(black)
# def prnt(Widget, Menu,):
#     global cnt
#     print(cnt)
def mainmenu():
    closed = False
    a = pygame_menu.pygame_menu.widgets.ScrollBar(500, (0,100),orientation="orientation-vertical")  #Scroll bar
    # a.add_draw_callback(prnt)
    imag_root_node = pygame.image.load("Imaginary Root Node.png")
    dft_root_node = pygame.image.load("Default Root Node.png")
    All_Nodes = {"Imag":(3*width/4 - imag_root_node.get_rect().w/2, 50), "Default": (width/4 - dft_root_node.get_rect().w/2,50)}
    while not(closed):
        screen.fill(black)
        x_1 = All_Nodes["Default"][0] + dft_root_node.get_rect().w/2
        y_1 = All_Nodes["Default"][1] + dft_root_node.get_rect().h
        pygame.draw.line(screen, white, (x_1,y_1), (x_1-100,y_1+100))
        pygame.draw.line(screen, white, (x_1,y_1), (x_1+100,y_1+100))
        # screen.blit(line_temp, (20,20))
        # cnt += 1
        # image = pygame.transform.scale(image, (40,40))
        font = pygame.font.SysFont('timesnewroman', 50)
        # text = font.render("John Nash's Demon", True, (255,255,255))
        # textRect = text.get_rect()
        # textRect.center = (320, 90)
        # screen.blit(text, textRect)
        screen.blit(imag_root_node, All_Nodes["Imag"])
        screen.blit(dft_root_node, All_Nodes["Default"])
        # a.draw(screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
                All_Nodes["Imag"] = (All_Nodes["Imag"][0],All_Nodes["Imag"][1]-0.5)
                All_Nodes["Default"] = (All_Nodes["Default"][0],All_Nodes["Default"][1]-0.5)
        if keys[pygame.K_UP]:
                All_Nodes["Imag"] = (All_Nodes["Imag"][0],All_Nodes["Imag"][1]+0.5)
                All_Nodes["Default"] = (All_Nodes["Default"][0],All_Nodes["Default"][1]+0.5)
        if keys[pygame.K_LEFT]:
            All_Nodes["Imag"] = (All_Nodes["Imag"][0]-0.5,All_Nodes["Imag"][1])
            All_Nodes["Default"] = (All_Nodes["Default"][0]-0.5,All_Nodes["Default"][1])
        if keys[pygame.K_RIGHT]:
            All_Nodes["Imag"] = (All_Nodes["Imag"][0]+0.5,All_Nodes["Imag"][1])
            All_Nodes["Default"] = (All_Nodes["Default"][0]+0.5,All_Nodes["Default"][1])
        for event in pygame.event.get():
            
            if (event.type == pygame.QUIT):
                closed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_DOWN or keys[pygame.K_DOWN]:
                    All_Nodes["Imag"] = (All_Nodes["Imag"][0],All_Nodes["Imag"][1]-5)
                    All_Nodes["Default"] = (All_Nodes["Default"][0],All_Nodes["Default"][1]-5)
                if event.key == pygame.K_UP:
                    All_Nodes["Imag"] = (All_Nodes["Imag"][0],All_Nodes["Imag"][1]+5)
                    All_Nodes["Default"] = (All_Nodes["Default"][0],All_Nodes["Default"][1]+5)

            # checks if the mouse has been clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        pygame.display.update()

mainmenu()