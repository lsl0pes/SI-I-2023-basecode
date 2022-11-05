from tree_search import *
from cidades import *
from blocksworld import *


def func_branching(connections,coordinates):
    #IMPLEMENT HERE
    pass

class MyCities(Cidades):
    def __init__(self,connections,coordinates):
        super().__init__(connections,coordinates)
        # ADD CODE HERE IF NEEDED

class MySTRIPS(STRIPS):
    def __init__(self,optimize=False):
        super().__init__(optimize)

    def simulate_plan(self,state,plan):
        #IMPLEMENT HERE
        pass

 
class MyNode(SearchNode):
    def __init__(self,state,parent,arg3=None,arg4=None,arg5=None):
        super().__init__(state,parent)
        #ADD HERE ANY CODE YOU NEED

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',optimize=0,keep=0.25): 
        super().__init__(problem,strategy)
        #ADD HERE ANY CODE YOU NEED

    def astar_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        pass


    # remove a fraction of open (terminal) nodes
    # with lowest evaluation function
    # (used in Incrementally Bounded A*)
    def forget_worst_terminals(self):
        #IMPLEMENT HERE
        pass

    # procurar a solucao
    def search2(self):
        #IMPLEMENT HERE
        pass

# If needed, auxiliary functions can be added




