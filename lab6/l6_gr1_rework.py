import random
from mpi4py import MPI

# MPI Variables.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Defines a function returning a random [int] in the [1,6] interval.
def throw_dice(n=1, prnt=False) -> list[int]:
    dice_values = []
    for i in range(n):
        dice_values.append(random.randint(1,6))

    if prnt:
        print(f"Process {rank} threw: {dice_values}.")

    return dice_values

# 0, 1, 2 + anything other than 3.
if (rank != 3):
    dice_values = throw_dice(rank+1, True)
    comm.send(sum(dice_values), 3)

# 3 - Sum of all received
if rank == 3:
    sum = 0
    for i in range(size):
        if i == rank:
            continue

        sum += comm.recv(source=i)

    print(f"Process {rank} received a sum of {sum} from {size-1} other processes.")

# RUN
# mpiexec -np 4 python .\lab6\l6_gr1_rework.py