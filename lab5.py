#!/usr/bin/env python3
from random import randint
from mpi4py import MPI


def get_random():
    return randint(1, 9)


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


match rank:
    case 0:
        comm.send(get_random(), 1)
        print(comm.recv(source=3))

    case 1:
        comm.send(10 * get_random() + comm.recv(source=0), dest=2)

    case 2:
        comm.send(100 * get_random() + comm.recv(source=1), dest=3)

    case 3:
        comm.send(1000 * get_random() + comm.recv(source=2), dest=0)
