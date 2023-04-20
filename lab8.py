#!/usr/bin/env python3
import time
from random import randint
from mpi4py import MPI


# NOTE: OpenMPI might complains about not enough slots being allocated
# if that happens, you can commit more slots with `--host localhost:N` as bellow
# $ mpirun --host localhost:11 -np 11 lab8.py


# Initialize the MPI communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


# Using a match to make it a tad more extensible in the future
match rank:
    case 0:
        # A list comprehension that gathers the messages from all processes besides itself
        messages = [comm.recv(source=proc) for proc in range(size) if proc != rank]
        total_time = time.strftime(     # Convert a struct_time into a string
            '%H:%M:%S',                 # according to this format
            time.gmtime(sum(messages))  # Convert the timestamp into a struct_time
        ).lstrip('00:').lstrip('00:')   # then strip leading segments if they're 0

        # Then prints a message with the total number of hours
        print(f"It took a total of {total_time} for all {size - 1} teams to do all their work.")

    # All ranks not covered above go here
    case _:
        # count how long it takes the process to run by checking time.time()
        # before and after starting the work
        time_start = time.time()
        time.sleep(randint(5, 20))  # Totally Real and Useful Work(TM)
        time_end = time.time()
        time_elapsed = time_end - time_start

        # Send the time to process 0
        comm.send(time_elapsed, dest=0)

        # Then print an exit message
        print(f"Process {rank} finished in {round(time_elapsed, 2)} seconds")


