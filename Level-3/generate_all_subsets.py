#!/usr/bin/python

# Date: 2018-07-30
#
# Description:
# Write a method to return all subsets of a set.
#
# Approach:
# New subsets can be generated by adding new element to end of all currently
# generated sets like:
# Subsets of {a1, a2} => {}, {a1}, {a2}, {a1, a2} => P(2) so now subsets of
# {a1, a2, a3} => P(3) can be generated by adding a3 to each subset of P(2), so
# P(3) => P(2) + {a3} => {}, {a1}, {a2}, {a1, a2}, {a3}, {a1, a3}, {a2, a3}, {a1, a2, a3}.
#
# Complexity:
# Time: O(n*2^n)
# Space: O(n*2^n)

import copy

def generateAllSubsets(a, n):
  """Generates all subsets using elements given in list a.
  
  Args:
    a: List of elements.
    n: Number of elements in list a.
  """
  subsets = [set()]
  if not n:
    return subsets
 
  idx = 0
  while idx < n:
    newSubsets = copy.deepcopy(subsets)
    for new in newSubsets:
      new.add(a[idx])
    subsets.extend(newSubsets)
    idx += 1
  return subsets

def main():
  a = []
  n = input("Enter number of elements: ")
  for i in xrange(n):
      x = input("Enter value of a[%d] : " % i)
      a.append(x)

  subsets = generateAllSubsets(a, n)
  print "\nAll subsets are: "
  for i in range(len(subsets)):
    print "{idx}: {subset}".format(idx=i, subset=subsets[i])

if __name__ == '__main__':
  main()

# Output:
# *************************
# python generate_all_subsets.py 
# Enter number of elements: 2
# Enter value of a[0] : 1
# Enter value of a[1] : 2
# 
# All subsets are: 
# 0: set([])
# 1: set([1])
# 2: set([2])
# 3: set([1, 2])
#
# python generate_all_subsets.py 
# Enter number of elements: 3
# Enter value of a[0] : 1
# Enter value of a[1] : 2
# Enter value of a[2] : 3
# 
# All subsets are: 
# 0: set([])
# 1: set([1])
# 2: set([2])
# 3: set([1, 2])
# 4: set([3])
# 5: set([1, 3])
# 6: set([2, 3])
# 7: set([1, 2, 3])
