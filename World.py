from networkx import nx
import random
import Agent

class World:
    
    def __init__(self,n,m,agents):
        self.graph  = nx.triangular_lattice_graph(n,m) # NetworkX grpah defining the world space
        self.agents = agents                           # List of agents in the world
        # location of the agents are set randomly on the graph
        for agent in agents:
            t = random.choice(range(0,len(self.graph.nodes())))
            agent.set_location( list( self.graph.nodes() )[t] )

    def get_graph(self):
        return self.graph
                    
    def add_agent(self,agent):
        self.agents.append(agent)            # Add a new agent in the world
        # Set its location randomly on the graph
        t = random.choice(range(0,len(self.graph.nodes())))
        agent.set_location(list(G.nodes())[t])
        
    def next_state(self):
        for agent in self.agents:
            agent.act(self) # Sending the world and location
                    