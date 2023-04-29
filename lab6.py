# echipele in teren
import time
from random import randint
# raninit
from mpi4py import MPI

# MPI variables
# comunity of processes
comm = MPI.COMM_WORLD
# ranks & sizes
rank = comm.Get_rank()
size = comm.Get_size()

if rank ==0:
    time_total = 0
    for i in range(1, size):
        time_total+=comm.recv(source=i)

    time_total = time.localtime(time_total)
    time_total = time.strftime('$H:$M:$S', time_total)
    print(f"Procesul s-a incheiat. Cele {size} procese au durat in total {time_total}.")

else:
    time_start = time.time()
    #print(f"Time start: {time_start}")
    time.sleep(randint(5, 20))
    time_end = time.localtime()
    #print(f"Time end: {time_end}")
    #time_total= time.localtime(time_end - time_start))
    time_total = time_end + time_start
    time_total = randint(20, 60)
    comm.send(time_total, 0)
    print(f"Procesul # {rank} a durat {time_total} secunde.")

# mpiexec.exe -np 11 python lab6.py