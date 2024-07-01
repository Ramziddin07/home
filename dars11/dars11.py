with open('pi_millon.txt') as fayl:
    pi = fayl.read()

import pickle

talaba1 = pi


with open('info','wb') as file:
    pickle.dump(talaba1,file)



pi = float(pi)
print(pi)



