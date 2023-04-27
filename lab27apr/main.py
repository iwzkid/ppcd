import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# departament_achizitii (rank1)
#     primeste de la manager rank 0 un ordin (int - caiete)
#     trimite celor 3 angajati rank 2,3,4 cererea de oferta

# angajatii rank 2,3,4
#     genereaza oferte 
#     trimit ofertele la manager

# manager
#     primeste ofertele

# MANAGER rank 0
if rank == 0:
    # send the nubmer of required q
    quantity = 100
    comm.send(quantity, 1)

    offers_list = []

    # receive offers
    for i in range(2,5):
        offers_list.append(comm.recv(source=i))

    sorted_offers = sorted(offers_list, key=lambda offer: offer['w_price'])

    quantity_var = quantity

    print(sorted_offers)

    for offer in sorted_offers:
        if quantity_var > 0:
            if offer['w_number'] >= quantity_var:
                print("Taking " + str(quantity_var) + " for " + str(offer['w_price']))
            else:
                print("Taking " + str(offer['w_number']) + " for " + str(offer['w_price']))
            quantity_var = quantity_var - offer['w_number']
        
if rank == 1:
    quantity = comm.recv(source=0)
    # let the employees know the quantity

    for i in range(2,5):
        comm.send(quantity, i)

# Employees 2,3,4
if rank in range(2,5):
    quantity = comm.recv(source=1)
    
    # we have to generate a combination of worksheets & price
    w_number = random.randint(35, 150)
    w_price = round(random.uniform(0.5, 5), 2)

    offer = {
        'w_number': w_number,
        'w_price': w_price
    }

    comm.send(offer, 0)
