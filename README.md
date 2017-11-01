# Floyd-Warshall Algorithm

## Overview

This python program creates an all-pairs shortest path matrix determining the minimum distance between nodes in a weighted 
graph (known as the Floyd-Warshall algorithm). For more information on the algoritm specifically reference: 
http://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm.

## Usage

The input for the program is best done from a flat file, the file syntax is best shown viewing either example1.input or 
example2.input. The program parses the information, creates a predecessor (naive) matrix and then calculates the 
"all-pairs shortest path matrix".

Two examples of input of provided in example1.input and example2.input, both can be tested with the commands:
```make test1``` and ```make test2```,respectfully.

Taking input from the user directly can be done through ```make run``` but this is not recommended as it is easy to make a 
mistake entering input.

New input should be piped in from a file following the format in example1.input or example2.input.
