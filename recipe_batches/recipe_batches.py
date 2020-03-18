#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_items = []
  recipe_amounts = []
  inv_items = []
  inv_amounts = []
  for key, value in recipe.items():
    recipe_items.append(key)
    recipe_amounts.append(value)
  for key, value in ingredients.items():
    inv_items.append(key)
    inv_amounts.append(value)
  if not all(i in inv_items for i in recipe_items):
    return 0
  if all(i in inv_items for i in recipe_items):
    for i, j in zip(recipe_amounts, inv_amounts):
      if i > j:
        return 0
      if i < j:
        counts = []
        counts.append(j // i) 
        return min(counts) 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))