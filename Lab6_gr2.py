import random
from mpi4py import MPI

def trow_dice(n=1, prnt=False)-> list:
    dice_values = []

    for i in range(n):
        dice_value = random.randint(1,6)
        dice_values.append(dice_value)

        if prnt == True:
            print(dice_value)

    return dice_values

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    dice_values = trow_dice(1,True)


if rank == 0:
    dice_values = trow_dice(1,True)
    dice_values_sum = sum(dice_values)
    print(dice_values_sum)

if rank == 1:
    dice_values = trow_dice(2,True)
    dice_values_sum = sum(dice_values)

if rank == 2:
    sum = 0
    if size > 1:
        for i in range(size-1):
            if i == 0:
                data = comm.recv(source=0)
            else:
                data = comm.recv(source=MPI.ANY_SOURCE)
            sum += data

    print(f"Process {rank} received a sum of {sum} from other processes.")


