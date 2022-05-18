import pygame
import pygame_menu
import pygame.gfxdraw
from eertree import *
print ("Enter the desired string below:")
string = 'racecar'
print ("String to be Processed: \"", string, end="\"\n", sep="")
print ("Processing string...")

eertree = Eertree()
# for char in string:
# 	eertree.add(char)

#Traverse tree to find sub-palindromes
result = []
eertree.get_sub_palindromes(eertree.imgRoot, [eertree.imgRoot], [], result) #Odd length words
eertree.get_sub_palindromes(eertree.emptyRoot, [eertree.emptyRoot], [], result) #Even length words

print ("Processing finished!")
print ("Number of unique sub-palindromes:", len(eertree.nodes))
print ("Unique Sub-palindromes:", result)
# eertree.printNodes()
# print(eertree.S)

for i,j in eertree.emptyRoot.dirEdges.items():
	print(i,"->",j.content)
for i,j in eertree.imgRoot.dirEdges.items():
	print(i,"->",j.content)

print("Height:", eertree.get_height())
f = eertree.get_height()
subtrees = {}
subtrees['01'] = {}
subtrees['01'][eertree.emptyRoot] = eertree.emptyRoot.dirEdges
subtrees['01'][eertree.imgRoot] = eertree.imgRoot.dirEdges
for lp in range(1,f):
	subtrees[str(lp)+str(lp+1)] = {}	
	for i in subtrees[str(lp-1)+str(lp)]:
		for j,val in subtrees[str(lp-1)+str(lp)][i].items():	
			subtrees[str(lp)+str(lp+1)][val] = val.dirEdges
# subtrees['12'] = {}
# for i in subtrees['01']:
# 	for j,val in subtrees['01'][i].items():
# 		subtrees['12'][val] = val.dirEdges

 
def getNodes(lvl, subtrees):
	return [i.content for i in subtrees[str(lvl)+str(lvl+1)].keys()]
def getNodes_w_parent(lvl1,lvl2,subtrees):
	d = []
	for i in subtrees[str(lvl1)+str(lvl2)]:
		for j in subtrees[str(lvl1)+str(lvl2)][i]:
			d.append((subtrees[str(lvl1)+str(lvl2)][i][j].content, i.content))
			# if lvl1 == 3:
				# print(subtrees[str(lvl1)+str(lvl2)][i][j].content, subtrees[str(lvl1)+str(lvl2)][i][j].dirEdges)
	return d

# print(getNodes(1,subtrees))
for i in range(f):
	print(str(i)+str(i+1) ,"->", getNodes_w_parent(i,i+1,subtrees))
columns = [0 for i in range(7)]
def calc_pad(node: ENode, bool, T, s=0):
    a = 35
    if bool:
        a = 5
    else:
        a = 0
    # if len(list(node.dirEdges.keys())) == 1:
    #     return (0, )    
    
    
    return a



def parent_childs(T: Eertree, node):
    if node==T.emptyRoot.content:
        return(T.emptyRoot.content, [i.content for i in T.emptyRoot.dirEdges.values()])
    elif node==T.imgRoot.content:
        return(T.imgRoot.content, [i.content for i in T.imgRoot.dirEdges.values()])
    else:
        a = len(node)
        if a%2 == 0:
            dest = T.emptyRoot
            temp = a//2 - 1
            # print(temp)
            for i in range(temp+1):
                # print("Node:",dest)
                # print("Node Value:", dest.content)
                dest = dest.dirEdges[node[temp]]
                temp -= 1
            # print("Node:",dest)
            # print("Node Value:", dest.content)
            return (dest.content, [j.content for j in dest.dirEdges.values()])
        else:
            dest = T.imgRoot
            temp = a//2 
            # print(temp)
            for i in range(temp+1):
                # print("Node:",dest)
                # print("Node Value:", dest.content)
                dest = dest.dirEdges[node[temp]]
                temp -= 1
            # print("Node:",dest)
            # print("Node Value:", dest.content)
            return (dest.content, [j.content for j in dest.dirEdges.values()])

def pad_it(pdg, cond, offset):
    print('cond: ', cond )
    print('offset: ', offset )
    print()
    for i in pdg:
        if pdg[i] >= cond:
            pdg[i] += offset


    # if i==2:
    #     break
# print(parent_childs(eertree, "ee"))
# print(parent_childs(eertree, 't'))
def set_col_width(pdg:dict, size):
    col = {}
    try:
        d = max(list(pdg.values()))
    except:
        d = 0
    for i in range(d+1):
        temp = []
        for j in pdg:
            if pdg[j] == i:
                if j == None:
                    temp.append(2)
                elif j == "":
                    temp.append(1)
                else:
                    temp.append(len(j))
        try:
            col[i] = (((max(temp)//2)+1)*size)
        except:
            col[i] = 100
    return col
pdg = {}
subtrees = {}
padding = {}
edges = []
suffix_edges = []
col_width = {}

def update(eertree, pdg, subtrees, padding, edges, suffix_edges, col_width):
    # for i,j in eertree.emptyRoot.dirEdges.items():
    #     print(i,"->",j.content)
    # for i,j in eertree.imgRoot.dirEdges.items():
    #     print(i,"->",j.content)

    # print("Height:", eertree.get_height())
    f = eertree.get_height()
    
    subtrees['01'] = {}
    subtrees['01'][eertree.emptyRoot] = eertree.emptyRoot.dirEdges
    subtrees['01'][eertree.imgRoot] = eertree.imgRoot.dirEdges
    for lp in range(1,f):
        subtrees[str(lp)+str(lp+1)] = {}	
        for i in subtrees[str(lp-1)+str(lp)]:
            for j,val in subtrees[str(lp-1)+str(lp)][i].items():	
                subtrees[str(lp)+str(lp+1)][val] = val.dirEdges
    padding[0] = {}
    pd = calc_pad(eertree.emptyRoot,True, eertree, 0)
    # print("pd", pd)
    padding[0][eertree.emptyRoot] = pd
    i = 0
    i = 0
    if f == 0:
        d = getNodes(i,subtrees)
        a = 0
        for j in d:
            pdg[j] = a
            a += 2
    while i<f:
        # print("here cones")
        d = getNodes(i,subtrees)
        if i ==0:
            a = 0
            for j in d:
                pdg[j] = a
                a += 2
        for j in d:
            pc = parent_childs(eertree, j)
            # print("pc", pc)
            padding = (len(pc[1])-1)
            previous = pdg[pc[0]]
            if padding > 0:
                pad_it(pdg, previous, padding)
            y = -(len(pc[1])//2)
            for x in pc[1]:
                pdg[x] = pdg[j] + 2*y
                y += 1
        i += 1
    # print("pdg:", pdg)
    # print(eertree.lst)

    col_width = set_col_width(pdg, 60)
    # print(col_width)
    nds = [i.content for i in eertree.nodes] + ['', None]
# print(z)
    for i in eertree.nodes:
        if i.suffixLink != None:
            if (i.content, i.suffixLink.content) not in suffix_edges:
                suffix_edges.append((i.content, i.suffixLink.content))

    for z in nds:
        tmp = parent_childs(eertree, z)
        # print(tmp)
        edges.extend([(tmp[0], tmp[1][j]) for j in range(len(tmp[1]))])
    print('suffix_edges', suffix_edges)


update(eertree, pdg, subtrees, padding, edges, suffix_edges, col_width)

print('edges', edges)
col_width = set_col_width(pdg, 60)
print('col_width', col_width)






pygame.init()
width = 1200
height = 650
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
pink = (252,15,192)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Palindromic Tree")
screen.fill(black)
# def prnt(Widget, Menu,):
#     global cnt
#     print(cnt)
def add3(self, startNode, a, c_node, Q):
    df = False
    if startNode != self.imgRoot and self.S[len(self.S) - startNode.len - 1] != a:
        df = True
        print("While inserting", a,": ", self.S[len(self.S) - startNode.len - 1])
        if startNode != startNode.suffixLink: # This Detects that we have reached the Imaginary Root
            df = True
            startNode = startNode.suffixLink
            print('Start Node now is', startNode.content)
    if not(df):
        if startNode == eertree.imgRoot and Q.len == -1:
            c_node.suffixLink = eertree.emptyRoot
        else:
            c_node.suffixLink = startNode.dirEdges[a]
        df = False
        # P becomes the new maxSufT
        self.maxSufT = Q.dirEdges[a]
        print(" updated maxSufT:", self.maxSufT.content)
		#Store accumulated input string
        self.S.append(a)
        print('Thiss Called')
    return (startNode, df)
def add1(self, startNode, a):
    df = False
    if startNode != self.imgRoot and self.S[len(self.S) - startNode.len - 1] != a:
        df = True
        print("While inserting", a,": ", self.S[len(self.S) - startNode.len - 1])
        if startNode != startNode.suffixLink: # This Detects that we have reached the Imaginary Root
            df = True
            startNode = startNode.suffixLink
            print('Start Node now is', startNode.content)
    return (startNode, df)
def add2(self, Q, a):
    createANewNode = not a in Q.dirEdges
    print(createANewNode)
    if createANewNode:
        if Q.len == -1: # If Q is ImagRoot
            P = ENode(len = Q.len + 2, sLink = None, content = a)
				# # if P = a, create the suffix suffixLink (P,0)
				# P.suffixLink = self.emptyRoot
        else:
            P = ENode(len = Q.len + 2, sLink = None, content = f"{a}{Q.content}{a}")
				# It remains to create the suffix suffixLink from P if |P|>1. Just
				# continue traversing suffix-palindromes of T starting with the suffix 
				# suffixLink of Q.
        self.nodes.append(P)

			# create the edge (Q,P)
        Q.dirEdges[a] = P
        return (Q.suffixLink,P)
def add(self, a) -> bool:
		# print("Inserting ", a)
		# We need to find the maximum suffix-palindrome P of T.
		# Start by finding maximum suffix-palindrome Q of T.
		# To do this, we traverse the suffix-palindromes of T
		# in the order of decreasing length, starting with maxSuf(T)
		print("maxSufT:", self.maxSufT.content)
		Q = self.get_max_suffix_pal(self.maxSufT, a)
		print('Q:',Q.content)
		# We check Q to see whether it has an outgoing edge labeled by a.
		createANewNode = not a in Q.dirEdges
		print(createANewNode)
		if createANewNode:
			if Q.len == -1: # If Q is ImagRoot
				P = ENode(len = Q.len + 2, sLink = self.emptyRoot, content = a)
				# # if P = a, create the suffix suffixLink (P,0)
				# P.suffixLink = self.emptyRoot
			else:
				P = ENode(len = Q.len + 2, sLink = self.get_max_suffix_pal(Q.suffixLink, a).dirEdges[a], content = f"{a}{Q.content}{a}")
				# It remains to create the suffix suffixLink from P if |P|>1. Just
				# continue traversing suffix-palindromes of T starting with the suffix 
				# suffixLink of Q.
			self.nodes.append(P)
 
			# create the edge (Q,P)
			Q.dirEdges[a] = P
 
		# P becomes the new maxSufT
		self.maxSufT = Q.dirEdges[a]
		print(" updated maxSufT:", self.maxSufT.content)
 
		#Store accumulated input string
		self.S.append(a)
 
		return createANewNode
def mainmenu():
    stage1 = False
    stage2 = False
    stage3 = False
    stage4 = False
    stage5 = False

    global col_width
    xoff = 0
    yoff = 0
    edges_Rect = {}
    nodes_Rect = {}
    closed = False 
    traversed = []
    on_screen = ""
    center_offset = (240, 120)
    a = pygame_menu.pygame_menu.widgets.ScrollBar(500, (0,100),orientation="orientation-vertical")  #Scroll bar
    # a.add_draw_callback(prnt)
    font_size = 60
    imag_root_node = pygame.image.load("Imaginary Root Node.png")
    dft_root_node = pygame.image.load("Default Root Node.png")
    All_Nodes = {"Imag":(3*width/4 - imag_root_node.get_rect().w/2, 50), "Default": (width/4 - dft_root_node.get_rect().w/2,50)}
    bgt = 0
    idx = 0
    string_input = False
    step = 0
    current_node = None
    P = None
    Q = None
    while not(closed):
        center_offset = (240, 120)
        screen.fill(black)
        font = pygame.font.SysFont('consolas', font_size)
        # x_1 = All_Nodes["Default"][0] + dft_root_node.get_rect().w/2
        # y_1 = All_Nodes["Default"][1] + dft_root_node.get_rect().h
        # pygame.draw.line(screen, white, (x_1,y_1), (x_1-100,y_1+100))
        # pygame.draw.line(screen, white, (x_1,y_1), (x_1+100,y_1+100))
        # vb = pygame.Rect(300-150,300-30,font_size*5,font_size)
        # text = font.render("", True, white)
        # textRect = text.get_rect()
        # textRect.center = (300,300)
        # screen.blit(text, textRect)
        # pygame.gfxdraw.rectangle(screen, vb, white)
        # screen.blit(line_temp, (20,20))
        # cnt += 1
        # image = pygame.transform.scale(image, (40,40))
        # FOR COLUMN ONE
        c0s = 100
        r0 = 200
        roff = 80
        lgt = 0
        
        strg = ''
        # print(pdg)
        for i in pdg:
            if True:
                if i == "":
                    lgt = 1
                    strg = '0'
                elif i == None:
                    lgt = 2
                    strg = '-1'
                else:
                    lgt = pdg[i]
                    strg = i
                hgt = 0
                for j in eertree.lst:
                    if i in eertree.lst[j]:
                        hgt = j
                        break
                r0 += 200*(hgt)
                for x in range(pdg[i]):
                    c0s += col_width[x]
                # if strg == '-1':
                #     print(strg, pdg[i], c0s)
                c0e = c0s + col_width[pdg[i]]
                c0c = (c0s + c0e)/2
                
                text = font.render(strg, True, white)
                textRect = text.get_rect()
                textRect.center = (c0c, r0+30)
                textRect.x += xoff
                textRect.y += yoff
                # print( r0 + font_size/2 ,c0s+col_width[pdg[i]])
                # textRect.center = (col_width[pdg[i]] - ((lgt//2)+1)*30 ,col_width[pdg[i]], col_width[pdg[i]] + ((lgt//2)+1)*30)
                screen.blit(text, textRect)
                vb = pygame.Rect(textRect.x-5, textRect.y-1, textRect.w+10, textRect.h+2)
                if i == eertree.maxSufT.content:
                    pygame.gfxdraw.rectangle(screen, vb, pink)    
                else:
                    pygame.gfxdraw.rectangle(screen, vb, white)
                if current_node == None:
                    pass
                elif current_node.content == i:
                    pygame.gfxdraw.rectangle(screen, vb, ((255,0,0)))    
                elif i != eertree.maxSufT.content:
                    pygame.gfxdraw.rectangle(screen, vb, white)
                
                # traversed += i
                # pygame.draw.line(screen,white, (c0s+xoff,r0+yoff), (c0s+xoff,r0+1000+yoff))
                # pygame.draw.line(screen,white, (c0e+xoff,r0+yoff), (c0e+xoff,r0+1000+yoff))
                # pygame.draw.line(screen,(255,0,0), (c0c+xoff,r0+yoff), (c0c+xoff,r0+1000+yoff))
                # pygame.draw.line(screen,(0,255,0), (0+xoff,r0+30+yoff), (1000+xoff,r0+30+yoff))
                
                # print((c0s + (col_width[pdg[i]] - textRect.x),r0,col_width[pdg[i]],r0+textRect.y))
                c0s = 200
                r0 = 200
            nodes_Rect[i] = vb
        a = False
        # print([[i.x, i.y] for i in nodes_Rect.values()])
        # print(edges)
        if bgt == 3000:
            pygame.draw.line(screen,white, (100,100), (2000,2000))
        for i,j in edges:
            x1, y1 = nodes_Rect[i].x + nodes_Rect[i].w/2 , nodes_Rect[i].y + nodes_Rect[i].h 
            x2, y2 = nodes_Rect[j].x + nodes_Rect[j].w/2, nodes_Rect[j].y
            pygame.draw.line(screen,white, (x1,y1), (x2,y2))
            text = font.render(j[0], True, red)
            textRect = text.get_rect()
            textRect.center = ((x1+x2)/2, (y1+y2)/2)
            screen.blit(text, textRect)
        for i,j in suffix_edges:
            x1, y1 = nodes_Rect[i].x + nodes_Rect[i].w/2 , nodes_Rect[i].y 
            x2, y2 = nodes_Rect[j].x + nodes_Rect[j].w/2, nodes_Rect[j].y + nodes_Rect[j].h 
            pygame.draw.line(screen, (0,255,0), (x1,y1), (x2,y2))
        x1, y1 = nodes_Rect[''].x + nodes_Rect[''].w , nodes_Rect[''].y + nodes_Rect[''].h/2
        x2, y2 = nodes_Rect[None].x , nodes_Rect[None].y + nodes_Rect[None].h/2
        pygame.draw.line(screen, (0,255,0), (x1,y1), (x2,y2))
        x1, y1 = nodes_Rect[None].x + nodes_Rect[None].w/2  , nodes_Rect[None].y
        x2, y2 = x1, y1 - 30
        x3, y3 = x2 + 60, y2 
        x4, y4 = x3, y3 + 60
        x5, y5 = x4 - 24, y4
        pygame.draw.line(screen, (0,255,0), (x1,y1), (x2,y2))
        pygame.draw.line(screen, (0,255,0), (x2,y2), (x3, y3))
        pygame.draw.line(screen, (0,255,0), (x3,y3), (x4,y4))
        pygame.draw.line(screen, (0,255,0), (x4,y4), (x5,y5))
        # print(edges)
        tmp_rect = pygame.Rect(0,0,1200,r0/2*1.5)
        pygame.draw.rect(screen, black, tmp_rect)
        pygame.gfxdraw.rectangle(screen, tmp_rect, white)


        text = font.render('t', True, red)
        textRect = text.get_rect()
        textRect.center = (600, 30)
        screen.blit(text, textRect)
        text = font.render('r', True, (0,255,0))
        textRect = text.get_rect()
        textRect.center = (560, 30)
        screen.blit(text, textRect)
        text = font.render('r', True, (0,255,0))
        textRect = text.get_rect()
        textRect.center = (640, 30)
        screen.blit(text, textRect)
        text = font.render('e', True, (252,15,192))
        textRect = text.get_rect()
        textRect.center = (520, 30)
        screen.blit(text, textRect)
        text = font.render('e', True, (252,15,192))
        textRect = text.get_rect()
        textRect.center = (680, 30)
        screen.blit(text, textRect)
        text = font.render('e', True, (0,0,255))
        textRect = text.get_rect()
        textRect.center = (480, 30)
        screen.blit(text, textRect)
        text = font.render('e', True, (0,0,255))
        textRect = text.get_rect()
        textRect.center = (720, 30)
        screen.blit(text, textRect)
        if not(string_input):
            text = font.render('Input: ', True, (0,0,255))
            textRect = text.get_rect()
            textRect.center = (120,120)
            screen.blit(text, textRect)
            
            for i in on_screen:
                text = font.render(i, True, (252,15,192))
                textRect = text.get_rect()
                textRect.center = center_offset
                screen.blit(text, textRect)
                center_offset = (center_offset[0]+40, center_offset[1])
        else:
            text = font.render('Processed: ', True, (0,0,255))
            textRect = text.get_rect()
            textRect.center = (180,120)
            screen.blit(text, textRect)
            center_offset = (360,120)
            for i in on_screen[:idx]:
                text = font.render(i, True, (252,15,192))
                textRect = text.get_rect()
                textRect.center = center_offset
                screen.blit(text, textRect)
                center_offset = (center_offset[0]+40, center_offset[1])
            













        # text = font.render("John Nash's Demon", True, (255,255,255))
        # textRect = text.get_rect()
        # textRect.center = (320, 90)
        # screen.blit(text, textRect)
        # screen.blit(imag_root_node, All_Nodes["Imag"])
        # screen.blit(dft_root_node, All_Nodes["Default"])
        # a.draw(screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
                yoff += 1
                All_Nodes["Imag"] = (All_Nodes["Imag"][0],All_Nodes["Imag"][1]-0.5)
                All_Nodes["Default"] = (All_Nodes["Default"][0],All_Nodes["Default"][1]-0.5)
        if keys[pygame.K_UP]:
                yoff -= 1
                All_Nodes["Imag"] = (All_Nodes["Imag"][0],All_Nodes["Imag"][1]+0.5)
                All_Nodes["Default"] = (All_Nodes["Default"][0],All_Nodes["Default"][1]+0.5)
        if keys[pygame.K_LEFT]:
            xoff -= 1
            All_Nodes["Imag"] = (All_Nodes["Imag"][0]-0.5,All_Nodes["Imag"][1])
            All_Nodes["Default"] = (All_Nodes["Default"][0]-0.5,All_Nodes["Default"][1])
        if keys[pygame.K_RIGHT]:
            xoff += 1
            All_Nodes["Imag"] = (All_Nodes["Imag"][0]+0.5,All_Nodes["Imag"][1])
            All_Nodes["Default"] = (All_Nodes["Default"][0]+0.5,All_Nodes["Default"][1])
        for event in pygame.event.get():
            # if event.type == pygame.K_a:
            #     print(event.type)
            if (event.type == pygame.QUIT):
                closed = True
            if event.type == pygame.KEYDOWN:
                asb = pygame.key.name(event.key)
                if asb.isalnum() and len(asb) == 1:
                    on_screen += asb
                if event.key == pygame.K_RETURN:
                    string_input = True
                    string = on_screen
                    stage1 = True
                if event.key == pygame.K_SPACE and string_input:
                    if idx <= len(string):
                        if stage1:
                            if step == 0:
                                idx += 1
                                current_node = eertree.maxSufT
                                if idx > len(string):
                                    current_node = None
                                    stage1 = False
                                step += 1
                            else:
                                d1 = add1(eertree, current_node , string[idx-1])
                                current_node = d1[0]
                                # print(d1[1], current_node.content)
                                if d1[1] == False:
                                    Q = current_node
                                    stage1 = False
                                    stage2 = True
                            print('stage 1')
                        elif not(stage1) and stage2:
                            print("here")
                            dm = add2(eertree, d1[0], string[idx-1])
                            current_node = dm[0]
                            P = dm[1]
                            stage2 = False
                            stage3 = True
                            print('stage 2')
                        elif not(stage1 or stage2) and stage3:
                            ds2 = add3(eertree, current_node, string[idx-1], P, Q)
                            current_node = ds2[0]
                            if not(ds2[1]):
                                stage1 = True
                                stage3 = False
                                step = 0
                                current_node = None
                            print('stage 3')
                    # elif idx >=  len(string):
                    #     print("wtf?")
                    #     stage1 = False
                    #     stage2 = False
                    #     stage3 = False
                    #     stage4 = False
                        
                        update(eertree, pdg, subtrees, padding, edges, suffix_edges, col_width)
                        col_width = set_col_width(pdg, 60)
                    
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
        # if bgt == 3000:
        #     bgt = 0
        #     idx += 1
        

        pygame.display.update()
        # pygame.time.delay(1000)

mainmenu()