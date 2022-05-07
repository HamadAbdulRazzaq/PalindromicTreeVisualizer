class ENode():
	'A Node in an Eertree'
	def __init__(self, len=0, sLink = None):
		self.dirEdges = dict() 
		self.suffixLink = sLink
		self.len = len

 
class Eertree():
	'Our Eertree'
	def __init__(self) -> None:
		self.nodes = []
		# two initial root nodes
		self.imgRoot = ENode(len = -1); self.imgRoot.suffixLink = self.imgRoot;
		self.emptyRoot = ENode(len = 0, sLink = self.imgRoot)
 
		# Initialize empty tree
		self.S = [0] # accumulated input string, T=S[0..n]
		self.maxSufT = self.emptyRoot # maximum suffix of tree T
 
	def get_max_suffix_pal(self, startNode: ENode, a: str) -> ENode:
		# We traverse the suffix-palindromes of T in the order of decreasing length.
		# For each palindrome we read its length k and compare T[i-k] against a
		# until we get an equality or arrive at the -1 node.
		while startNode != self.imgRoot and self.S[len(self.S) - startNode.len - 1] != a:
			if startNode != startNode.suffixLink: #Prevent infinte loop
				startNode = startNode.suffixLink
		return startNode
 
	def add(self, a) -> bool:
		# We need to find the maximum suffix-palindrome P of T.
		# Start by finding maximum suffix-palindrome Q of T.
		# To do this, we traverse the suffix-palindromes of T
		# in the order of decreasing length, starting with maxSuf(T)
		Q = self.get_max_suffix_pal(self.maxSufT, a)
 
		# We check Q to see whether it has an outgoing edge labeled by a.
		createANewNode = not a in Q.dirEdges
 
		if createANewNode:
			if Q.len == -1:
				P = ENode(len = Q.len + 2, sLink = self.emptyRoot)
				# # if P = a, create the suffix suffixLink (P,0)
				# P.suffixLink = self.emptyRoot
			else:
				P = ENode(len = Q.len + 2, sLink = self.get_max_suffix_pal(Q.suffixLink, a).dirEdges[a])
				# It remains to create the suffix suffixLink from P if |P|>1. Just
				# continue traversing suffix-palindromes of T starting with the suffix 
				# suffixLink of Q.
			self.nodes.append(P)
 
			# create the edge (Q,P)
			Q.dirEdges[a] = P
 
		#P becomes the new maxSufT
		self.maxSufT = Q.dirEdges[a]
 
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
		if id(nd) != id(self.imgRoot) and id(nd) != id(self.emptyRoot): #Don't print for root nodes
			tmp = "".join(charsToHere)
			if id(nodesToHere[0]) == id(self.emptyRoot): #Even string
				assembled = tmp[::-1] + tmp
			else: #Odd string
				assembled = tmp[::-1] + tmp[1:]
			result.append(assembled)
 
 
if __name__== "__main__":

	print ("Enter the desired string below:")
	string = str(input())
	print ("String to be Processed: \"", string, end="\"\n", sep="")
	print ("Processing string...")

	eertree = Eertree()
	for char in string:
		eertree.add(char)
 
	print ("Processing finished!")
	print ("Number of unique sub-palindromes:", len(eertree.nodes))
 
	#Traverse tree to find sub-palindromes
	result = []
	eertree.get_sub_palindromes(eertree.imgRoot, [eertree.imgRoot], [], result) #Odd length words
	eertree.get_sub_palindromes(eertree.emptyRoot, [eertree.emptyRoot], [], result) #Even length words
	print ("Unique Sub-palindromes:", result)