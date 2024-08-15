import torch
from torch import nn

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
#torch.__version__
tensor_a=torch.tensor([3,4])
print(tensor_a,tensor_a.device)
tensor_a_on_gpu=tensor_a.to(device)
print(tensor_a_on_gpu, tensor_a_on_gpu.device)

#print(f"tensor's shape:{tensor_a.shape}")
tensor_rand_7_7= torch.rand([7,7])
print(f"tensor_7_7:{tensor_rand_7_7}")

tensor_rand_1_7= torch.rand([1,7])
print(f"tensor_1_7:{tensor_rand_1_7}")

tensor_mul= torch.matmul(tensor_rand_7_7,tensor_rand_1_7.T)
print(f"tensor_mul:{tensor_mul}")

RANDOM_SEED_1=0
torch.manual_seed(RANDOM_SEED_1)
tensor_rand_7_7= torch.rand([7,7])
print(f"tensor_7_7:{tensor_rand_7_7}")
#torch.manual_seed(RANDOM_SEED_1)
tensor_rand_1_7= torch.rand([1,7])
print(f"tensor_1_7:{tensor_rand_1_7}")

RANDOM_SEED_2=1234

torch.manual_seed(RANDOM_SEED_2).device


class abcd:
    def __init__(self,name='amd'):
        self.name=name
    def prt(self):
        print("hello")

class abcde(abcd):
    def __init__(self,age):
        self.age=age

class abcdef(abcd):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
a=abcd()
print(a.name)
b= abcde(10)
b.age
b.prt()
c= abcdef('intel',10)
c.name
c.age
c.prt()