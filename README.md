# Telenor code test

This repository contains the code for a code test done in preparation for an interview with Telenor.

### How to run:

Create a python environment with ```python>=3.10```, then run this command to install requirements:

```
pip install -r requirements.txt
```

To run the program:

```
python main.py
```

It is also possible to test with different number of *k*, here is an example with *k=5*:

```
python main.py --k 5
```


### Approach / Notes:

First thought was to use 4 for loops for checking horizontally, vertically, diagonally down left and diagonally down right. 
But to spare time, I used a for loop for the rows with a for loop for columns inside. This results in checking every index once(as starting point). To constrain the search, I used if-statements to avoid checking the edges when not necessary: 

1. last 3 numbers in row horizontally
2. last 3 numbers in column vertically
3. last 3 numbers in row and column for diagonal down right search
4. first 3 numbers and last 3 numbers for diagonal down left search.