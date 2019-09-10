from networkx import nx
import random
import importlib
import Agent

def random_actor(world,agent):
    # Randomly selects an action for an agent for demenstration purpose
    neighbors = list(world.get_graph()[agent.get_location()])
    n = len(neighbors)
    t = random.choice(range(0,n))
    
    return neighbors[t]