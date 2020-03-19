#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache={0:1, 1:1, 2:2}):
  # Recursive solution with caching
  # if n < 0:
  #   return 0
  # elif n == 0: 
  #   return 1
  if n in cache:
    return cache[n]
  else:
    cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cache[n]

# New method:
def eating_cookies_non_rec(n):

  if n == 0 or n == 1:
    return 1
  if n == 2:
    return 2
  # Our base cases are 0:1, 1:1, 2:2
  base = [1,1,2]
  # Notice that adding these gives 4, i.e. eating_cookies(3)
  # Notice sum(1, 2, 4) = 7, i.e. eating_cookies(4)
  # Notice sum(2, 4, 7) = 13, i.e. eating_cookies(5)
  # Instead of recursively calling the funciton, let's just store the
  # values in a list, base, and sum the last three elements
  # To get to this point, n > 2, so we iterate n-2 times
  for _ in range(2, n):
    cookies = base[-3] + base[-2] + base[-1]
    # Then append the new value to the end of the list to continue iteration
    base.append(cookies)
  ## Return the last element of the list
  ## return base[-1]
  # Easier to just return the variable cookies!
  return cookies 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')