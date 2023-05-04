import time
from random import randint
from mpi4py import MPI



comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()



match rank:
    case 0:
       
        messages = [comm.recv(source=proc) for proc in range(size) if proc != rank]
        total_time = time.strftime(     
            '%H:%M:%S',                 
            time.gmtime(sum(messages))  
        ).lstrip('00:').lstrip('00:')   

      
        print(f"It took a total of {total_time} for all {size - 1} teams to do all their work.")

   
    case _:
       
        time_start = time.time()
        time.sleep(randint(5, 20)) 
        time_end = time.time()
        time_elapsed = time_end - time_start

 
        comm.send(time_elapsed, dest=0)

        print(f"Process {rank} finished in {round(time_elapsed, 2)} seconds")
