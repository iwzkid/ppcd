import random
from mpi4py import MPI

# comunity of processes
comm = MPI.COMM_WORLD
# ranks & sizes
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    x0 = random.randint(1, 9)
    print(f"Process {rank}: x0 = {x0}")
    comm.send(x0, dest=1)

if rank == 1:
    x0 = comm.recv(source=0)
    x1 = random.randint(1, 9)
    x = x1 * 10 + x0
    print(f"Process {rank}: x = {x}")
    comm.send(x, dest=2)

if rank == 2:
    x = comm.recv(source=1)
    x2 = random.randint(1, 9)
    x = x2 * 100 + x
    print(f"Process {rank}: x = {x}")
    comm.send(x, dest=3)

if rank == 3:
    x = comm.recv(source=2)
    x3 = random.randint(1, 9)
    x = x3 * 1000 + x
    print(f"Process {rank}: x = {x}")
    comm.send(x, dest=0)

if rank == 0:
    x = comm.recv(source=3)
    print(f"Process {rank}: x received from process 3: {x}")
