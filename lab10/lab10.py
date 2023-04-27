import random
import time


from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    quantity = 100;
    comm.send(quantity, 1)

if rank == 1:
    quantity = comm.recv(0)

    for i in range (2,4):
        comm.send(quantity, i)

if rank in range (2,4):
    quantity = comm.recv(1)

    amount = random(quantity-50, quantity+50)
    price_per_unit = random(1,5)

    offer = {
        'amount' : amount,
        'price_per_unit' : price_per_unit
    }

    comm.send(offer, 0)