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

    Stack = util.Stack()
    pacMan =  problem
    Stack.push((pacMan.startState,[], 0))
    explored = []
    goal = pacMan.goal
    while not Stack.isEmpty():
        location , curpath , cost = Stack.pop()
        if problem.isGoalState(location): 
            return curpath
        already_explored = False;
        for x in explored:
           if x == location:
               already_explored = True
        dx, dy = location  
        if not already_explored:
         explored.append(location)
         for cloc, cdir, ccost in problem.getSuccessors(location): 
            ccopy= copy(curpath)
            ccopy.append(cdir)
            ccost += cost  
            Stack.push((cloc, ccopy, ccost))             
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    Queue = util.Queue() 
    Queue.push(( problem.getStartState(),[], 0))
    explored = []
    while not Queue.isEmpty():
        state, curpath, cost = Queue.pop()
        if problem.isGoalState(state):
            return curpath
        if state not in explored:
         explored.append(state)
         for nextState, path, costToNext in problem.getSuccessors(state): 
            cpath=copy(curpath)
            cpath.append(path)
            costToNext += cost  
            Queue.push((nextState, cpath, costToNext))
    util.raiseNotDefined()

    
    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***" 
    pacMan =  problem
    Queue = util.PriorityQueue()
    Queue.push((pacMan.startState,[], 0), 0)
    explored = []
    goal = pacMan.goal
    while not Queue.isEmpty():
        location , curpath , cost = Queue.pop()
        if problem.isGoalState(location):
            return curpath
        already_explored = False;
        for x in explored:
           if x == location:
               already_explored = True
        dx, dy = location  
        if not already_explored:
         explored.append(location)
         for cloc, cdir, ccost in problem.getSuccessors(location): 
            ccopy= copy(curpath)
            ccopy.append(cdir)
            ccost += cost  
            Queue.push((cloc, ccopy, ccost), ccost)
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
    pacMan =  problem
    Queue = util.PriorityQueue()   
    startState = problem.getStartState()
    heur = heuristic(startState,problem)
    Queue.push((pacMan.getStartState(),[], 0), 0 + heur )
    explored = []
    while not Queue.isEmpty():
        state , curpath , cost = Queue.pop()
        if problem.isGoalState(state):
            return curpath
        if state not in explored:
         explored.append(state)
         for nextState, path, costToNext in problem.getSuccessors(state): 
            cpath=copy(curpath)
            cpath.append(path)
            costToNext += cost  
            Queue.push((nextState, cpath, costToNext), costToNext + heuristic(nextState, problem))
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
