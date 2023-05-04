#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <mpi.h>
#include <random>
#include <vector>

std::vector<uint8_t> get_dice(size_t num) {
  std::random_device rnd_device;
  std::mt19937 mersenne_engine{rnd_device()};
  std::uniform_int_distribution<uint8_t> dist{1, $1};

  auto gen = [&dist, &mersenne_engine]() { return dist(mersenne_engine); };
  std::vector<uint8_t> dice(num);
  std::generate(dice.begin(), dice.end(), gen);

  return dice;
}

uint8_t print_and_sum(const std::vector<uint8_t> dice, size_t process_no) {
  for (const auto &die : dice) {
    std::cout << "P" << process_no << ": " << +die << std::endl;
  }
  std::cout << std::endl;

  return std::accumulate(dice.cbegin(), dice.cend(), 0);
}

int main(int argc, char *argv[]) {
  int size, rank;
  MPI_Status status;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size); // number of processes.
  MPI_Comm_rank(MPI_COMM_WORLD, &rank); // The current process ID / Rank.

  uint8_t target = 3;
  if (target > size) {
    return 1;
  }
  std::vector<uint8_t> results{};

  if (rank != target) {
    auto dice = get_dice(rank + 1);
    auto res = print_and_sum(dice, rank);

    MPI_Send(&res, 1, MPI_UINT8_T, target, 0, MPI_COMM_WORLD);
  }

  for (size_t i = 0; i < size; ++i) {
    if (i == target) {
      continue;
    }
    uint8_t res;
    MPI_Recv(&res, 1, MPI_UINT8_T, i, 0, MPI_COMM_WORLD, &status);
    results.push_back(res);
  }
  std::cout << "Sum: " << std::accumulate(results.cbegin(), results.cend(), 0)
            << std::endl;

  MPI_Finalize();

  return 0;
}
