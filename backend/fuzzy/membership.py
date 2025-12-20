import numpy as np
import skfuzzy as fuzz

def tri(x,a,b,c):
    return fuzz.trimf(x,[a,b,c])

def trap(x,a,b,c,d):
    return fuzz.trapmf(x,[a,b,c,d])

def gauss(x,mean,sigma):
    return fuzz.gaussmf(x,mean,sigma)

def make_tri_set(universe,centers,width):
    out=[]
    n=len(centers)
    for i,ctr in enumerate(centers):
        left=ctr-width if i>0 else ctr-width
        right=ctr+width if i<n-1 else ctr+width
        a=left
        b=ctr
        c=right
        out.append(tri(universe,a,b,c))
    return out
