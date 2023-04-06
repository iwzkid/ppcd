import mpi4py
import random
import typing

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Defines a function return ing a random int in the [1, 6] inrerval.


def throw_dice(n=1, prnt=False) -> list:
    dice_values = []
    for i in range(n):
        dice_values.append(random.randint(1, 6))
    if prnt:
        print(dice_values)
    return dice_values


match rank:
    case 0:  # 0 - print & send to 3
        throw_dice(6, True)
    # 1 - throw twice, print each time, sum , send sum to 3
    # 2 - throw thrice, print each time, sum, send sum to 3
    # 3 - sum of all received
