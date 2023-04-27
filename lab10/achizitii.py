import random
import pprint

from mpi4py import MPI

# MPI Variables.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Manager. // Rank 0.
if rank == 0:
    # Let acquisitions know of the required q.
    quantity = 100
    comm.send(quantity, 1)  # Acquisitions is rank 1.

    offers = []
    # Receive offers.
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
                print("Taking " + str(offer['amount']) +
                      " for " + str(offer['price_per_unit']))

            quantity -= offer['amount']
            print(quantity)

# Acquisitions. // Rank 1.
if rank == 1:
    quantity = comm.recv(source=0)
    # Let employees know the quantity.
    for i in range(2, 5):
        comm.send(quantity, i)

# Employees. // Ranks 2, 3, 4.
if rank in range(2, 5):
    quantity = comm.recv(source=1)

    # Generat oferta / combinatie.
    amount = random.randint(quantity-50, quantity+50)
    price_per_unit = round(random.uniform(1, 5), 2)  # RON

    offer = {
        'amount': amount,
        'price_per_unit': price_per_unit
    }

    comm.send(offer, 0)

# Exemplu:
# Oferta 1: (25, 1)
# Oferta 2: (2000, 2)
# Oferta 3: (50, 1.5)
# Managerul alege combinaţia: 25 caiete la 1 leu + 50 caiete la 1.5 lei + 25 caiete la 2 lei, pret total: 25+75+50=150 lei