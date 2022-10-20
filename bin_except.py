#Author: Faith Elledge
#Githubuser: elledgef
#Date:
#Description:

import unittest

class Error(Exception):
    """ Base class"""
    pass

class TargetNotFound(Error):
    """ When the target found is not a list """
    pass

def binary_search(a_list, target):
      """ Searches a_list fpr target
      if found, returns its location on the list
      if not found, TargetNotFound exception should pop up """

      first = 0
      last = len(a_list) -1
      while first <= last:
          middle = (first + last) //2
          if a_list[middle] == target:
              return middle
          if a_list[middle] > target:
              last = middle - 1
          else:
              first = middle + 1
      return TargetNotFound

