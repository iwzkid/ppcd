from mpi4py import MPI
import random

# 1. generate random integer from 0 to 9
def random_number(prnt=False) -> int:
    n = random.randint(0, 9)
    if prnt:
        print(f"Process {rank}: Random number is {n}")
    return n

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 2:
    print("Error: This program requires at least 2 processes to run")
    comm.Abort()

# initialize sent_value
sent_value = 0

# send and receive values
if rank == 0:
    random_value = random_number(True)
    sent_value = random_value
    print(f"Process {rank}: Sending {sent_value} to Process 1")
    comm.send(sent_value, dest=1)
elif rank == 1:
    received_value = comm.recv(source=0)
    print(f"Process {rank}: Received {received_value} from Process 0")
    random_value = random_number(True)
    sent_value = random_value * 10 + received_value
    print(f"Process {rank}: Sending {sent_value} to Process 2")
    comm.send(sent_value, dest=2)
elif rank == 2:
    received_value = comm.recv(source=1)
    print(f"Process {rank}: Received {received_value} from Process 1")
    random_value = random_number(True)
    sent_value = random_value * 10 + received_value
    print(f"Process {rank}: Sending {sent_value} to Process 3")
    comm.send(sent_value, dest=3)
elif rank == 3:
    received_value = comm.recv(source=2)
    print(f"Process {rank}: Received {received_value} from Process 2")
    random_value = random_number(True)
    sent_value = random_value * 10 + received_value
    print(f"Process {rank}: Sending {sent_value} to Process 0")
    comm.send(sent_value, dest=0)

# print final result
if rank == 0:
    print(f"Process {rank}: Final result is {sent_value}")