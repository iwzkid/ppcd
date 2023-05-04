#include <cstring>
#include <iostream>
#include <mpi.h>
#include <string>

int main(int argc, char *argv[]) {
  int size, rank, errclass, ierr;
  MPI_Status status;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Errhandler_set(MPI_COMM_WORLD, MPI_ERRORS_RETURN); /* return info about
        errors */

  std::string message;
  int count;
  char *buf = (char *)malloc(sizeof(char) * (message.size() + 1));
  char err[MPI_MAX_ERROR_STRING];
  int len;

  switch (rank) {
  case 0:
    message = "123";
    MPI_Send(message.c_str(), message.size() + 1, MPI_CHAR, 1, 19,
             MPI_COMM_WORLD);

    MPI_Probe(1, 98, MPI_COMM_WORLD, &status);
    MPI_Get_count(&status, MPI_CHAR, &count);
    buf = (char *)malloc(sizeof(char) * count);
    ierr = MPI_Recv(&buf, count, MPI_CHAR, 1, 98, MPI_COMM_WORLD, &status);
    std::cout << ierr << std::endl;

    std::cout << "Process " << rank << " completed." << std::endl;
    std::cout << "Message received: " << strlen(buf) << " " << count
              << std::endl;
    break;
  case 1:
    message = "567";
    MPI_Send(message.c_str(), message.size() + 1, MPI_CHAR, 0, 98,
             MPI_COMM_WORLD);

    MPI_Probe(0, 19, MPI_COMM_WORLD, &status);
    MPI_Error_string(status.MPI_ERROR, err, &len);
    MPI_Get_count(&status, MPI_CHAR, &count);
    buf = (char *)calloc(sizeof(char), count);
    MPI_Recv(&buf, count, MPI_CHAR, 0, 19, MPI_COMM_WORLD, &status);
    // message = buf;

    std::cout << "Process " << rank << " completed ! ." << std::endl;
    std::cout << "Message received: " << strlen(buf) << std::endl;
    break;
  default:
    std::cout << "Process " << rank << "/" << size << " is completing."
              << std::endl;
    break;
  }

  MPI_Finalize();

  return 0;
}

// int main(int argc, char **argv) {
//   int myid, numprocs;
//   char mesaj[100];
//   MPI_Status stare;

//   MPI_Init(&argc, &argv);
//   MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
//   MPI_Comm_rank(MPI_COMM_WORLD, &myid);
//   if (myid == 0) {
//     MPI_Send(mesaj, 100, MPI_CHAR, 1, 99, MPI_COMM_WORLD);
//     MPI_Recv(mesaj, 100, MPI_CHAR, 1, 98, MPI_COMM_WORLD, &stare);
//     printf("Procesul %d complet\n", myid);
//   } else if (myid == 1) {
//     MPI_Recv(mesaj, 100, MPI_CHAR, 0, 99, MPI_COMM_WORLD, &stare);
//     MPI_Send(mesaj, 100, MPI_CHAR, 0, 98, MPI_COMM_WORLD);
//     printf("Procesul %d complet\n", myid);
//   }

//   printf("Procesul %d / %d se incheie \n", myid, numprocs);
//   MPI_Finalize();
//   return 0;
// }
