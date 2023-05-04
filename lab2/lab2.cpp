#include <iostream>
#include <mpi.h>
#include <string>

int main(int argc, char *argv[]) {
  int size, rank;
  MPI_Status status;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  std::cout << "Process " << rank << "/" << size << " is "
            << (rank % 2 ? "odd!" : "even!") << std::endl;
  MPI_Finalize();

  return 0;
}
