# ppcd 09.03.2023 - invatam cum sa comunicam intre procese
import mpi4py

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"Hello world from process {rank} out of {size} processes")
