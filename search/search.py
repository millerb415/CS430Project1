# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu)
from asyncore import loop
from _ast import Str
from Queue import PriorityQueue


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import *
import game
import pacman
import searchAgents

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def getpath (explored, goal):
    from game import Directions
    direction = []
    prev = explored.pop(0)
    for current in explored:
        x, y = prev
        dx, dy = current
        if (x-dx) == 1 and dy-y == 0:
         direction.append(Directions.WEST)
         prev = current
        if (x-dx) == -1 and dy-y == 0:
            direction.append(Directions.EAST)
            prev = current
        if (y-dy) == 1 and dx-x == 0:
            direction.append(Directions.SOUTH) 
            prev = current   
        if (y-dy) == -1 and dx-x == 0:
            direction.append(Directions.NORTH)
            prev = current
    
    
     

    return direction
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
 # function GRAPH-SEARCH(problem, queueing strategy) returns a solution. or failure
   # initialize the fringe using the initial state of problem 
   # done initialize the explored set to be empty 
   # done loop do 
     # done if the fringe is empty then return failure 
     #  choose a  node from the fringe (using queueing strategy)
     #  if node contains goal state then return the corresponding solution 
     #  if node not in the fringe or explored set then
       #   add node to the explored set
        #    expand the chosen node, adding the resulting nodes to the fringe
    
    print problem.getfood(problem.getfood)
    Stack = util.Stack()
    pacMan =  problem
    Stack.push((pacMan.startState, [pacMan.startState]))
    explored = []
 #   print str(Stack.pop())
    goal = pacMan.goal
    while not Stack.isEmpty():
        location , curpath = Stack.pop()
        walls = pacMan.walls
        if location == goal:
            problem._expanded += 1
            curpath.append(location)
            return getpath(curpath, goal)
        already_explored = False;
        for x in explored:
           if x == location:
               already_explored = True
        dx, dy = location                 
        if already_explored == False: 
           problem._expanded += 1   
           explored.append(location)
           pacMan._visitedlist.append(location) 
        if walls[dx][dy + 1] == False and not already_explored:
            curpath.append((dx ,dy+ 1))
            Stack.push(((dx ,dy+ 1),copy(curpath)))
            curpath.pop()
        if walls[dx + 1][dy] == False and not already_explored:
            curpath.append((dx + 1 ,dy))
            Stack.push(((dx + 1 ,dy),copy(curpath)))
            curpath.pop()
        if walls[dx ][dy-1] == False and not already_explored:
            curpath.append((dx ,dy- 1))
            Stack.push(((dx,dy-1), copy(curpath)) )
            curpath.pop()
        if walls[dx -1 ][dy] == False and not already_explored:
            curpath.append((dx-1 ,dy))
            Stack.push(((dx-1,dy),copy(curpath)))
            curpath.pop()
    for x in explored:
        print x
#     
#     return []  
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    pacMan =  problem
    queue.push((pacMan.startState, [pacMan.startState]))
    explored = []
 #   print str(queue.pop())
    goal = pacMan.goal
    while not queue.isEmpty():
        location , curpath = queue.pop()
        walls = pacMan.walls
        if location == goal:
            curpath.append(location)
            problem._expanded += 1
            return getpath(curpath, goal)
        already_explored = False;
        for x in explored:
           if x == location:
               already_explored = True
        dx, dy = location                 
        if already_explored == False:
           problem._expanded += 1    
           explored.append(location)
           pacMan._visitedlist.append(location) 
        if walls[dx][dy + 1] == False and not already_explored:
            curpath.append((dx ,dy+ 1))
            queue.push(((dx ,dy+ 1),copy(curpath)))
            curpath.pop()
        if walls[dx + 1][dy] == False and not already_explored:
            curpath.append((dx + 1 ,dy))
            queue.push(((dx + 1 ,dy),copy(curpath)))
            curpath.pop()
        if walls[dx ][dy-1] == False and not already_explored:
            curpath.append((dx ,dy- 1))
            queue.push(((dx,dy-1), copy(curpath)) )
            curpath.pop()
        if walls[dx -1 ][dy] == False and not already_explored:
            curpath.append((dx-1 ,dy))
            queue.push(((dx-1,dy),copy(curpath)))
            curpath.pop()
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    depth = 0
    
    pacMan =  problem
    queue = util.PriorityQueue()
    queue.push((pacMan.startState, [pacMan.startState]), 0)
    explored = []
 #   print str(queue.pop())
    goal = pacMan.goal
    while not queue.isEmpty():
        location , curpath = queue.pop()
        walls = pacMan.walls
        if location == goal:
            problem._expanded += 1
            curpath.append(location)
            return getpath(curpath, goal)
        already_explored = False;
        for x in explored:
           if x == location:
               already_explored = True
        dx, dy = location                 
        if already_explored == False:
           depth +=1    
           explored.append(location)
           problem._expanded += 1
           pacMan._visitedlist.append(location) 
        if walls[dx][dy + 1] == False and not already_explored:
            curpath.append((dx ,dy+ 1))
           
            queue.push(((dx ,dy+ 1),copy(curpath)), depth )
            curpath.pop()
        if walls[dx + 1][dy] == False and not already_explored:
            curpath.append((dx + 1 ,dy))
            
            queue.push(((dx + 1 ,dy),copy(curpath)), depth)
            curpath.pop()
        if walls[dx ][dy-1] == False and not already_explored:
            curpath.append((dx ,dy- 1))
           
            queue.push(((dx,dy-1), copy(curpath)), depth )
            curpath.pop()
        if walls[dx -1 ][dy] == False and not already_explored:
            curpath.append((dx-1 ,dy))
            
            queue.push(((dx-1,dy),copy(curpath)),  depth)
            curpath.pop()
    util.raiseNotDefined()
def copy(self):
    copy = []
    for i in self:
     copy.append(i)
    return copy
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    depth = 0
    queue = util.PriorityQueue()
    path = util.PriorityQueue()
    
    pacMan =  problem
    path.push([pacMan.startState], (depth + manhattanDistance( pacMan.startState, pacMan.goal )))
    queue.push(pacMan.startState, (depth + manhattanDistance( pacMan.startState, pacMan.goal )))
    explored = []
 #   print str(queue.pop())
    goal = pacMan.goal
    
    while not queue.isEmpty():
        curpath = path.pop()
        depth = depth + 1
        location = queue.pop()
        walls = pacMan.walls
        if location == goal:
            problem._expanded += 1
            curpath.append(location)
            return getpath(curpath, goal)
        already_explored = False;
        for x in explored:
           if x == location:
               already_explored = True
        dx, dy = location                 
        if already_explored == False :
           problem._expanded += 1    
           explored.append(location)
           pacMan._visitedlist.append(location) 
        if walls[dx][dy + 1] == False and not already_explored:
            queue.push((dx ,dy+ 1), (depth + manhattanDistance(goal, (dx,dy+1) )))
            curpath.append((dx ,dy+ 1))
            path.push(copy(curpath), (depth + manhattanDistance(goal, (dx,dy+1) )))
            curpath.pop()
        if walls[dx + 1][dy] == False and not already_explored:
            queue.push((dx+1,dy),(depth + manhattanDistance( goal, (dx+1,dy) )))
            curpath.append((dx + 1,dy))
            path.push(copy(curpath), (depth + manhattanDistance(goal, (dx+1,dy) )))
            curpath.pop()
        if walls[dx ][dy-1] == False and not already_explored:
            queue.push((dx,dy-1), (depth + manhattanDistance(goal, (dx,dy-1) )))
            curpath.append((dx ,dy - 1))
            path.push(copy(curpath), (depth + manhattanDistance(goal, (dx,dy-1) )))
            curpath.pop()
        if walls[dx -1 ][dy] == False and not already_explored:
            queue.push((dx-1,dy), (depth + manhattanDistance(goal, (dx-1,dy) )))
            curpath.append((dx -1,dy))
            path.push(copy(curpath), (depth + manhattanDistance(goal, (dx-1,dy) )))
            curpath.pop()
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
