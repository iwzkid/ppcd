import random

from mpi4py import MPI


def random_1_6():
    
    
    return random.randint(1,6)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


match rank: 
        case 0:
            #Throm once.
            rank_0_throw_1 = random_1_6()
            #Print.
            print(f"Process {rank} throw 0 {rank_0_throw_1}.")
        
        case 1:
            #Throw twice.
            rank_1_throw_1 = random_1_6()
            print(f"Process {rank} throw 0 {rank_1_throw_1}.")
            rank_1_throw_2 = random_1_6()
            print(f"Process {rank} throw 0 {rank_1_throw_2}.")
            
            #Sum values.
            sum_rank_1 = rank_1_throw_1 + rank_1_throw_2
            
            print(f"Sum of values thrown by process {rank} is {sum_rank_1}).")
            
            
            
            
        case 2:
            #Throw twice.
            rank_2_throw_1 = random_1_6()
            print(f"Process {rank} throw 0 {rank_2_throw_1}.")
            rank_2_throw_2 = random_1_6()
            print(f"Process {rank} throw 0 {rank_2_throw_2}.")
            rank_2_throw_3 = random_1_6()
            print(f"Process {rank} throw 0 {rank_2_throw_3}.")
            
            #Sum values.
            sum_rank_2 = rank_2_throw_1 + rank_2_throw_2 + rank_2_throw_3
            
            print(f"Sum of values thrown by process {rank} is {sum_rank_2}).")
                
                
                
        
print(random_1_6())