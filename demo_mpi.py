#Folosim libreria mpi4py de la Python
import mpi4py

#Din libreria mpi4py, folosim o bucata care ne trebuie, in cazul asta MPI
from mpi4py import MPI

#MPI Variables.
comm =  MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#Aicea tiparim ce vrem prin print
print (f"Hello world from process {rank} out of {size} processes!")
