#############LAB1################

import mpi4py
from mpi4py import MPI
from random import randint

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# function that simulates a dice throw
def throw_dice():
    return randint(1,6)

if size < 4:
    print("The program needs at least 4 processes.")
else:
    if rank == 0:
        random_number = throw_dice()
        comm.send(random_number, dest=3)

    elif rank == 1:
        rolls = [throw_dice() for _ in range(2)]
        rolls_sum = sum(rolls)
        comm.send(rolls_sum, dest=3)

    elif rank == 2:
        rolls = [throw_dice() for _ in range(3)]
        rolls_sum = sum(rolls)
        comm.send(rolls_sum, dest=3)

    elif rank == 3:
        total_sum = 0
        for i in range(3):
            data = comm.recv()
            total_sum += data
        print("Total sum:", str(total_sum))