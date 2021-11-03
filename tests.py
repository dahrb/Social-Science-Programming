#######################################################################################################
#IMPORTS
#######################################################################################################

import unittest
import model
import agentframework

#######################################################################################################
#TEST CLASSES
#######################################################################################################

class Tests(unittest.TestCase):
    """
    This class intiates 5 unit tests for the agentframework class

    Tests:
    test_eat_1(): tests if environment > 10 that 10 will be deducted from the environment and added to the store
    test_eat_2(): tests if environment  < 10 that number will be deducted from the environment and added to the store
    test_eat_3(): tests if sicking after >=100 in store functions correctly
    test_share(): tests if sharing works correctly, if stores add upto 150 then individual stores should be 75
    test_distance_between(): tests if the calculation of pythag distance works correctly
    """

    def test_eat_1(self):
        """
        tests if environment > 10 that 10 will be deducted from the environment and added to the store
        """

        #sets environment and other agents
        self.agents = []
        self.environment = model.read_data()
        self.cols = len(self.environment[0])
        self.rows = len(self.environment)

        #creates agent
        agent = agentframework.Agent(1, self.environment, self.agents, self.cols, self.rows)
        self.environment[agent.y][agent.x] = 25
        agent.eat()
        self.assertEqual(self.environment[agent.y][agent.x], 15)
        self.assertEqual(agent.store,10)

    def test_eat_2(self):
        """
        tests if environment  < 10 that number will be deducted from the environment and added to the store
        """

        #sets environment and other agents
        self.agents = []
        self.environment = model.read_data()
        self.cols = len(self.environment[0])
        self.rows = len(self.environment)

        #creates agent
        agent = agentframework.Agent(1, self.environment, self.agents, self.cols, self.rows)
        self.environment[agent.y][agent.x] = 8
        agent.eat()
        self.assertEqual(self.environment[agent.y][agent.x], 0)
        self.assertEqual(agent.store,8)
    
    def test_eat_3(self):
        """
        tests if sicking after >=100 in store functions correctly
        """

        #sets environment and other agents
        self.agents = []
        self.environment = model.read_data()
        self.cols = len(self.environment[0])
        self.rows = len(self.environment)

        #creates agent
        agent = agentframework.Agent(1, self.environment, self.agents, self.cols, self.rows)
        agent.store = 100
        self.environment[agent.y][agent.x] = 10
        agent.eat()

        #testing against 110 as it started at 10
        self.assertEqual(self.environment[agent.y][agent.x], 110)
        self.assertEqual(agent.store,0)
    
    def test_share(self):
        """
        tests if sharing works correctly, if stores add upto 150 then individual stores should be 75
        """

        #sets environment and other agents
        self.agents = []
        self.environment = model.read_data()
        self.cols = len(self.environment[0])
        self.rows = len(self.environment)

        #creates secondary agent
        self.agents.append(agentframework.Agent(2, self.environment, self.agents, self.cols, self.rows,30,50))

        #creates primary agent
        agent = agentframework.Agent(1, self.environment, self.agents, self.cols, self.rows,30,40)
        agent.store = 50
        self.agents[0].store = 100
        agent.share_with_neighbours(20)

        #calculated expected average being compared by hand
        self.assertEqual(agent.store,75)
        self.assertEqual(self.agents[0].store,75)

    def test_distance_between(self):
        """
        tests if the calculation of pythag distance works correctly
        """

        #sets environment and other agents
        self.agents = []
        self.environment = model.read_data()
        self.cols = len(self.environment[0])
        self.rows = len(self.environment)

        #creates secondary agent
        self.agents.append(agentframework.Agent(2, self.environment, self.agents, self.cols, self.rows,30,50))

        #creaes primary agent
        agent = agentframework.Agent(1, self.environment, self.agents, self.cols, self.rows,30,40)

        distance = agent.distance_between(self.agents[0])

        #calculated distance by hand to compare with
        self.assertEqual(distance,10)

if __name__ == '__main__':

    #runs the unit tests
    unittest.main()
        

