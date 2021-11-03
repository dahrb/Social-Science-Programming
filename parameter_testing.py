#######################################################################################################
#IMPORTS
#######################################################################################################

import subprocess
import time

#######################################################################################################
#MAIN
#######################################################################################################

"""KNOWN ISSUE - parameter testing does not respect the stop condition and iterates through it - further details in README"""

#allows parameter testing for agents in the range 10-100 with no visual output
for i in range(10,110,10):
    
    start = time.time()
    subprocess.call(['python','model.py',str(i),'10','20','False'])
    end = time.time()

    print("time= ", str(end-start))
