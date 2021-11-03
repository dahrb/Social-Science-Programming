# do docs
# known issue - stopping condition doesn't work from command line with no visualisation

#######################################################################################################
#IMPORTS
#######################################################################################################

import random
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework
import csv
import tkinter
import requests
import bs4
import sys
import time

#######################################################################################################
#FUNCTIONS
#######################################################################################################

def update(frame_number):
    """
    iterates through the eating, moving and sharing of the agents
  
    Parameters:
    frame_number (int): the animation frame number which corresponds to the current iteration number

    """
  
    #resets graph
    fig.clear() 

    #the stopping condition -> bool
    global carry_on

    #shows the background image in the graph and sets the x/y limits
    plt.imshow(environment)
    plt.xlim(0, cols)
    plt.ylim(0, rows)
    
    print("iteration =", frame_number)

    #times how long each iteration takes to process
    start = time.time()
    
    #shuffles the order of the agents each iteration
    random.shuffle(agents)

    #iterates through the agents
    for i in range(num_of_agents):
        #print(agents[i])
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

    #sets a stopping condition when all agent stores are greater than or equal to 85
    stop = False
    for i in range(num_of_agents):
        store = agents[i].store
        #print(store)
        if store <=85:
            stop=False
            break
        else:
            stop=True

    if stop == True:
        carry_on = False
        print("stopping condition met")
    
    #runs animation and plots graph
    for i in range(num_of_agents):
        plt.scatter(agents[i].x,agents[i].y)
    
    end = time.time()

    print("Iteration Time Taken = ",str(end-start))

def gen_func(b=[0]):
    """
    generates the next frame_number unless the stopping condition is reached
  
    Return:
    a (int): current frame_number/ iteration
    """

    #starts the frame_number at 0
    a = 0
    global carry_on

    #defines the stopping condition as false so long as the num_of_iterations is less than a and carry_on is true
    while (a<num_of_iterations) & (carry_on):
        yield a
        a += 1

def run():
    """
    allows the animation to run
    """

    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_func, repeat=False)
    canvas.draw()

def webscraping():
    """
    webscrapes the data from the iven domain
  
    Return:
    td_ys (class): this class holds the x values scraped from the data
    td_xs (class): this class holds the y values scraped from the data
    """

    #requests the webpage otherwise raises an exception
    try:
        r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    except:
        raise ConnectionError("The server could not be accessed, you might be offline.")    

    #the html
    content = r.text

    #initialises the html parser
    soup = bs4.BeautifulSoup(content, 'html.parser')

    #finds the x and y values storing them in a class
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    
    #commented out check that data scraped correctly
    #print(td_ys)
    #print(td_xs)
    
    return td_ys, td_xs

def read_data():
    """
    webscrapes the data from the given domain
  
    Return:
    environment (list): a list defining the quantities of food and dimensions of the environment
    """

    #tries to read the stated file, if not raises an exception
    try:
        #reads in the text data
        with open("in.txt", newline='') as f:
            
            dataset = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
            
            #initialises the environment list
            environment = []

            #iterates through each row adding the values
            for row in dataset:
                
                rowlist = []
                for value in row:
                    rowlist.append(value)

                #adds the row to the environment list
                environment.append(rowlist)
    except:
        raise IOError("The file you are trying to open does not exist")

    #print(environment)

    return environment

def create_agents():
    """
    creates the specified number of agents within the model
  
    Return:
    agents (list): a list with all the agent class instances composing the model
    """

    #initialises the agents list
    agents = []

    #creates agents
    for i in range(num_of_agents):

        #gives the corresponding x and y coords from the data read in
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)

        #adds the newly created agent to the list
        agents.append(agentframework.Agent(i, environment, agents,cols,rows,x,y))
    
    return agents

#######################################################################################################
#MAIN
#######################################################################################################

if __name__ == '__main__':

    #HYPERPARAMETERS

    #sys.argv enables running from the command line
    try:
        #number of agents
        num_of_agents = int(sys.argv[1])
    except:
        print("You did not enter an integer number for number of agents, default value 10 used")
        num_of_agents = 10

    try:
        #number of iterations
        num_of_iterations = int(sys.argv[2])
    except:
        print("You did not enter an integer number for number of iterations, default value 100 used")
        num_of_iterations = 100

    try:
        #how large the neighbourhood is
        neighbourhood = int(sys.argv[3])
    except:
        print("You did not enter an integer number for neighbourhood, default value 20 used")
        neighbourhood = 20

    try:
        #a flag to determine whether the UI should be displayed or not
        if sys.argv[4] == 'False':
            visualOutput = False
        else:
            visualOutput = True
    except:
        print("You did not enter a correct boolean for visualOutput so default True used")
        visualOutput = True

    #sets the random seed
    random.seed(42)

    #defines the environment
    environment = read_data()

    #defines the size of the columns and rows
    cols = len(environment[0])
    rows = len(environment)

    #defines the y and x coordinates coming from the webscraped data
    td_ys, td_xs = webscraping()

    #stores agents
    agents = create_agents()

    #defines animation
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True

    #defines the UI window, including the menu
    root = tkinter.Tk()
    root.wm_title("Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    menu= tkinter.Menu(root)
    root.config(menu=menu)
    model_menu = tkinter.Menu(menu)
    menu.add_cascade(label='Model', menu=model_menu)
    model_menu.add_command(label="Run Model", command=run)

    #allows the user to quit the window
    model_menu.add_command(label="Quit", command=root.quit)

    #initialises the UI and checks whether visual output is on or off
    if visualOutput == True:
        tkinter.mainloop()

    else:

        #if visual output is off then loop the update function to enable the agents to perform their actions iteratively
        for i in range(0,num_of_iterations):
            update(i)

    #Prints final agents
    print("Final Agents")
    # https://docs.python.org/3/howto/sorting.html
    sorted_agents = sorted(agents, key=lambda a: a.i)
    for i in range(num_of_agents):
        print(sorted_agents[i])

    #writes the final environment to a txt file 
    f2 = open('final_environment.txt','w',newline='')
    writer = csv.writer(f2, delimiter=',')
    for row in environment:
        writer.writerow(row)
    f2.close()

    #writes total amount stored by all agents on one line - appends data
    #tested by running the model a few times and checking the file appends to a new row each time in the same file
    f3 = open('stored_food.txt','a',newline='')
    writer = csv.writer(f3, delimiter=',')
    food_stored = []
    for i in range(num_of_agents):
        food_stored.append(sorted_agents[i].store)
    writer.writerow(food_stored)
    f3.close()  