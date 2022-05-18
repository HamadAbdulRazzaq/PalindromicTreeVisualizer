# Data Structures II Project - Palindromic Tree (eertree)
Palindromic Trees (also know as eertree) are efficient data structures which can be used to store all the subpalindromes in a string in just $O(nlog(\Sigma) ))$ where:
- $n:$ Size of the input string.
- $\Sigma :$ Size of the Alphabet <br/>
In English, the Size of the alphabet is 26 which is $O(1)$ so in that case the complexity becomes $O(n)$
## Applications
A Palindromic Tree can be used for many problems regarding the palindromes such as:
- Finding the sub-palindromes inside a string
- Finding the longest palindrome inside the string
- Finding all unique palindromes <br/>
For more informtation regarding the algorithm of constructing eertree, refer to [this link](https://medium.com/@alessiopiergiacomi/eertree-or-palindromic-tree-82453e75025b)
## Our Application
Our Project aimed at visualizing the construction of the palindromic tree for any given input string. It is a step-by-step colored visualization which insert each nodes and shows all steps by coloring.
## How to Operate
The file [eertree.py](eertree.py) handles all the eertree's opeartions and also contains class of the nodes contained in the eertree. Running the file [Display.py](Display.py) will open the GUI. The pre-requisites for running the file is that you should have pygame and the pygame_menu modules installed. With that said, follow the following steps for visualization:
- Type the word that you want to enter. The word would be shown on the GUI. Once you are done entering the string, press Enter.
- From here with every press of space bar key, we increment a step in constructing the Palindromic Tree.
- The red node marks where we stand at and the pink node marks where the traversal begins.
- Once the string is fully processed, the whole palindromic tree is displayed on the GUI
- The Green edges are the Suffix Links and the white edges are the labelled edges
- To scroll, you can use the left, right, down and up keys to move the tree.
- Pressing the escape key at any point will close the application. The application can also be closed by pressing the cross on the top-right.

## References
- [https://arxiv.org/pdf/1506.04862.pdf](https://arxiv.org/pdf/1506.04862.pdf)
- [https://medium.com/@alessiopiergiacomi/eertree-or-palindromic-tree-82453e75025b](https://medium.com/@alessiopiergiacomi/eertree-or-palindromic-tree-82453e75025b)
- [https://rosettacode.org/wiki/Eertree#Python](https://rosettacode.org/wiki/Eertree#Python)
- [https://iq.opengenus.org/palindromic-tree-eertree/](https://iq.opengenus.org/palindromic-tree-eertree/)