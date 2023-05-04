import time

from mpi4py import MPI
from random import randint

# MPI Variables.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Un departament de reparații are 10 echipe in teren. 
# mpiexec -np 11 python .\lab8\l8_attempt_2.py

if rank == 0:
# După ce șeful a colectat toate mesajele de încheiere a reparațiilor,
# scrie ca ziua de muncă s-a încheiat și cât timp au muncit în total cele 10 echipe.
    time_total = 0
    for i in range(1, size):
        time_total += comm.recv(source=i)

    time_total = time.localtime(time_total)

    print(f"Time din localtime = {time_total}")

    time_total = time.strftime('%H:%M:%S', time_total)

    print(f"Procesarea s-a incheiat. Cele {size} procese au durat in total {time_total}.")

else:
# Fiecare echipa,
# când încheie reparatia din teren,
# anunța șeful departamentului (procesul 0) că a efectuat reparatia
# si îi comunica timpul care a fost necesar.
    time_start = time.time()
    # print(f"Time start: {time_start}")
    time.sleep(randint(5, 20))
    time_end = time.time()
    # print(f"Time end: {time_end}")
    time_total = time_end - time_start
    # print(f"Time total: {time_total}")

    comm.send(time_total, 0)

    print(f"Procesul #{rank} a durat {time_total} secunde.")

# https://pynative.com/python-get-time-difference/
