import random

from mpi4py import MPI

# Simulate throwing a dice.
def random_1_6(times = 1):
    """
    random_1_6 generates a random number between 1 and 6.

    :return: integer values of generated numbers under an array.
    """ 
    times = range(times)
    result = []

    for time in times:
        result.append(random.randint(1,6))

    return result

# Define variables for parallelism.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

match rank:
    case 0:
        # Throw once.
        rank_0_throws = random_1_6()
        # Print.
        print(f"Process {rank} threw a {rank_0_throws}.")
    case 1:
        #Throw & Print twice.
        rank_1_throws =  random_1_6(2)
        print(f"Process {rank} threw a {rank_1_throws}.")

        #Sum values.
        sum_rank_1 = sum(rank_1_throws)
        print(f"Sum of values thrown by process {rank} is {sum_rank_1}.")

    case 2:
        #Throw & Print thrice.
        rank_2_throws =  random_1_6(3)
        print(f"Process {rank} threw a {rank_2_throws}.")

        #Sum values.
        sum_rank_2 = sum(rank_2_throws)
        print(f"Sum of values thrown by process {rank} is {sum_rank_2}.")

# print(random_1_6())