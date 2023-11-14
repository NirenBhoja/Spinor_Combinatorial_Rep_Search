# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:39:33 2023

This file contains a class SpinorRep that contains the structure of a Spinor. 
This class has contained methods to compute and validate certain representations against user 
provided constraints.

@author: Niren Bhoja & Harry Wells 
"""

import numpy as np
from itertools import combinations

class SpinorRep:   
     
    def __init__(self,num_rows,num_cols,col_sum_limit,row_sum_list,row_match_limit):
        self.N = num_rows
        self.M = num_cols
        self.K = col_sum_limit #column sum condition
        
        self.num_of_ones = row_sum_list
        self.lim_of_matches = row_match_limit
        
        self.table = np.ones((num_rows-1, num_cols), dtype = int)+np.zeros((1,self.M), dtype = int)
        self.temp_table = np.ones((num_rows-2,num_cols), dtype = int)
        
        for j in range(num_cols):
            
            self.temp_table[self.K[j]-1:,j] = 0
        
        
    def permute_columns(self):
        
        for col in range(self.M):
            permuted_indices = np.random.permutation(self.N-2)
            self.temp_table[:, col] = self.temp_table[permuted_indices, col]
        return
    
    def is_valid_rows(self):
        
        set_of_sums = set(np.sum(self.temp_table, axis=1))
        set_of_ones = set(self.num_of_ones)
        
        set_diff = set_of_sums.difference(set_of_ones)
        
        is_valid = True
        if set_diff:
            is_valid = False
            return is_valid
        
        return is_valid
    
    def is_matching_rows(self):
        
        for i, j in combinations(range(self.N-2), 2):
            
            row_i = self.temp_table[i][:]
            row_j = self.temp_table[j][:]
            
            counter = 0
            
            for k in range(self.M):
                
                counter += (row_i[k] == row_j[k])
                
                if counter >= self.lim_of_matches:
                    return False
                
        return True
                
    
    def compute_solution(self):
        
        is_valid = False
        counter = 0
        
        while not is_valid:
            
            self.permute_columns()
            is_valid = self.is_valid_rows()
            
            if not is_valid:
                continue
            
            is_valid = self.is_matching_rows()
            counter += 1
            print(counter)
            
        ones_row = np.ones((1,self.M), dtype = int)
        zero_row = np.zeros((1,self.M), dtype = int)
        self.table = np.vstack((ones_row, zero_row, self.temp_table))
        print(self.table)


"""
Example of a Spinor representation
"""

problem = SpinorRep(num_rows = 6, 
                    num_cols = 8,
                    col_sum_limit = [3,3,3,3,3,3,3,3], 
                    row_sum_list = [4], 
                    row_match_limit = 6)
problem.compute_solution()



        
