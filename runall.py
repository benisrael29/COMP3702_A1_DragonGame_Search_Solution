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

def run_all(mode):
    in_files = ["./testcases/L1.txt",
                "./testcases/L2.txt",
                "./testcases/L3.txt",
                "./testcases/L4.txt",
                "./testcases/L5.txt",
                "./testcases/L6.txt",
                "./testcases/L7.txt",
                "./testcases/L8.txt"]
    
    out_files = ["./out/L1_out",
                 "./out/L2_out",
                 "./out/L3_out",
                 "./out/L4_out",
                 "./out/L5_out",
                 "./out/L6_out",
                 "./out/L7_out",
                 "./out/L8_out",]
    i=0
    l=0
    for file in in_files:
        if mode == 'ucs':
            solution([file, out_files[i], 'ucs'])
            tester([file, out_files[i]])
            time.sleep(5)
            visualiser([file, out_files[i]])
            i== i +1
        if mode == 'a_star':
            solution([file, out_files[l], 'a_star'])
            tester([file, out_files[l]])
            time.sleep(6)
            visualiser([file, out_files[l]])
            l== l +1

if __name__ == '__main__':
    run_all('a_star')