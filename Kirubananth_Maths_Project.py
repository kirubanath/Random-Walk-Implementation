import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

d = pd.read_excel("Leader3.xlsx").fillna(0)
a = d.to_numpy()[1:][:,2:] #extracting data from the excel sheet

#this is just for noting down the names of people
k = np.array(d['#'][1:])
n = len(k)
leader = {}
for i in range(n):
    leader[i] = k[i] # a dictionary that has names of people from our class

n = len(a)
count = [0 for i in a] #this is the array that keeps count of how many times we visit a person in the random walk

"""
idea: we are storing all the voting info as a matrix
we start at a random node(random person) then among the people he/she voted we jump to one of them 
then repeat the same process for 10000 times and everytime we keep count of how many times we visited a particular person
result: the person(node) who was visited most is the leader -->
"""

def randomNode(a):
    """
    choose a random neighbour
    (mainly to select the first person)
    """
    node = random.randint(0,len(a)-1) #among the people in a choose a random person
    return node

def nextNeighbour(a,node,count):
    """
    from the current node it will return the next node 
    (from the current porson we jump to one of the people he/she voted for!)
    """
    n = len(a)
    list = a[:,node] #create a list of all people he voted for 
                     #in this list 0 means he didnt vote to 1 means he voted to 
    for i in range(2000): #we took 2000 as random ...take any number of high steps
                          #this step is useful when the person didnt vote for anyone
        x = random.randint(0,n-1) #choose a random person in the class
        if list[x]==1:            #see if this person was voted by our target
            count[x]+=1           #if true then increase the counter 
            return x              # return the new person
    #if we cant find next neighbour in due time we teleport
    return(randomNode(a))  

#initialize a node -->first person
node = randomNode(a)

#do the random walk! for 10000 steps in our case
for i in range(10000): # we did for 10000 steps(walks)
    node = nextNeighbour(a,node,count)



#find the leader-->find the maximum:
count = np.array(count)
count = count/np.linalg.norm(count)
max_index = 0
max = 0 
for i in range(len(count)):
    if max < count[i]:
        max = count[i]
        max_index = i 

#print the leader! 
print(f"Our Leader is: {leader[max_index]}")
print(f"ALL HAIL : {leader[max_index]} we swear to serve under your command!")

#this is just to plot votes/count and the person with highest is the leader/winner
node_list = list(leader.values())
plt.bar(node_list,count)
plt.xlabel("Candidates")
plt.ylabel("scores")
plt.xticks(node_list, rotation=90)
plt.show()

