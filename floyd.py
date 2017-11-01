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


# Sentinel for the highest distance possible between vertices
def get_sentinel():
  return sys.maxint


# createMatrix: Creates a BLANK matrix
# @param numRows is the number of rows, the number of columns is fine too
# @return a blank matrix (2-D list)
def create_matrix(numRows):
  sentinel = get_sentinel()
  matrix = []
  for i in range(numRows):
    col = []
    for j in range(numRows):
      if i != j:
        col.append(sentinel)
      else:
        col.append(0)
    matrix.append(col)
  return matrix


# assignMatrix: Assigns values to a predecessor matrix
# @param matrix is the matrix to be assigned (2-D list)
# @param simPath is an array that comes from stdin
# no return (the matrix will be manipulated by reference)
def assign_matrix(matrix, sim_path):
  num_row = int(sim_path[0])
  sim_path.remove(sim_path[0])
  for i in sim_path:
    num_col = int(i.split(',')[0])
    dist = int(i.split(',')[1])
    matrix[num_row][num_col] = dist
    # Since the graph is undirected we mirror this image
    matrix[num_col][num_row] = dist


# floydMatrix: Creates Floyd-Warshall Matrix by implementing the Algorithm
# @param matrix is the matrix that needs the algorithm applied to (2-D list)
# no return (the matrix will be manipulated by reference)
def floyd_matrix(matrix):
  num_rows = len(matrix)
  for k in range(0, num_rows):
    for i in range(0, num_rows):
      for j in range(0,num_rows):
        matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])


# printMatrix: Formatted printing (to stdout) for a matrix
# @param matrix is the matrix to be printed
# no return
def print_matrix(matrix):
  sentinel = get_sentinel()
  for i in matrix:
    for j in i:
      if j != sentinel:
        sys.stdout.write('%4d' % j)
      else:
        sys.stdout.write('%4s' % 'INF')
    sys.stdout.write('\n')


# where the magic happens
def main():
  # Reads from stdin
  data = sys.stdin.readlines()
  # Creates a (empty) matrix
  num_rows = 0
  for rows in data:
    num_rows = num_rows + 1
  matrix = create_matrix(num_rows)
  # Assigns distance to predecessor matrix
  l = []
  for line in data:
    l.append(line.split())
  for i in l:
    assign_matrix(matrix, i)
  # Prints predecessor matrix (with formatting and whatnot)
  pred_matrix = matrix
  sys.stdout.write("Predecessor Matrix\n")
  print_matrix(pred_matrix)
  sys.stdout.write('\n')
  # Floyds up the matrix
  floyd_matrix(matrix)
  # Prints finished matrix
  comp_matrix = matrix
  sys.stdout.write('All Pairs Shortest Path Matrix\n')
  print_matrix(comp_matrix)


# this thing has to be here for Python reasons
if __name__ == '__main__':
  main()
