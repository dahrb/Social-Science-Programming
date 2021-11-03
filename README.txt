CONTENTS OF DIRECTORY
---------------------

- model.py: the main class to run in order to see the GUI output
- agentframework.py: the file containing the Agent class
- parameter_testing.py: this file allows different numbers of agents
			to be run one after the other without showing 
			the GUI for more effective running
- tests.py: contains the unit tests which were conducted
- in.txt: contains the environment data
- LICENSE.txt: the license for this software
- README.txt: the readme file

INTRODUCTION
---------------------

This software instantiates an ABM model with agents interacting with
each other and an environment. 

HOW TO RUN
----------------------

This software was tested and developed with an Anaconda distribution
of Python 3.8.8 64-bit.

Run model.py to run the model with the GUI.
^ this file can also be run in the command line with the following
arguments: number of agents, number of iterations, neighbour distance

python model.py 20 2 20

Run parameter_testing.py to run the model without the GUI visible
and with different numbers of agents from 10-100.

Run test.py to run the unit tests

EXPECTED OUTCOME
----------------------

The output for running model.py will be a GUI which will allow
the model to run from the menu showing an animation of the model running. 
Pressing the quit button in the menu will end the GUI and print the final
locations and food stored for all the agents. This will also cause the final
environment to be written to a .txt file called 'final_environment.txt' 
and the total amount stored by all agents to be added to a .txt file called 'stored_food.txt'.

Whilst the model is running the iteration number and time taken for that
iteration will be printed.

KNOWN ISSUES
----------------------

In parameter_testing.py there is an issue in which after the stopping condition
is reached by printing 'stopping conditon met' it will continue to run
through further iterations. I believe this is because the stopping condition is
tied to the animation which I am not running in this file but I have been
unable to fix it.

TESTING
----------------------

Testing has been conducted through print statements which have
been commented out and unit tests.












