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
    dice_values = throw_dice(2, True)
    dice_value = dice_values[0]
    comm.send(dice_value, 3)

if rank == 1:
    # throw and print
    dice_values = throw_dice(2, True)
    # sum
    dice_values_sum = sum(dice_values)
    print(dice_values_sum)

if rank == 2:
    # throw and print
    dice_values = throw_dice(3, True)
    # sum
    dice_values_sum = sum(dice_values)
    print(dice_values_sum)

if rank == 3:
    sum = 0
    if size > 1:
        for i in range(size - 1):
            data = comm.recv(source=i)

            sum += data
    # Run
    print(f"Procces {rank} received a sum out of {sum} from other processes!")

# 1 - throw twice print each line , sum, send TO 3
# 2- throw twice, print each time, sum, send sum
# 3 summ of al
