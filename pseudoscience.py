# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:16:18 2018

@author: Denny.Lehman
"""

#import pandas and numpy
import pandas as pd
import numpy as np



    
def main():
    
    
    #initialize test data
    
    mu = 238900
    personal_numbers = np.array([14,102329,1936,13])
    charm_numbers = np.array([-5,-4,-3,-2,-1,-1/2,-1/3,-1/4,0,1/4,1/3,1/2,1,2,3,4,5])
    error_tolerance = 0.01
    #initialize
    
    #min_err = calculate_error(deJager(personal_numbers,[charm_numbers[0],charm_numbers[0],charm_numbers[0],charm_numbers[0]]),mu)
    
    #greet user
    print( 'hello' )
    #ask for inputs
    #throw error if illegal input
    #evaluation
    #run optimizer
    optimize_deJager(mu,personal_numbers,charm_numbers,error_tolerance)
    


def optimize_deJager(mu,personal_numbers,charm_numbers,error_tolerance):
    best_answer = [charm_numbers[0],charm_numbers[0],charm_numbers[0],charm_numbers[0]]
    min_err = calculate_error(deJager(personal_numbers,best_answer),mu)
    for a in charm_numbers:
        #print(a)
        for b in charm_numbers:
            #print(b)
            for c in charm_numbers:
                #print(c)
                for d in charm_numbers:
                    #print(d)
                    #print(str(a) +' & ' +str(b)+' & '+str(c)+' & '+str(d))
                    charm_arr = np.array([a,b,c,d])
                    #print(charm_arr)
                    result = min_error_check(min_err,calculate_error(deJager(personal_numbers,charm_arr),mu))
                    min_err = result[0]
                    if result[1]:
                        best_answer = charm_arr
                        print(min_err)
    print()
    print('------------------------')
    print()
    print('best answer is:')
    print(best_answer)
    print('with an error of:')
    print(min_err)
    
    
def deJager(personal_numbers, charm_numbers):
    dj = personal_numbers[0]**charm_numbers[0]*personal_numbers[1]**charm_numbers[1]*personal_numbers[2]**charm_numbers[2]*personal_numbers[3]**charm_numbers[3]
    return dj

#error_tolerance
def calculate_error(deJager_val, mu_val):
    decimal_error = abs((deJager_val - mu_val))/mu_val
    return decimal_error

def min_error_check(old_error,new_error):
    swap = 0
    if new_error<old_error:
        old_error = new_error
        swap = 1
    return [old_error,swap]

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
