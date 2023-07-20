from collections import deque



## will start on inputted floor floor
floor = int(input("what floor are you on?"))

repeat = int(input("how many floors do you need to visit?"))

buttonQueue = deque()

## enqueues floors inputted by user
for i in range(repeat):
        desiredFloor = int(input("which floor?"))
        buttonQueue.append(desiredFloor)

## needs to calculate the difference between the floor you are on and the floors inputted
sortedQueue = deque(sorted(buttonQueue, key=lambda x: (
    x > floor,  # Sort floors above the current floor first
    abs(x - floor)  # Sort floors based on their proximity to the current floor
)))

print(sortedQueue)
        



        


       
                
                




    
    
