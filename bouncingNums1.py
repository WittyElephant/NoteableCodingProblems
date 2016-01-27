#https://www.hackerrank.com/contests/projecteuler/challenges/euler113
#given t = #of tests
#and t lines of the intiger n
#how many numbers below 10^n are non bouncy
#required to print the answer mod (10^+7)
import math
from operator import mul
def comb(n,r): # fast choose funtion I found online
    if r > n-r:  # for smaller intermediate values
        r = n-r
    return int( reduce( mul, range((n-r+1), n+1), 1) /
      reduce( mul, range(1,r+1), 1) )
def nonBounce(n):
    dec = comb(9+n,n)-2 #9 (1 to 9) possibilities for the first number, and n differnt sets to switch things around
						 # -2 for counting 0 and 00
    inc = comb(10+n,n)-n # 10 (0 to 9) possibilities, and n different sets
						 # - n for leading zeros
    return dec+inc-(9*n)
t = int(raw_input())
for i in range(t):
    div = (1000000007)
    n = int(raw_input())
    tot = int(nonBounce(n))
    a = tot/div
    print int(divmod(tot,div)[1])