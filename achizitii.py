import random
import pprint
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    #Let acquisitions know of the required q.
    quantity = 100
    comm.send(quantity, 1)  # Acquisitions is rank 1.

    offers = []
    for i in range(2, 5):
        offers.append(comm.recv(source=i))

    sorted_offers = sorted(offers, key=lambda x: x['price_per_unit'])
    # pprint.pprint(sorted_offers)
    # bought_amount = 0
    # We know the quantity.
    for offer in sorted_offers:
        if quantity > 0:
            if offer['amount'] >= quantity:
                print("Taking " + str(quantity) + " for " +
                      str(offer['price_per_unit']))
            else:
                print("Taking " + str(offer['amount']) + " for " +
                      str(offer['price_per_unit']))

            quantity -= offer['amount']
            print(quantity)

if rank == 1:
    quantity = comm.recv(source=0)
    for i in range(2, 5):
        comm.send(quantity, i)

if rank in range(2, 5):
    quantity = comm.recv(source=1)

    amount = random.randint(quantity - 50, quantity + 50)
    price_per_unit = round(random.uniform(1, 5), 2)  #RON

    offer = {'amount': amount, 'price_per_unit': price_per_unit}

    comm.send(offer, 0)

# for executing: mpiexec -np 5 python .\lab10\achizitii.py