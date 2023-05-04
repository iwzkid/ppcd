from random import randint
from mpi4py import MPI
import time
 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
time_total = 0
 
if rank == 0:
    for i in range(1, size):
        time_total += comm.recv(source=i)
    print(f"Ziua de munca s-a incheiat. Cele 10 echipe au lucrat in total {time_total}.")
 
else:
    time_start = time.time()
    time.sleep(randint(5,20))
    time_end = time.time()
    time_total = time_end - time_start
    print(f"Echipa {rank} a terminat munca in {time_total}.")
    comm.send(time_total, 0)