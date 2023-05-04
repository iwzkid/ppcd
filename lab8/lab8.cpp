#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <mpi.h>
#include <random>
#include <thread>
#include <vector>

int do_random_stuff() {
  std::mt19937_64 rng{std::random_device{}()};
  std::uniform_int_distribution<> dist{1, 3};

  auto start = std::chrono::steady_clock::now();
  std::this_thread::sleep_for(std::chrono::seconds{dist(rng)});
  auto end = std::chrono::steady_clock::now();

  return std::chrono::duration_cast<std::chrono::milliseconds>(end - start)
      .count();
}

int main(int argc, char *argv[]) {
  int size, rank;
  MPI_Status status;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size); // number of processes.
  MPI_Comm_rank(MPI_COMM_WORLD, &rank); // The current process ID / Rank.

  const uint8_t target = 0;
  if (target > size) {
    return 1;
  }

  unsigned long long duration = 0;

  switch (rank) {
  case target: {
    for (size_t i = 0; i < size; i++) {
      if (i == target) {
        continue;
      }

      int curr_dur;
      MPI_Recv(&curr_dur, 1, MPI_INT, i, 69, MPI_COMM_WORLD, &status);
      duration += curr_dur;
    }

    auto secs = duration / 1000;
    duration %= 1000;
    int minutes = duration / 60;
    secs %= 60;
    int hours = minutes / 60;
    minutes %= 60;

    std::cout << "All processes took: " << hours << "h:" << minutes
              << "m:" << secs << "s:" << duration << "ms" << std::endl;
    break;
  }

  default:
    int dur = do_random_stuff();
    MPI_Send(&dur, 1, MPI_INT, 0, 69, MPI_COMM_WORLD);
    break;
  }
  MPI_Finalize();

  return 0;
}
