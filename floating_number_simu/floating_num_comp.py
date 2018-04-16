# by jimmy shen
# Mar 11, 2018
# this code is used to compare the two floating number repre: 1) naive way  and 2)IEEE 

import numpy
import matplotlib.pyplot as plt

def get_naive_floating_numbers(a,b):
    """
    input : a number of bits for the integer parts
    input : b number of bits for the fraction parts.
    """
    non_neg_results = [i+j/float(2**b) for i in xrange(2**a)
                                       for j in xrange(2**b)]
    neg_results = [-_ for _ in non_neg_results]
    return sorted(neg_results+non_neg_results)

def get_ieee_floating_numbers(a,b):
    """
    input a: number of bits for the exp parts
    input b: number of bits for the fraction parts
    """
    bias = 2**(a-1)
    non_neg_results = [(1+j/float(2**b))*2**(i-bias) for i in xrange(2**a)
                                                  for j in xrange(2**b) ]
    neg_results = [-_ for _ in non_neg_results]
    return sorted(neg_results + non_neg_results)
if  __name__=="__main__":
    integer_bits, frac_bits = 7,5
    offset = 4    
    naive_floating = get_naive_floating_numbers( integer_bits+offset, frac_bits-offset)
    #print naive_floating
    ieee_floating  = get_ieee_floating_numbers ( integer_bits, frac_bits)
    # print ieee_floating
    print( "number of naive_floating, max,min",len(naive_floating),max(naive_floating), min(naive_floating))
    print "number of ieee_floating, max,min",len(ieee_floating),max(ieee_floating), min(ieee_floating)
    y = [1 for _ in xrange(len(naive_floating))]
    plt.scatter(naive_floating, y, color="#ff0000",s=10, alpha=0.99)
    z =  [10 for _ in xrange(len(ieee_floating))]
    plt.scatter(ieee_floating, z,color="#00ff00", s =10,alpha=0.3)
    plt.show()
    plt.close()
    plt.hist(naive_floating,bins = 100 , alpha=0.5)
    plt.show()
    plt.close()
    plt.hist(ieee_floating, bins=100, alpha=0.5)
    plt.show()
    plt.close()
