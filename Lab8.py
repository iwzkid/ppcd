import random
import time

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank != 0:
    print(f"Echipa de reparatii numarul {rank}.")
    # Trimite timpul de executie al procesului catre rank #0.

    time_start = time.time()
    time.sleep(random.randint(5, 20))
    time_end = time.time()
    elapsed_time = time_end - time_start

    comm.send(elapsed_time, 0)
else:
    print("Sef de departament.")
    time = 0
    for i in range(size):
        if i == rank:
            continue
        
        time += comm.recv(source=1)

    print(f'Ziua de munca s-a terminat, au fost {time} minute.')

# RUN
# mpiexec -n 4 python Lab_PPCD.py