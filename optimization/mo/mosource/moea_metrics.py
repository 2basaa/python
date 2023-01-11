
"""
Computes the Coverage metric between two non-dominated sets A and B 
"""

import moea_base as moea

def cmetric(A,B):
    count = 0
    for b in B:
        for a in A:
            if moea.dominates(a,b):
                count += 1
                break
    return (count/len(B))