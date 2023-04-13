import mpi4py
import random

from mpi4py import MPI

# Defines a function returning a random int in the [1,6] interval.
def throw_dice(n=1, prnt=False) -> list[int]:
    dice_values = []
    for i in range(n):
        dice_value = random.randint(1,6)
        dice_values.append(dice_value)

    if prnt:
        print(dice_values)

    return dice_values

# MPI Variables.
# Community of porocesses.
comm = MPI.COMM_WORLD
# Ranks & Sizes.
rank = comm.Get_rank()
size = comm.Get_size()

# 0, 1, 2 + anything other than 3.
if (rank != 3):
    dice_values = throw_dice(rank+1, True)
    comm.send(sum(dice_values), 3)

# 3 - sum of all received
if rank == 3:
    sum = 0
    if size > 1:
        for i in range(size):
            if i == rank:
                continue

            data = comm.recv(source=i)

    print(f"Procesul {rank} received a sum of {sum} from other processes.")

# RUN
# mpiexec -np 4 python .\lab2\l6.py
