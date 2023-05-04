from random import randint
import time
from mpi4py import MPI


# MPI variables
# citesc prin mpi ce se intampla, pe cat procese se asteapta se se ruleze programul
# comm - multitudinea proceselor pe care a fost instantiat programul (toate proceselor)
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # procesul in sine
size = comm.Get_size()  # numarul proceselor

# Un departament de reparatii are 10 echipe in teren

if rank == 0:
    print('Sef de departament.')
    # Dupa ce seful a colectat toate mesajele de incheiere a reparatiilor,
    # scrie ca ziua de munca s-a incheiat
    # si cat timp am muncit in total cele 10 echipe.
    time_total = 0
    for i in range(1, size):
        time_total += comm.recv(source=1)

    time_total = time.localtime(time_total)
    print(
        f'Ziua de munca s-a incheiat. Cele 10 echipe au muncit in total {time_total}')

else:
    # Trimite timpul de executie a procesului catre rank #0.
    # Fiecare echipa, cand incheie reparatia din teren,
    # anunta seful departamentului (procesul 0) ca a efectuat reparatia
    # si ii comunica timpul care a fost necesar.
    time_start = time.time()
    time.sleep(randint(5, 20))
    time_end = time.time()
    time_total = time_end - time_start
    comm.send(time_total, 0)

    print(
        f'Echipa de reparatii numarul {rank} a terminat lucrarea in {time_total} secunde.')


# RUN
# mpiexec -np 11 python lab-20_04.py

# de terminat si sa lucreze cu tipul de datele corecte
