import random

from mpi4py import MPI

# Comunity of processes
com =MPI.COMM_WORLD
# Ranks & Sizes.
rank = com.Get_rank()
size = com.Get_size()

#defines a function returning a random int in the (1,6) interval. 
def throw_dice(n=1, prnt=False)-> list[int]:
    dice_values =[]
    for i in range(n):
        dice_value = random.randint(1,6)
        dice_values.append(dice_value)
        

    if prnt:
        print(f"Process {rank} throw {dice_values}.")
        
    return dice_values


# 0 - print & send to 3

if rank == 0:
    # Throw & Print
    dice_values = throw_dice(1,True)
    # Extract only value
    dice_value = dice_values=[0]
    # Send
    com.send(sum(dice_value), 3)


# 1 trow twice,  print each time, sum, send sum to 3
if rank ==1:
    # Throw & Print
    dice_values = throw_dice(2, True)
    # Sum
    dice_values_sum = sum(dice_values)
    # Send
    com.send(sum(dice_values), 3)
    
    
# 2 trow trice, print each time, sum send sum to 3
if rank == 2:
    # Throw & Print
    dice_values = throw_dice(3, True)
     # Sum
    dice_values_sum = sum(dice_values)
    # Send
    com.send(sum(dice_values), 1)
    
    
# 3 sum of all received
if rank == 3:
    sum = 0
    for i in range(size):
        if i == rank:
             continue
       
        sum += com.recv(source=1)
        
    
    
    print(f"Process {rank} received a sum of {sum} from {size-1} olther processes.")
    