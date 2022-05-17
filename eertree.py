class ENode():
	'A Node in an Eertree'
	def __init__(self, len=0, sLink = None, content = ""):
		self.dirEdges = dict() # Direct Edges
		self.suffixLink = sLink # SUffix Link / Edges
		self.len = len # Length of the Palindrome Contained
		self.content = content # The Palindrome Contained
	def __str__(self) -> str:
		return self.content
 
class Eertree():
	'Our Eertree'
	def __init__(self) -> None:
		self.nodes = []
		# Two Initial Root Nodes - One with legnth 0 and the other with Length -1
		'''Imaginary Root contains an imaginary string of length -1 which we assume to be None.
		   It has a suffix link towards itself.'''
		self.imgRoot = ENode(len = -1, content = None)
		self.imgRoot.suffixLink = self.imgRoot
		'''Empty Root contains an empty string which is of course of length 0.
		   It has a suffix link towards the imaginary root.'''
		self.emptyRoot = ENode(sLink = self.imgRoot)
 
		# Initialize empty tree
		self.S = [0] # Processed Input String T = [0....n]
		self.maxSufT = self.emptyRoot # Latest Inserted Node in the processed String 

		self.lst = {}
 
	def get_max_suffix_pal(self, startNode: ENode, a: str) -> ENode:
		# We traverse the suffix-palindromes of T in the order of decreasing length.
		# For each palindrome we read its length k and compare T[i-k] against a
		# until we get an equality or arrive at the -1 node.
		while startNode != self.imgRoot and self.S[len(self.S) - startNode.len - 1] != a:
			print("While inserting", a,": ", self.S[len(self.S) - startNode.len - 1])
			if startNode != startNode.suffixLink: # This Detects that we have reached the Imaginary Root
				startNode = startNode.suffixLink
				print('Start Node now is', startNode.content)
		return startNode
 
	def add(self, a) -> bool:
		print("Inserting ", a)
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
 
	def get_sub_palindromes(self, nd, nodesToHere, charsToHere, result):
		#Each node represents a palindrome, which can be reconstructed
		#by the path from the root node to each non-root node.
 
		#Traverse all dirEdges, since they represent other palindromes
		for lnkName in nd.dirEdges:
			nd2 = nd.dirEdges[lnkName] #The lnkName is the character used for this edge
			self.get_sub_palindromes(nd2, nodesToHere+[nd2], charsToHere+[lnkName], result)
 
		#Reconstruct based on charsToHere characters.
		if nd != self.imgRoot and nd != self.emptyRoot: #Don't print for root nodes
			tmp = "".join(charsToHere)
			if nodesToHere[0] == self.emptyRoot: #Even string
				assembled = tmp[::-1] + tmp
			else: #Odd string
				assembled = tmp[::-1] + tmp[1:]
			result.append(assembled)
	def get_height(self):
		h = 0
		a = [self.imgRoot, self.emptyRoot]
		a_bar = [self.imgRoot.content, self.emptyRoot.content]
		self.lst[h] = a_bar
		while True:
			t_bar = []
			t  = []
			for i in a:
				for j in i.dirEdges.values():
					t.append(j)
					t_bar.append(j.content)
			a = t
			a_bar = t_bar
			if a == []:
				break
			h += 1
			self.lst[h] = a_bar
		return h
			
		
				
	def printNodes(self):
		# map(lambda i: print(i.content), self.nodes) 
		# 'map()' Not Working (Using Loop Now)
		for node in self.nodes:
			print('Info for Node:',node.content)
			print('Length:', node.len)
			print('Suffix Links:', node.suffixLink)
			print('Direct Edges:', node.dirEdges,  sep="\n")
 


# print ("Enter the desired string below:")
# string = 'eertree'
# print ("String to be Processed: \"", string, end="\"\n", sep="")
# print ("Processing string...")

# eertree = Eertree()
# for char in string:
# 	eertree.add(char)
# 	print()
# #Traverse tree to find sub-palindromes
# result = []
# eertree.get_sub_palindromes(eertree.imgRoot, [eertree.imgRoot], [], result) #Odd length words
# eertree.get_sub_palindromes(eertree.emptyRoot, [eertree.emptyRoot], [], result) #Even length words

# print ("Processing finished!")
# print ("Number of unique sub-palindromes:", len(eertree.nodes))
# print ("Unique Sub-palindromes:", result)
# # eertree.printNodes()
# # print(eertree.S)

# for i,j in eertree.emptyRoot.dirEdges.items():
# 	print(i,"->",j.content)
# for i,j in eertree.imgRoot.dirEdges.items():
# 	print(i,"->",j.content)

# subtrees = {}
# subtrees['01'] = {}
# subtrees['01'][eertree.emptyRoot] = eertree.emptyRoot.dirEdges
# subtrees['01'][eertree.imgRoot] = eertree.imgRoot.dirEdges
# for lp in range(1,4):
# 	subtrees[str(lp)+str(lp+1)] = {}	
# 	for i in subtrees[str(lp-1)+str(lp)]:
# 		for j,val in subtrees[str(lp-1)+str(lp)][i].items():	
# 			subtrees[str(lp)+str(lp+1)][val] = val.dirEdges
# # subtrees['12'] = {}
# # for i in subtrees['01']:
# # 	for j,val in subtrees['01'][i].items():
# # 		subtrees['12'][val] = val.dirEdges

 
# def getNodes(lvl, subtrees):
# 	return [i.content for i in subtrees[str(lvl)+str(lvl+1)].keys()]
# def getNodes_w_parent(lvl1,lvl2,subtrees):
# 	d = []
# 	for i in subtrees[str(lvl1)+str(lvl2)]:
# 		for j in subtrees[str(lvl1)+str(lvl2)][i]:
# 			d.append((subtrees[str(lvl1)+str(lvl2)][i][j].content, i.content))
# 			if lvl1 == 3:
# 				print(subtrees[str(lvl1)+str(lvl2)][i][j].content, subtrees[str(lvl1)+str(lvl2)][i][j].dirEdges)
# 	return d

# print(getNodes(1,subtrees))
# for i in range(4):
# 	print(str(i)+str(i+1) ,"->", getNodes_w_parent(i,i+1,subtrees))