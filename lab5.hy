#!/usr/bin/env hy
(import random [randint]
        mpi4py [MPI])

(setv comm MPI.COMM-WORLD
      rank (comm.Get-rank)
      size (comm.Get-size))

(defn get-random []
  (return (randint 1 9)))

(match rank
  0 (do
      (comm.send (get-random) 1)
      (print (comm.recv :source 3)))

  1 (comm.send
      (+ (* 10 (get-random))
         (comm.recv :source 0))
      :dest 2)

  2 (comm.send
      (+ (* 100 (get-random))
         (comm.recv :source 1))
      :dest 3)

  3 (comm.send
      (+ (* 1000 (get-random))
         (comm.recv :source 2))
      :dest 0))

