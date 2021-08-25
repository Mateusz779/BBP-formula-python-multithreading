#
#   @Mateusz779
#
from decimal import Decimal
from decimal import getcontext
import time
from multiprocessing.dummy import Pool as Pool #pip3 install multiproces
from tqdm import tqdm #pip3 install tqdm

threads=4 #threads number
count = 10000 #number of numbers after the point

thread_list = []
count=count+1
list_all = {}
pbar = tqdm(total =count)

def pi(start):
    getcontext().prec=count-start
    for k in range (start,int(start+one_count)):
        pbar.update(1)
        list_all[k]=(1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)))  

start_table = []
if count >500:
    th=int(threads*(count/1000))
else:
    th=1
while count%th!=0:
    if count>th:
        th=th+1
    else:
        th=th-1

one_count=int(count/th)

for i in range(th):
    start_table.append(int((one_count*i)))

start = time.time()
with Pool(processes=threads) as pool:
    results = pool.starmap(
        pi, 
        iterable=zip(start_table),
        chunksize=100000 // threads
    )
end = time.time()
result=0
getcontext().prec=count
sort = sorted(list_all.items())
for i in sort:
    result=result+i[1]

print(Decimal(result))
print("\n\n")
print("Elapsed time: ",end - start,"s\n")