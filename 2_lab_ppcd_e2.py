import mpi4py
import random
import typing

from mpi4py import MPI


def throw_dice(n=1, prnt=False) -> list:
    dice_values = []
    for i in range(n):
        dice_value = random.randint(1, 6)
        dice_values.append(dice_value)

    if prnt:
        print(dice_values)

    return dice_values


comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

# 0 - print & send to 3
if rank == 0:
    throw_dice(2, True)
# 1 - throw twice print each line , sum, send TO 3
# 2- throw twice, print each time, sum, send sum
# 3 summ of all
