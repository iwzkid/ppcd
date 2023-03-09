#!/usr/bin/env hy
(import mpi4py [MPI])

(defn main []
  (setv comm MPI.COMM_WORLD
        rank (comm.Get-rank)
        size (comm.Get-size))

  (print f"Hello world from process {rank} out of {size} processes!"))

(when (= __name__ "__main__")
  (main))

