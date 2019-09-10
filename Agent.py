import random_actor

class Agent:
    
    def __init__(self,name,role,location=None):
        self.name     = name      # Name(string of three letters)
        self.role     = role      # Evader or Pursuer('evader' or 'pursuer')
        self.location = location  # Location on Graph(node of the graph)
        
    def get_location(self):
        return self.location
    
    def get_role(self):
        return self.role
    
    def get_name(self):
        return self.name
    
    def set_location(self,location):
        self.location = location
        
    def act(self,world):
        self.location = random_actor.random_actor(world,self) # output from agent-dqn using world model parameters
        