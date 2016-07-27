import unittest
import json
import urllib
from pprint import pprint
class FibonacciTestCase(unittest.TestCase):

  def test_start_0_length_1(self):
    startstring = '0'
    lengthstring = '1'
    url = 'http://localhost:5000/fibonacci?start=0&length=1'
    result = json.load(urllib.urlopen(url))
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "fibonacci" in str(result) and "[0]" in str(result):
      print('Test test_start_0_length_1 passed.')
    else:
      print('ERROR !!! Test test_start_0_length_1 FAILED.')
  
  def test_start_0_length_2(self):
    startstring = '0'
    lengthstring = '2'
    url = 'http://localhost:5000/fibonacci?start=0&length=2'
    result = json.load(urllib.urlopen(url))
    print(' ')
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "fibonacci" in str(result) and "[0, 1]" in str(result):
      print('Test test_start_0_length_2 passed.')
    else:
      print('ERROR !!! Test test_start_0_length_2 FAILED.')

  def test_start_0_length_3(self):
    startstring = '0'
    lengthstring = '3'
    url = 'http://localhost:5000/fibonacci?start=0&length=3'
    result = json.load(urllib.urlopen(url))
    print(' ')
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "fibonacci" in str(result) and "[0, 1, 1]" in str(result):
      print('Test test_start_0_length_3 passed.')
    else:
      print('ERROR !!! Test test_start_0_length_3 FAILED.')

  def test_start_0_length_4(self):
    startstring = '0'
    lengthstring = '4'
    url = 'http://localhost:5000/fibonacci?start=0&length=4'
    result = json.load(urllib.urlopen(url))
    print(' ')
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "fibonacci" in str(result) and "[0, 1, 1, 2]" in str(result):
      print('Test test_start_0_length_4 passed.')
    else:
      print('ERROR !!! Test test_start_0_length_4 FAILED.')

  def test_start_0_length_5(self):
    startstring = '0'
    lengthstring = '5'
    url = 'http://localhost:5000/fibonacci?start=0&length=5'
    result = json.load(urllib.urlopen(url))
    print(' ')
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "fibonacci" in str(result) and "[0, 1, 1, 2, 3]" in str(result):
      print('Test test_start_0_length_5 passed.')
    else:
      print('ERROR !!! Test test_start_0_length_5 FAILED.')

  def test_start_1_length_10(self):
    startstring = '1'
    lengthstring = '10'
    url = 'http://localhost:5000/fibonacci?start=1&length=10'
    result = json.load(urllib.urlopen(url))
    print(' ')
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "fibonacci" in str(result) and "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]" in str(result):
      print('Test test_start_1_length_10 passed.')
    else:
      print('ERROR !!! Test test_start_1_length_10 FAILED.')

  def test_start_1_length_0(self):
    startstring = '1'
    lengthstring = '0'
    url = 'http://localhost:5000/fibonacci?start=1&length=0'
    result = json.load(urllib.urlopen(url))
    print(' ')
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "error" in str(result) and "The \"length\" parameter can not be less than 1 (length >= 1)" in str(result):
      print('Test test_start_1_length_0 passed.')
    else:
      print('ERROR !!! Test test_start_1_length_0 FAILED.')

  def test_start_negative_1_length_0(self):
    startstring = '-1'
    lengthstring = '0'
    url = 'http://localhost:5000/fibonacci?start=-1&length=0'
    result = json.load(urllib.urlopen(url))
    print(' ')
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "error" in str(result) and "The \"start\" parameter can not be a negative number (start >= 0)" in str(result):
      print('Test test_start_negative_1_length_0 passed.')
    else:
      print('ERROR !!! Test test_start_negative_1_length_0 FAILED.')

  def test_start_negative_1_length_1(self):
    startstring = '-1'
    lengthstring = '1'
    url = 'http://localhost:5000/fibonacci?start=-1&length=1'
    result = json.load(urllib.urlopen(url))
    print(' ')
    print(str(startstring) + ' : ' + str(lengthstring) + ' : ' + str(result))
    if "error" in str(result) and "The \"start\" parameter can not be a negative number (start >= 0)" in str(result):
      print('Test test_start_negative_1_length_1 passed.')
    else:
      print('ERROR !!! Test test_start_negative_1_length_1 FAILED.')
  
if __name__ == '__main__':
  unittest.main()