#!/usr/bin/env hy
(import random [randint]
        mpi4py [MPI])

;; Function to throw a dice
(defn throw-dice [[n 1] [prnt False]]
  (let [values []]
    (for [i (range n)]
      (.append values (randint 1 6)))
    (when prnt (print values))
    (return values)))

(setv comm MPI.COMM-WORLD
      rank (comm.Get-rank)
      size (comm.Get-size))

(match rank
  ;; 0: Print and send to 3
  0 (do
      (setv dice-values (throw-dice :prnt True))
      (comm.send (get dice-values 0) 3))
  ;; 1: Throw twice, print each time, sum, send to 3
  1 (do
      (setv dice-values (throw-dice :n 2 :prnt True))
      (comm.send (sum dice-values) 3))
  ;; 2: Throw thrice, print each time, sum, send to 3
  2 (do
      (setv dice-values (throw-dice :n 3 :prnt True))
      (comm.send (sum dice-values) 3))
  ;; 3: sum of all received
  3 (do
      (setv received [])
      (for [i (range size)]
        (when (= i rank)
          (continue))

        (received.append (comm.recv :source i)))

      (print (sum received))))

(print f"Process {rank} of {size} ended")

