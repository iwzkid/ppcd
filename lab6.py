import mpi4py
import typing
import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
dice_values_sum3 = 0
#defines a function returing a random int from the [1,6] interval.
def throw_dice(n=1, prnt=False) -> list:
    dice_values = []
    for i in range(n):
        dice_value = random.randint(1,6)
        dice_values.append(dice_value)
    if prnt:
        print(dice_values)
    return dice_values

match rank:
    case 0: # 0 - print -> send to 3
        dice_values = throw_dice(1, True)
        comm.send(sum(dice_values), 3)
    case 1: # 1 - throw 2 dices, print each time, sum, send to 3
        dice_values = throw_dice(2,True)
        dice_values_sum = sum(dice_values)
        comm.send(dice_values_sum, 3)
    case 2: # 2 - throw 3 dices, print each time, sum, send to 3
        dice_values = throw_dice(3, True)
        dice_values_sum = sum(dice_values)
        comm.send(dice_values_sum, 3)
    case 3: # 3 - sum of all received
        sum = 0
        if size > 1:
            for i in range(size-1):
                data = comm.recv(source=MPI.ANY_SOURCE)
                sum += data
        print(f"Procesul {rank} a primit suma {sum} din celelalte procese.")
        


        