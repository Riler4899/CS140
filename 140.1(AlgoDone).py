



#INPUT/FILEREAD
f= open('WarStrategy.txt')
d= open('WarStrategy.txt')

cities = [i.strip("\n1234567890").strip() for i in f.readlines()]
day = [i.strip("\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ").strip() for i in d.readlines()]
city_array=[]
citiesLeft = list(cities)
# print(day[0])


for i in cities:
    f = open(i +'.txt')
    city_array.append([i.strip() for i in f.readlines()])
    f.close()



#ALGO STARTS HERE
actions = ["attack","defend","parley","siege"]
role = 1
print("Welcome Commandante! Our grand army has begun its offensive onto these lands for the exterminatus of the xeno filth that ravage these lands and for the glory of our God-Emperor ")
print("What shall you be doing for this grand crusade o wise commandante?")
while True:
    
    for act in range(len(actions)):
        print("{} - {}".format(act,actions[act]))
    role = int(input())
    if(role < len(actions) and role >= 0):
        break
    print("")
    print("That is not an option, commandante")



daynum = 1 # Tells us the day
cityNum = 0 # corresponds to each city. First city = 0 etc.
#Standard : City, Action, Turns
current = [] 
queue = [] 
subcommander = [] 
subcommandertemp = [] 
planPos = []

#Function to add new orders. Based on the city
def addshit(city):
    global current
    global queue
    global subcommander
    global city_array
    global planPos
    global cities
    global citiesLeft
    if(planPos[city] != len(city_array[city])):
        order = [city, city_array[city][planPos[city]].split()[0], int(city_array[city][planPos[city]].split()[1])]
        
        if(order[1] == actions[role]):
            #if the current is empty then add it to current
            
            if(len(current) == 0):
                current = order
                print("We are beginning to {} for {}, Commandante".format(order[1],cities[order[0]]))
                #If its full add it to queue
            else:
                queue.append(order)
                print("Your forces at {} is waiting for further commands, Commandante".format(cities[order[0]]))
               
        else:
            subcommandertemp.append(order)
            print("Our forces have begun the {} for {}, Commandante".format(order[1],cities[order[0]]))
        planPos[city] += 1
    else:
        #checks if the city has fallen and scratches it off our cities left list
        for i in range(len(citiesLeft)):
            if(citiesLeft[i] == cities[city]):
                citiesLeft.pop(i)
                print("The Battle for {} has concluded, Commandante. The city has fallen to our victorious troops.".format(cities[city]))
                break

#Function containing the strat we use. Now set to FIFO
def strat(array, index): 
    popped = array.pop(index)
    return popped

while True:
    #Update all the counters
    if(len(current) != 0):
        current[2] -= 1
    #add if current ends transfer 1st element to queue
        if(current[2] == 0 and len(queue) != 0):
            addshit(current[0])    
            current = strat(queue,0)
        elif(current[2] == 0 and len(queue) == 0):
            t = current[0]
            current = []
            addshit(t)
            if(len(current) == 0 and len(queue) != 0):
                current = strat(queue,0)
            

    for suborder in subcommander:
        suborder[2]-=1
        #Only add orders with greater turns ahead to subcommandertemp.
        #  This was done to prevent popping or removing an index during the for loop
        if(suborder[2] == 0):
            addshit(suborder[0])
            
        else:
            subcommandertemp.append(suborder)
            



    #Chek for new cities to take
    if(cityNum < len(day)):
        if(int(day[cityNum]) == daynum):
            print("The Battle for {} has begun Commandante".format(cities[cityNum]))
            planPos.append(0)
            #Check if its our role
            addshit(cityNum)
            cityNum += 1

    #Reset the subcommander orders and continue to the next day
    subcommander = subcommandertemp 
    subcommandertemp = []
    if(len(citiesLeft) == 0):
        print("Congratulations Commandante, our glorious forces showed the Xeno scum the might our gracious God-Emperor and defeated them all. The Empire of Maharlika ENDURES!")
        break
    #Add print stuff here :3

    print("Report for day: " + str(daynum))
    print("current: ")
    print(current)
    print("queue ")
    print(queue)
    print("Subcommander" )
    print(subcommander)
    print("------------------------")

    

    #Do not edit below this
    
    daynum += 1
