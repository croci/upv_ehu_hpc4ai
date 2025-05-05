# NOTE: to be run with: mpiexec -n 2 xterm -e "ipython3 my_program.py"

from mpi4py import MPI
from time import sleep

comm = MPI.COMM_WORLD # this is the standard MPI communicator (there are others). It is the WORLD COMMUNICATOR, i.e. it allows to communicate across all processes.
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 1:
    while True:
        print("I am rank %d and I am stuck!" % rank, flush=True)
        sleep(3)
    
comm.barrier() # this causes a deadlock

print("I am rank: %d. There are: %d of us." % (rank,size), flush=True)
