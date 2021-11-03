#######################################################################################################
#IMPORTS
#######################################################################################################

import random

#######################################################################################################
#CLASSES
#######################################################################################################

class Agent():
    """
    A class to represent the agent

    Attributes:
    environment (list): the dimensions of the environment and the quantities of food availiable in each coordinate
    agents (list): the class instances of all other agents
    store (float): the food currently stored by the agent
    cols (int): the number of columns in the environment
    rows (int): the number of rows in the environment
    _x (int): the agent's x coordinate
    _y (int): the agent's y coordinate
    i (int): the agent's id number

    Methods:
    move(): allows the agent to move across the grid
    eat(): allows the agent to eat, at most, 10 pieces of the food at its current location, as well as sicking up food if its had too much
    share_with_neighbours(neighbourhood: int): averages out the food stores of two agents in close proximity as defined by the neighbours parameter
    distance_between(agent: class): calculates the pythagorean distance between two agents
    set_x(value: int): sets the x coordinate to a new value
    set_y(value: int): sets the y coordinate to a new value
    get_x(): gets the x coordinate
    get_y(): gets the y coordinate
    """
    
    def __init__(self, i, environment, agents, cols, rows, x= None, y=None):
        """
        constructs all of the agent's necessary attributes

        Parameters:
        environment (list): the dimensions of the environment and the quantities of food availiable in each coordinate
        agents (list): the class instances of all other agents
        store (float): the food currently stored by the agent
        cols (int): the number of columns in the environment
        rows (int): the number of rows in the environment
        x (int): the agent's x coordinate
        y (int): the agent's y coordinate
        """

        #stores the size of the environment allowing the agents to scale to the environment
        self.environment = environment

        #stores the current agents
        self.agents = agents

        #how much food the agent has stored
        self.store = 0

        #how many columns are in the environment
        self.cols = cols

        #how many rows are in the environment
        self.rows = rows

        #sets randomnly generated values for the x and y coords if not set from scraped data
        if (x==None):
            
            self._x = random.randint(0,len(self.environment))
        else:
            self._x = x
        
        if (y==None):
            self._y = random.randint(0,len(self.environment[0]))
        else:
            self._y=y
        
        self.i = i
    
    def __str__(self):
        """
        default string representation changed
        """

        return "Id = {} Location is x:{} and y:{}. Food stored is {}".format(self.i, self._x,self._y,self.store)
    
    def move(self):
        """
        allows the agent to move across the grid
        """

        #agent moves right on the x-axis 1 step if random number less than 0.5
        if random.random() < 0.5:
            self._x = (self._x+1) % self.cols
        else:
            #agent moves left on the x-axis 1 step if random number greater than 0.5
            self._x = (self._x-1) % self.cols
        
        #agent moves up the y-axis 1 step if random number less than 0.5
        if random.random() < 0.5:
            self._y = (self._y+1) % self.rows
        else:
            #agent moves down the y-axis 1 step if random number greater than 0.5
            self._y = (self._y-1) % self.rows
            
    def eat(self):

        """
        allows the agent to eat, at most, 10 pieces of the food at its current location, as well as sicking up food if its had too much
        """

        #adds 10 to agent's store if more than 10 pieces left at the current location
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        
        #if less than 10 pieces left at the current location, the agent eats them all
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
            
        #sicks up the store in a location if more than 100 units eaten
        if self.store>=100:
            self.environment[self.y][self.x] += self.store
            self.store -= self.store
    
    def share_with_neighbours(self, neighbourhood):
        """
        averages out the food stores of two agents in close proximity

        Parameters:
        neigbourhood (int): the largest distance in which 2 agents will be considered to be neighbours
        """

        #iterates through all agents
        for agent in self.agents:
            
            #calxcs pythag distance
            distance = self.distance_between(agent)
            
            if distance <= neighbourhood:
                
                avg = (self.store + agent.store)/2

                #sest both agent's stores to the average of both stores added together
                self.store = avg
                agent.store = avg
               
    def distance_between(self, agent):
        """
        calculates the pythagorean distance between two agents

        Parameters:
        agent (class): the agent which the current agent will have its distance measured against
        """

        #the square root of the difference between both x and y coords squared
        return ((((self.x-agent.x)**2)+((self.y-agent.y)**2))**0.5)

    def set_x(self, value):
        """
        sets the x coordinate to a new value
        """
        self._x = value
        
    def set_y(self, value):
        """
        sets the y coordinate to a new value
        """
        self._y = value
    
    def get_x(self):
        """
        gets the x coordinate
        """
        return self._x
        
    def get_y(self):
        """
        gets the y coordinate
        """
        return self._y
    
    #ensures that the x and y coords as private variables will be set and get through their respective methods
    x = property(get_x, set_x,doc = "The agent's x coordinate")
    y = property(get_y, set_y,doc = "The agent's y coordinate")
    

    
    
    
    
    
    
    
    
    
    