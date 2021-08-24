# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 17:08:11 2021

@author: israe
"""
import sys
import time

from game_env import GameEnv
from solution import main as solution
from tester import main as tester
from visualiser import main as visualiser 

def run_all(mode, visualise):
    in_files = ["./testcases/L1.txt",
                "./testcases/L2.txt",
                "./testcases/L3.txt",
                "./testcases/L4.txt",
                "./testcases/L5.txt",
                "./testcases/L6.txt",
                "./testcases/L7.txt",
                "./testcases/L8.txt"]
    
    out_files = ["./out/L1_out.txt",
                 "./out/L2_out.txt",
                 "./out/L3_out.txt",
                 "./out/L4_out.txt",
                 "./out/L5_out.txt",
                 "./out/L6_out.txt",
                 "./out/L7_out.txt",
                 "./out/L8_out.txt"]
    
    i=0
    for file in in_files:
        if mode == 'ucs':
            t0 = time.time()
            print("Level %d:"% i)
            solution([file, out_files[i], 'ucs'])
            print("Time: %f" % (time.time()-t0))
            #tester([file, out_files[i]])
            if visualise == True:
                time.sleep(5)
                visualiser([file, out_files[i]])

        if mode == 'a_star':
            print("Level %d:"% i)
            t0 = time.time()
            solution([file, out_files[i], 'a_star'])
            print("Time: %f" % (time.time()-t0))
            tester([file, out_files[i]])
            if visualise == True:
                time.sleep(6)
                visualiser([file, out_files[i]])
        i += 1



if __name__ == '__main__':
    run_all('a_star', False)
    #run_all('ucs', False)