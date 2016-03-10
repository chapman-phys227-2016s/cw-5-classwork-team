# PHYS227 CW 5

**Author(s):** Michael Seaman, Austin Ayers, Taylor Patti, Andrew Malfavon, Chinmai Raman

[![Build Status](https://travis-ci.org/chapman-phys227-2016s/cw-5-classwork-team.svg?branch=master)](https://travis-ci.org/chapman-phys227-2016s/cw-5-classwork-team)

**Due date:** 2016/03/08

## Specification

*Hint:* Work together on all class exercises this week.

Complete the following exercises from the primary textbook, placing your solutions into separate files. In each file, write the solution as a callable function, so that you can write suitable test functions that demonstrate correct output using the nose framework. GitHub will automatically run your tests on every commit, indicating any failures via the Travis framework with build status above.

1. Create the module ```calculus.py``` with functions ```discrete_func(f, a, b, n)``` (on p.644, vectorized version), ```diff(f, a, b, n)``` (on p.648, no plot), and ```trapezoidal(f, a, b, n)``` (on p.653). Test that they work as expected.
1. Create a vectorized version of a central finite difference. That is, given a discretized function f defined on a grid of points from i=0 to i=N with spacing h, the central difference is: (f_{i+1} - f_{i-1}) / (2h). Implement this central difference operation as a matrix product with f in order to vectorize it. What dimensions must this matrix have to produce the correct answer? Test your implementation to make sure it works correctly. How does this implementation compare with ```diff``` from the first exercise?
1. Create a vectorized version of a second-order central finite difference (i.e., repeat the finite difference above twice - what formula do you get?). Implement this second-order derivative as a matrix product with f in order to vectorize it. Is it the same thing as squaring the matrix from the previous exercise?
1. Create a vectorized version of the trapezoidal integration rule. That is, given a discretized function f defined as in the previous two exercises, define the integral as a matrix product with f in order to vectorize it. What dimensions must this matrix have to produce the correct answer? How does this implementation compare with ```trapezoidal``` from the first exercise?
1. Read the following abstract from the journal article [Diabetes Care 17, 152-154 (1994)](http://care.diabetesjournals.org/content/17/2/152.abstract).  Based on the abstract (and [paper](TaisMethod.pdf)), explain in your own words what the results of the author are, and how they relate to the material from this assignment. Note that according to the [ISI Web of Science](http://apps.webofknowledge.com/), this article has been cited 213 times since 1994, according to the chart below:
![Citation chart](citations.jpg)

To cleanly present your work, create a Jupyter notebook ```cw5.ipynb``` that imports each of your python files as modules and demonstrates the functionality. The notebook should be formatted professionally using Markdown headings, including your name and a brief description of each homework section. 

## Assessment

Good stuff. Hahaha, trap rule.

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Errbody
