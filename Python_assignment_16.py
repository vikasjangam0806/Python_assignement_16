#Q-1 Python Program for Cycle Sort

def cycleSort(array):
   writes = 0
   # cycles to be rotated
   for cycleStart in range(0, len(array) - 1):
      item = array[cycleStart]
      #position to place the item
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
         if array[i] < item:
            pos += 1
      # if item exits, it is not a cycle
      if pos == cycleStart:
         continue
      # Otherwise, place the item
      while item == array[pos]:
         pos += 1
      array[pos], item = item, array[pos]
      writes += 1
      # rotation continued
      while pos != cycleStart:
         # Find a position to place the item
         pos = cycleStart
         for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
               pos += 1
         # place the item
         while item == array[pos]:
            pos += 1
         array[pos], item = item, array[pos]
         writes += 1
   return writes
# main
arr = [1,5,3,4,8,6,3,4,5]
n = len(arr)
cycleSort(arr)
print("Sorted array is : ")
for i in range(0, n) :
   print(arr[i], end = " ")

#Q-2 Python Program for Stooge Sort

def stoogesort(arr, l, h):
   if l >= h:
      return
   # swap
   if arr[l]>arr[h]:
      t = arr[l]
      arr[l] = arr[h]
      arr[h] = t
   # more than 2 elements
   if h-l+1 > 2:
      t = (int)((h-l+1)/3)
      # sort first 2/3 elements
      stoogesort(arr, l, (h-t))
      # sort last 2/3 elements
      stoogesort(arr, l+t, (h))
      # sort first 2/3 elements again
      stoogesort(arr, l, (h-t))
# main
arr = [1,4,2,3,6,5,8,7]
n = len(arr)
stoogesort(arr, 0, n-1)
print ("Sorted sequence is:")
for i in range(0, n):
   print(arr[i], end = " ")

#Q-3 Python Program to print the pattern ‘G’

def pattern(n):
    # rows
    for row in range(n): 
        # columns
        for col in range(n): 
            if ((row == 0 and (col != 0 and col != n-1)) or               
                (row == n - 1 and (col != 0 and col != n-1)) or                
                ((col == 0 and (row != 0 and row != n-1)) or                 
                 (col == n-1 and row != n-1 and row >= (n/2)-1)) or                
                (row == (n/2)-1 and ((n/2)-1 <= col < n-1))
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
# driver code
n = int(input("Enter the size you want: \t"))
if size < 8:
    print("Enter a size greater than 8")
else:
    pattern(n)

#Q-4 Python Program to print an Inverted Star Pattern

# python 3 code to print inverted star
# pattern 
  
# n is the number of rows in which
# star is going to be printed.
n=11
  
# i is going to be enabled to
# range between n-i t 0 with a
# decrement of 1 with each iteration.
# and in print function, for each iteration,
# ” ” is multiplied with n-i and ‘*’ is
# multiplied with i to create correct
# space before of the stars.
for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')


#Q-5 Python Program to print double sided stair-case pattern
# Python3 Program to demonstrate 
# staircase pattern
  
# function definition
def pattern(n):
  
    # for loop for rows
    for i in range(1,n+1):
  
        # conditional operator
        k =i + 1 if(i % 2 != 0) else i
  
        # for loop for printing spaces
        for g in range(k,n):
            if g>=k:
                print(end="  ")
  
        # according to value of k carry
        # out further operation
        for j in range(0,k):
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end = " ")
  
  
# Driver code
n = 10
pattern(n)

#Q-6 Python Program to print with your own font

# Python3 code to print input in your own font
 
name = "GEEK"
 
# To take input from User
# name = input("Enter your name: \n\n")
 
length = len(name)
l = ""
 
for x in range(0, length):
    c = name[x]
    c = c.upper()
     
    if (c == "A"):
        print("..######..\n..#....#..\n..######..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "B"):
        print("..######..\n..#....#..\n..#####...", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "C"):
        print("..######..\n..#.......\n..#.......", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "D"):
        print("..#####...\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..#####...\n\n")
         
    elif (c == "E"):
        print("..######..\n..#.......\n..#####...", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "F"):
        print("..######..\n..#.......\n..#####...", end = " ")
        print("\n..#.......\n..#.......\n\n")
         
    elif (c == "G"):
        print("..######..\n..#.......\n..#.####..", end = " ")
        print("\n..#....#..\n..#####...\n\n")
         
    elif (c == "H"):
        print("..#....#..\n..#....#..\n..######..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "I"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n....##....\n..######..\n\n")
         
    elif (c == "J"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n..#.##....\n..####....\n\n")
         
    elif (c == "K"):
        print("..#...#...\n..#..#....\n..##......", end = " ")
        print("\n..#..#....\n..#...#...\n\n")
         
    elif (c == "L"):
        print("..#.......\n..#.......\n..#.......", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "M"):
        print("..#....#..\n..##..##..\n..#.##.#..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "N"):
        print("..#....#..\n..##...#..\n..#.#..#..", end = " ")
        print("\n..#..#.#..\n..#...##..\n\n")
         
    elif (c == "O"):
        print("..######..\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "P"):
        print("..######..\n..#....#..\n..######..", end = " ")
        print("\n..#.......\n..#.......\n\n")
         
    elif (c == "Q"):
        print("..######..\n..#....#..\n..#.#..#..", end = " ")
        print("\n..#..#.#..\n..######..\n\n")
         
    elif (c == "R"):
        print("..######..\n..#....#..\n..#.##...", end = " ")
        print("\n..#...#...\n..#....#..\n\n")
         
    elif (c == "S"):
        print("..######..\n..#.......\n..######..", end = " ")
        print("\n.......#..\n..######..\n\n")
         
    elif (c == "T"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n....##....\n....##....\n\n")
         
    elif (c == "U"):
        print("..#....#..\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "V"):
        print("..#....#..\n..#....#..\n..#....#..", end = " ")
        print("\n...#..#...\n....##....\n\n")
         
    elif (c == "W"):
        print("..#....#..\n..#....#..\n..#.##.#..", end = " ")
        print("\n..##..##..\n..#....#..\n\n")
         
    elif (c == "X"):
        print("..#....#..\n...#..#...\n....##....", end = " ")
        print("\n...#..#...\n..#....#..\n\n")
         
    elif (c == "Y"):
        print("..#....#..\n...#..#...\n....##....", end = " ")
        print("\n....##....\n....##....\n\n")
         
    elif (c == "Z"):
        print("..######..\n......#...\n.....#....", end = " ")
        print("\n....#.....\n..######..\n\n")
         
    elif (c == " "):
        print("..........\n..........\n..........", end = " ")
        print("\n..........\n\n")
         
    elif (c == "."):
        print("----..----\n\n")


#Q-7 Get Current Date and Time using Python

# Python3 code to demonstrate 
# Getting current date and time using  
# now(). 
    
# importing datetime module for now() 
import datetime 
    
# using now() to get current time 
current_time = datetime.datetime.now() 
    
# Printing value of now. 
print ("Time now at greenwich meridian is : "
                                    , end = "") 
print (current_time) 

#Q-8 Python | Find yesterday’s, today’s and tomorrow’s date

# Python program to find yesterday,
# today and tomorrow
  
  
# Import datetime and timedelta
# class from datetime module
from datetime import datetime, timedelta
  
  
# Get today's date
presentday = datetime.now() # or presentday = datetime.today()
  
# Get Yesterday
yesterday = presentday - timedelta(1)
  
# Get Tomorrow
tomorrow = presentday + timedelta(1)
  
  
# strftime() is to format date according to
# the need by converting them to string
print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
print("Today = ", presentday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))

#Q-9 Python program to convert time from 12 hour to 24 hour format

# Python program to convert time
# from 12 hour to 24 hour format
  
# Function to convert the date format
def convert24(str1):
      
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
          
    # remove the AM    
    elif str1[-2:] == "AM":
        return str1[:-2]
      
    # Checking if last two elements of time
    # is PM and first two elements are 12   
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
          
    else:
          
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]
  
# Driver Code        
print(convert24("08:05:45 PM"))