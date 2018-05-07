import torch
import time

start = time.time()

#dtype = torch.FloatTensor
dtype = torch.cuda.FloatTensor # Uncomment this to run on GPU
N = 300

# Create random input and output data
A = torch.randn(N, N).type(dtype)
B = torch.randn(N, N).type(dtype)

C = A*B
#print(A)
#print(B)
#print(C)
end = time.time()
print("I am done and the time used to execuate this code is:", end-start)
