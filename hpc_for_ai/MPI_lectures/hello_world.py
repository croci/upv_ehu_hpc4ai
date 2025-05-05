from mpi4py import MPI

comm = MPI.COMM_WORLD # this is the standard MPI communicator (there are others). It is the WORLD COMMUNICATOR, i.e. it allows to communicate across all processes.
rank = comm.Get_rank()
size = comm.Get_size()

print("I am rank: %d. There are: %d of us." % (rank,size), flush=True)
