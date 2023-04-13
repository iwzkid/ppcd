import random
from mpi4py import MPI
import time

# Un departament de reparatii are 18 echipe in teren.
# MPI Variables
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Nu e sef de departament
if rank != 0:
    print(f'Echipa de reparatii numarul {rank}.')
    # Trimite timpul de executie a procesului catre rank 0.
    # Fiecare echipa, cand incheie reparatie din teren,
    # anunta seful departamentului (procesul 0) ca a efectuat reparatia
    # si ii comunica timpul care a fost necesar.
       
    time_start = time.time()
    time.sleep(random.randint(5, 20))
    time_end = time.time()
    elapsed_time = time_end - time_start
    
    comm.send(elapsed_time, 0)
else:
    print('Sef de departament.')
    # Dupa ce seful a colectat toate mesajele de incheiere a reparatiilor,
    # scrie ca ziua de munca s-a incheiat
    # si cat timp au muncit in total cele 18 echipe.
    time = 0
    for i in range(size):
        if i == rank:
            continue
        
        time += comm.recv(source=1)
        
    print(f'Ziua de munca s-a incheiat. In total, au fost folosite {time} secunde')  
    
    # mpiexec -np 10 python .\LAB3_TIRIS_CATALIN_IONEL\lab8.py