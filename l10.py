import random
import mpi4py
from mpi4py import MPI
# Un departament de reparatii are 10 echipe in teren.
# MPI Variables.
comm =  MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Fiecare echipa, cand incheie reparatia din teren,
# anunta seful departamentului (procesul 0) ca a efectuat reparatia
# si ii comunica timpul care a fost necesar.

# Nu e sef de departament
if rank != 0:
    print('Echipa de reparatii numarul {rank}.')
    # Trimite timpul de executie a procesului catre rank #0.
    comm.send(random.randint(25, 120), 0)
else:
    print('Sef de departament.')
    # Dupa ce seful a colectat toate mesajele de incheiere a reparatiilor,
    # scrie ca ziua de munca s-a incheiat
    # si cat timp am muncit in total cele 10 echipe.
    sum = 0
    for i in range(size):
        if i == rank:
            continue

        sum += comm.recv(source=i)

    print(f'Ziua de munca s-a incheiat. In total, au fost folosite {sum} minute.')

# RUN
# mpiexec -np 4 python l10.py