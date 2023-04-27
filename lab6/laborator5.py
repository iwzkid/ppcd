import mpi4py
from mpi4py import MPI
from random import randint

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def randomNumber():
    return randint(1,9)

if size < 4:
    print("The program needs at least 4 processes.")
else:
    if rank == 0:
        random_number = randomNumber()
        comm.send(random_number*10, dest=1)

        data = comm.recv()
        print(data)

    elif rank == 1:
        data = comm.recv()
        random_number = randomNumber()
        comm.send((random_number + data)*10, dest=2)

    elif rank == 2:
        data = comm.recv()
        random_number = randomNumber()
        comm.send((random_number + data)*10, dest=3)

    elif rank == 3:
        data = comm.recv()
        random_number = randomNumber()
        comm.send(random_number + data, dest=0)
