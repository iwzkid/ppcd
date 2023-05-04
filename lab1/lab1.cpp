#include <iostream>
#include <mpi.h>
#include <string>

int main(int argc, char *argv[]) {
  int size, rank;
  MPI_Status status;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  char processor_name[MPI_MAX_PROCESSOR_NAME];
  int len;
  MPI_Get_processor_name(processor_name, &len);

  std::cout << "Process " << rank << "/" << size << " on " << processor_name
            << " says: Hello!" << std::endl;

  MPI_Finalize();

  return 0;
}
