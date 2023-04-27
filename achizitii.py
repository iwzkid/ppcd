

import random
from pprint import pprint

import mpi4py.MPI
import time

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    #facem consent
    quantity = 100
    comm.send(quantity, 1)
    #trimite la procesul numarul 1
    offers = []

    for i in range(2, 5):
        offers.append(comm.recv(source=i))

    sorted_offers = sorted(offers, key=lambda x: x['price_per_unit'])
    pprint.pprint(sorted_offers)
    #print(offers)
    for offer in sorted_offers:
        if quantity > 0:
            if offer['amount'] >= quantity:
                 print("Taking " + str(quantity) + " for " + str(offer['price_per_unit']))
            else:
                print("Taking " + str(offer['amount']) + " for " + str(offer['price_per_unit']))

            quantity -= offer['amount']
            print(quantity)

if rank == 1:
    quantity = comm.recv(source = 0)

    for i in range(2, 5):
        comm.send(quantity, i)

##########Employees, // rank 2, 3 , 4.
if rank in range(2, 3):
    quantity = comm.recv(source = 1)

    #Generam oferta/combinatie
    amount = random(quantity-50, quantity+50)
    price_per_unit = round(random.uniform(1, 5), 2) #RON

    offer = {
        'amount' : amount,
        'price_per_unit' : price_per_unit
    }

    comm.send(offer, 0)
