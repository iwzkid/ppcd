#!/usr/bin/env python3
from random import randint
from mpi4py import MPI


def throw_dice(n=1, prnt=False):
    values = []
    for i in range(n):
        values.append(randint(1, 6))

    if prnt:
        print(values)

    return values


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

match rank:
    case 0:
        dice_values = throw_dice(prnt=True)
        comm.send(dice_values[0], 3)

    case 1:
        dice_values = throw_dice(n=2, prnt=True)
        comm.send(sum(dice_values), 3)

    case 2:
        dice_values = throw_dice(n=3, prnt=True)
        comm.send(sum(dice_values), 3)

    case 3:
        received = []
        for i in range(size):
            if i == rank:
                continue

            received.append(comm.recv(source=i))
        print(sum(received))


print(f'Process {rank} of {size} ended')

