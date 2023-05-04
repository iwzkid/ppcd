import random
import time

from mpi4py import MPI

# Un departament de reparatii are 10 echipe in teren. 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Nu e sef de departament
if rank != 0:
    print(f'Echipa de reparatii numarul {rank}.')

    time_start = time.time()
    time.sleep(random.randint(5, 20))
    time_end = time.time()
    elapsed_time = time_end - time_start

    comm.send(elapsed_time, 0)
else:
    print('Sef de departament.')
    time = 0
    for i in range(size):
        if i == rank:
            continue

        time += comm.recv(source=i)

    print(f'Ziua de munca s-a incheiat. In total, au fost folosite {time} secunde.')