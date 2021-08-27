#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: Mateusz779

"""
from decimal import Decimal
from decimal import getcontext
import time
from multiprocessing.dummy import Pool as Pool
from tqdm import tqdm 
import argparse

def pi(start):
    getcontext().prec=count-start
    for k in range (start,int(start+one_count)):
        pbar.update(1)
        list_all[k]=(1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)))  

def main():
    global count
    global pbar
    global list_all
    global tasks
    global one_count
    parser = argparse.ArgumentParser(description='The script computes the number pi.')
    parser.add_argument('-t', '--threads', help="Number of threads default 4", required=False,type=int, default=4)
    parser.add_argument('-c', '--count', help="Number of numbers after the point default 10000", required=False,type=int, default=10000)
    parser.add_argument('-f', '--filename', help="File to save result", required=False)
    args = parser.parse_args()

    threads=args.threads
    count = args.count #number of numbers after the point

    start_table = []
    if count > 500:
        tasks=int(threads*(count/1000))
    else:
        tasks=1
    count=count+1
    list_all = {}
    pbar = tqdm(total = count)
    one_count=int(count/tasks)
    start_table = [int((one_count * i)) for i in range(tasks)]

    
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
    if args.filename!=None:
        f = open(args.filename, "w")
        f.write(str(Decimal(result)))
        f.close()
if __name__ == "__main__":
    main()








