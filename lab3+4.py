import random

from mpi4py import MPI
#defines a function returning a random int in the (1,6) interval. 
def trow_dice(n=1, prnt=False)-> list[int]:
    dice_values =[]
    for i in range(n):
        dice_value = random.randint(1,6)
        dice_values.append(dice_value)

    if prnt:
        print(dice_values)

    return dice_values

# comunity of processes
com =MPI.COMM_WORLD
#ranks & sizes
rank = com.Get_rank()
size = com.Get_size()

# 0=print & send to 3
if (rank != 3):
    dice_values = trow_dice(rank+1, True)
    com.send(sum(dice_values), 3)

# 3 sum of all received

if rank == 3:
    sum = 0
    for i in range(size):
        if i == rank:
           continue

        sum += com.recv(source=i)

print(f'Procesul {rank} recived a sum of {size} from other processes.')