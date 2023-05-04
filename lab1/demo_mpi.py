# Import the module providing the MPI implementation.
import mpi4py

# In order to check locally what MPI implementation has been installed, run the following:
# python // will start the python interpreter.
# print(mpi4py.get_config()) // will print the mpi configuration.

# If MPI4PY is not installed, run:
# pip install mpi4py

# If MPI is not installed, download it for windows from:
# https://www.microsoft.com/en-us/download/details.aspx?id=100593

# PIP is usually shipped with Python, if PIP is not installed, check that you have python installed.

# Import the required packages.
from mpi4py import MPI

# Define variables.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Showcase parallelism.
# Print the same message from parallel processes.
print(f"Hello world from process {rank + 1} out of {size} processes!")

# Run on 4 slots.
# mpiexec -np 4 python demo_mpi.py
