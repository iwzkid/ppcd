import mpi4py
import random
import typing

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
# Ranks & Sizes.
rank = comm.Get_rank()
size = comm.Get_size()

# 0 - print & send to 3
if rank == 0:
    # Throw & Print.
    dice_values = throw_dice(1, True)
    # Extract only value.
    dice_value = dice_values[0]
    # Send.
    comm.send(dice_value, 3)

# 1 - throw twice, print each time, sum, send sum to 3
if rank == 1:
    # Throw & Print.
    dice_values = throw_dice(2, True)
    # Sum.
    dice_values_sum = sum(dice_values)
    # Send.
    comm.send(dice_values_sum, 3)

# 2 - throw thrice, print each time, sum, send sum to 3
if rank == 2:
    # Throw & Print.
    dice_values = throw_dice(3, True)
    # Sum.
    dice_values_sum = sum(dice_values)
    # Send.
    comm.send(dice_values_sum, 3)

# 3 - Sum of all received
if rank == 3:
    sum = 0
    if size > 1:
        for i in range(size-1):
            # if i == 0:
            #     data = comm.recv(source=0)
            # else:
            #     data = comm.recv(source=MPI.ANY_SOURCE)
            data = comm.recv(source=i)
            sum += data

    print(f"Process {rank} received a sum of {sum} from other processes.")

# RUN
# mpiexec -np 4 python .\lab6\l6_gr1.py