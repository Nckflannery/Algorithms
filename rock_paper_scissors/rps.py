#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  choices = [['rock'], ['paper'], ['scissors']]
  output = []
  # Base cases
  if n <= 0:
    return [[]]
  if n == 1:
    return choices
  looper = rock_paper_scissors(n-1)
  # Eventually rock_paper_scissors(n-1) will return choices, so:
  for i in looper:
    # iterate through choices
    for j in choices:
      # combine them
      k = i + j
      # append to output
      output.append(k)
  
  return output
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')