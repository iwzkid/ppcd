import mpi4py
import random
import typing

from mpi4py import MPI
#defines a function returning a random int in the (1,6) interval. 
def trow_dice(n=1, prnt=False)-> int:
    dice_values =[]
    for i in range(n):
        dice_value = random.randint(1,6)
        dice_values.append(dice_value)

    if prnt:
        print(dice_values)
    return dice_values

# comunity of processes
com =MPI.COMM_WORLD
#rank & lines
rank = com.Get_rank()
size = com.Get_size()

# 0=print & send to 3

if rank == 0:
    trow_dice(6,True)

# 1 trow twice,  print each time, sum, send sum to 3
# 2 trow trice, print each time, sum send sum to 3
# 3 sum of all received

#print(trow_dice())