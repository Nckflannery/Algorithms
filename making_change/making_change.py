#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # array to hold combinations for each amount
  combs = [0] * (amount + 1)
  # base case, i.e. for 0 amount, return 1
  combs[0] = 1

  # iterate through denominations
  for i in denominations:
    # then iterate through up to the amount to see which denoms can add up to the amount  
    for j in range(i, amount+1):
      if i <= j:
        combs[j] += combs[j - i]
  return combs[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")