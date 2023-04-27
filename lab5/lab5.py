import mpi4py
import random
import typing

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def rand():
    return random.randint(1, 9)


if size < 4:
    print("Error: This program requires at least 4 MPI processes.")
    comm.Abort()

if rank == 0:
    x0 = rand()
    print(x0)
    comm.send(x0, dest=1)
elif rank == 1:
    x1 = rand()
    x = x1*10 + comm.recv(source=0)
    print(x)
    comm.send(x, dest=2)
elif rank == 2:
    x2 = rand()
    x = x2*10 + comm.recv(source=1)
    print(x)
    comm.send(x, dest=3)
elif rank == 3:
    x3 = rand()
    x = x3*10 + comm.recv(source=2)
    print(x)
