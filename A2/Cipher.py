#  File: Cipher.py

#  Description: This program will accept one normal message and one encrypted message. It will return two strings: the first one encrypted and the second one decrypted.  

#  Student Name: Xun Zhou

#  Student UT EID: xz7637

#  Partner Name: Siqi Xie

#  Partner UT EID: sx2564

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 09/11/2022

#  Date Last Modified: 09/12/2022

# Input: Two strings. The first string contains information to be encrypted, and the second string
#        contains an already encrypted message. 
# Output: returns an encrypted string and a decrypted string

import sys
import math
from re import I
from smtplib import OLDSTYLE_AUTH
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
  wid = len(strng)//2 + len(strng) % 2
  hei = len(strng) //2
  for newW in range(wid):
    for newH in range(hei):
      strng[newW][newH],strng[newH][-newW-1],strng[-newW-1][-newH-1],strng[-newH-1][newW] = strng[-newH-1][newW],strng[newW][newH],strng[newH][-newW-1],strng[-newW-1][-newH-1]
  return strng
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
  wid = len(strng)//2 + len(strng) % 2
  hei = len(strng) //2
  for newW in range(wid):
    for newH in range(hei):
      strng[newW][newH],strng[newH][-newW-1],strng[-newW-1][-newH-1],strng[-newH-1][newW] = strng[newH][-newW-1],strng[-newW-1][-newH-1],strng[-newH-1][newW],strng[newW][newH]
  return strng

def matrix_filling( strng_matrix, strng, dimnsion):
  counter = 0
  for i in range(dimnsion):
    for j in range(dimnsion):
      if counter != len(strng):
        strng_matrix [i][j] = strng[counter]
        counter += 1
      else:
        strng_matrix [i][j] = "*"
  return strng_matrix

def de_matrix_fill(strng_matrix, strng, dimnsion,a_num):
  counter = 0
  for j in range(dimnsion):
    for i in range(dimnsion-1,-1,-1):
      if a_num == 0:
        break
      else:
        strng_matrix [i][j] = "*"
        a_num -= 1
        
  for i in range(dimnsion):
    for j in range(dimnsion):
      if counter != len(strng):
        if strng_matrix[i][j] != "*":
          strng_matrix[i][j] = strng[counter]
          counter += 1
  return strng_matrix    

def display(strng):
  for i in strng:
    for j in i:
      if j != "*":
        print(j, end = "")
  

def main():
  # read the strings P and Q from standard input
  string1 = sys.stdin.readline().rstrip()
  string2 = sys.stdin.readline().rstrip()
  # print (string1 +"\n"+string2)
  
  length1 = math.ceil(math.sqrt(len(string1)))
  length2 = math.ceil(math.sqrt(len(string2)))
  input_string = [[ 'a' for i in range (length1)] for j in range (length1)] 
  output_string = [[ 'a' for i in range (length2)] for j in range (length2)]
  input_string = matrix_filling(input_string,string1,length1)
  output_string = de_matrix_fill(output_string,string2,length2,length2*length2-len(string2))
  # for i in input_string:
  #   print(i)  
  # # encrypt the string P
  input_string = encrypt(input_string)
  # print ("\n")
  # for i in input_string:
  #   print(i)  
  # print("\n")
  # for j in output_string:
  #   print(j)
  output_string = decrypt(output_string)
  
  # print("\n")
  # for j in output_string:
  #   print(j)
  
  # decrypt the string Q

  # print the encrypted string of P
  # and the decrypted string of Q
  display(input_string)
  print("")
  display(output_string)

if __name__ == "__main__":
  main()


