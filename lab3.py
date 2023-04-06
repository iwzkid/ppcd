import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

x = random.randint(1, 9)

if rank == 0:
    comm.send(x, dest=1)

if rank == 1:
    x = comm.recv(source=0)
    y = random.randint(1, 9)
    xy = int(str(y) + str(x))
    print("Process 1 generated:", xy)
    comm.send(xy, dest=2)

if rank == 2:
    xy = comm.recv(source=1)
    z = random.randint(1, 9)
    xyz = int(str(z) + str(xy))
    print("Process 2 generated:", xyz)
    comm.send(xyz, dest=3)

if rank == 3:
    xyz = comm.recv(source=2)
    w = random.randint(1, 9)
    xyzw = int(str(w) + str(xyz))
    print("Process 3 generated:", xyzw)
    comm.send(xyzw, dest=0)

if rank == 0:
    xyzw = comm.recv(source=3)
    print("Final number:", xyzw)
