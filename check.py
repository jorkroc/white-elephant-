import numpy as np
seed=input("Please enter your answer to the question.")
np.random.seed(seed)
for i in range(np.random.randint(100)):
    np.random.randint(100)
check=np.random.randint(1000000000)
if (check!=432719002):
    print("Sorry, but that's not right.")
else:
    print("Correct!")
    np.random.seed(1209002624)
    secret="170445323320503534515771884184474844071802029372393273570298713318763319771291817636225987564920415974251063344295720571116224305633015005424773397146725352685408775837734807760141146164418196365983103925435387259953144964248535768109547698428158927940878972562877366632470887571379111432388737232744979434771343929424681194898548218"
    index=0
    print("Your code is: ", end='')
    for i in range(3):
        for i in range(4):
            index+=np.random.randint(1,10)
            print(secret[index], end='')
        print("-", end='')
    for i in range(4):
        index+=np.random.randint(1,10)
        print(secret[index], end="")
    print("!")
    
    print("The expiration date is ", end='')
    index+=np.random.randint(1,10)
    print(secret[index], end="")
    index+=np.random.randint(1,10)
    print(secret[index], end="/")
    index+=np.random.randint(1,10)
    print(secret[index], end="")
    index+=np.random.randint(1,10)
    print(secret[index], end=".\n")
    
    print("The security code is ", end='')
    index+=np.random.randint(1,10)
    print(secret[index], end="")
    index+=np.random.randint(1,10)
    print(secret[index], end="")
    index+=np.random.randint(1,10)
    print(secret[index], end=".\n")



