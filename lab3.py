from mpi4py import MPI

com = MPI.COMM_WORLD
rank = com.Get_rank()
size = com.Get_size()
# thread-uri
print(f"Hello world from process {rank} out of {size} processors!")
