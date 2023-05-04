from mpi4py import MPI
import random
import typing

# Defines a function returning a random int in the [1,6] iterval.


def throw_dice(n=1, prnt=False) -> list:
    dice_values = []

    for i in range(n):
        dice_value = random.randint(1, 6)
        dice_values.append(dice_value)

    if prnt == True:
        print(dice_values)

    return dice_values


# Community
comm = MPI.COMM_WORLD
# Rank & Sizes
rank = comm.Get_rank()
size = comm.Get_size()

# 0 - print & send to 3
if rank == 0:
    dice_values = throw_dice(1, True)
    # Send
    dice_value = dice_values[0]
    comm.send(dice_value, 3)

# 1 - throw twice, print each time, sum, send sum to 3

if rank == 1:
    # Throw & print
    dice_values = throw_dice(2, True)
    # sum
    dice_values_sum = sum(dice_values)
    print(dice_values_sum)
    # send.
    comm.send(dice_values_sum, 3)
# 2 - throw thrice, print each time, sum, send sum to 3
if rank == 2:
    dice_values = throw_dice(3, True)
    dice_values_sum = sum(dice_values)
    # send
    comm.send(dice_values_sum, 3)

# 3 - sum of all received
if rank == 3:
    sum = 0
    if size > 1:
        for i in range(size-1):
            # if i == 0:
            #     data = comm.recv(source=0)
            # else:
            #     data = comm.recv(source=MPI.ANY_SOURCE)
            data = comm.recv(source=i)
            # if isinstance(data, list):
            #     # If the received data is a list, add its elements to the sum
            #     for d in data:
            #         sum += d
            # else:
                # If the received data is not a list, assume it's an integer and add it directly to the sum
            sum += data
    # Run
    print(f"Procces {rank} received a sum out of {sum} from other processes!")
