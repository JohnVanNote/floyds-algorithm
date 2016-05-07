#!usr/bin/python
#
# floyd.py
#
# Created by John Van Note
# Created on 03/06/12
#
# Implementation of Floyd's all pairs shortest path
# For more info review:
# http://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
#

import sys

# Global Sentinel for the highest distance possible between verticies
SENTINEL = sys.maxint

# createMatrix: Creates a BLANK matrix
# @param numRows is the number of rows, the number of columns is fine too
# @return a blank matrix (2-D list)
def createMatrix( numRows ):
  matrix = []
  for i in range( numRows ):
    col = []
    for j in range( numRows ):
      if i != j:
        col.append( SENTINEL )
      else:
        col.append( 0 )
    matrix.append( col )
  return matrix

# assignMatrix: Assigns values to a predecessor matrix
# @param matrix is the matrix to be assigned (2-D list)
# @param simPath is an array that comes from stdin
# no return (the matrix will be manipulated by reference)
def assignMatrix( matrix, simPath ):
  numRow = int( simPath[0] )
  simPath.remove( simPath[0] )
  for i in simPath:    
    numCol = int( i.split(',')[0] )
    dist = int( i.split(',')[1] )
    matrix[numRow][numCol] = dist
    # Since the graph is undirected we mirror this image
    matrix[numCol][numRow] = dist  

# floydMatrix: Creates Floyd-Warshall Matrix by implementing the Algorithm
# @param matrix is the matrix that needs the algorithm applied to (2-D list)
# no return (the matrix will be manipulated by reference)
def floydMatrix( matrix ):
  numRows = len( matrix )
  for k in range(0, numRows):
    for i in range(0, numRows):
      for j in range(0,numRows):
        matrix[i][j] = min( matrix[i][j], matrix[i][k]+matrix[k][j] )

# printMatrix: Formatted printing (to stdout) for a matrix
# @param matrix is the matrix to be printed
# no return
def printMatrix( matrix ):
  for i in matrix:
    for j in i:
      if j != SENTINEL:
        sys.stdout.write( '%4d' % j )
      else:
        sys.stdout.write( '%4s' % 'INF' )
    sys.stdout.write( '\n' )

# where the magic happens
def main():
  # Reads from stdin
  data = sys.stdin.readlines()
  # Creates a (empty) matrix
  numRows = 0
  for rows in data:
    numRows = numRows + 1
  matrix = createMatrix( numRows )
  # Assigns distance to predecessor matrix
  l = []
  for line in data:
    l.append( line.split() )
  for i in l:
    assignMatrix( matrix, i )
  # Prints predecesssor matrix (with foratting and whatnot)
  predMatrix = matrix
  sys.stdout.write( "Predecessor Matrix\n" )
  printMatrix( predMatrix )
  sys.stdout.write( '\n' )
  # Floyds up the matrix
  floydMatrix( matrix )
  # Prints finished matrix
  compMatrix = matrix
  sys.stdout.write( "All Pairs Shortest Path Matrix\n" )
  printMatrix( compMatrix )  

# this thing has to be here for Python reasons
if __name__ == '__main__':
  main() 

#eof 
