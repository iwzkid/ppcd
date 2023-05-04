import mpi4py
import numpy
import random
import typing

# https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html
from mpi4py import MPI

# Defines a function returning a random int in the [1,6] interval.
def throw_dice(n=1, prnt=False) -> list:
    dice_values = []
    for i in range(n):
        dice_value = random.randint(1,6)
        dice_values.append(dice_value)

    if prnt:
        print(dice_values)

    return dice_values

# Community of processes.
comm = MPI.COMM_WORLD

# Ranks & Size.
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Generate two random numbers and send them to rank 3
    rand_nums = throw_dice(1, True)
    comm.send(rand_nums, dest=3)

if rank == 1 or rank == 2:
    # Generate one random number and send it to rank 3
    rand_num = random.randint(1, 100)
    comm.send(rand_num, dest=3)

if rank == 3:
    # Receive all the random numbers and display their sum
    sum = 0
    if size > 1:
        for i in range(size-1):
            if i == 0:
                data = comm.recv(source=0)
            else:
                data = comm.recv(source=MPI.ANY_SOURCE)
            if isinstance(data, list):
                for j in range(len(data)):
                    sum += data[j]
            else:
                sum += data
    print(f"Rank {rank} received a sum of {sum} from other processes.")

# RUN
# mpiexec -np 3 python .\lab6\l6_xld.py