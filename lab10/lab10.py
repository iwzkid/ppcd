import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# MANAGER rank 0
if rank == 0:
    quantity = 100
    comm.send(quantity, 1)

    offers_list = []

    for i in range(2,5):
        offers_list.append(comm.recv(source=i))

    sorted_offers = sorted(offers_list, key=lambda offer: offer['w_price'])

    quantity_var = quantity
    final_price = 0
    good_offers = []

    print(sorted_offers)

    for offer in sorted_offers:
        if quantity_var > 0:
            if offer['w_number'] >= quantity_var:
                print(f"Taking " + str(quantity_var) + " for " + str(offer['w_price']))
                final_price = final_price + quantity_var * offer['w_price']
                good_offers.append({"w_number": quantity_var, "w_price": offer['w_price']})
            else:
                print("Taking " + str(offer['w_number']) + " for " + str(offer['w_price']))
                final_price = final_price + offer['w_number'] * offer['w_price']
                good_offers.append({"w_number": offer['w_number'], "w_price": offer['w_price']})

            quantity_var = quantity_var - offer['w_number']

    print(good_offers)
    print(round(final_price, 2))

if rank == 1:
    quantity = comm.recv(source=0)

    for i in range(2,5):
        comm.send(quantity, i)

# Employees 2,3,4
if rank in range(2,5):
    quantity = comm.recv(source=1)

    w_number = random.randint(35, 150)
    w_price = round(random.uniform(0.5, 5), 2)

    offer = {
        'w_number': w_number,
        'w_price': w_price
    }

    comm.send(offer, 0)