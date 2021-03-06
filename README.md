﻿### Binary Number data structure
In this project, I created a new data structure called Binary. This data strcuture is an object which can be initilized with a string of a binary number, or left blank for a Binary number intialized to 0. The object stores the binary number in a 16-bit array. The class uses function overloading to implement the python operators =, +, -, <, abs(), int(), and str().

### Features
This project showcases some of my best software development skills and practices around object oriented programming, commenting and documentation, and algorithms.

### How to use
To test out the Binary class yourself, you can clone this repository to your local machine, and in the root directory of the repo create a new .py file. Then just write ```from hw4 import Binary```, and now you can use the Binary class to hold binary numbers and perform mathematical operations on them in your file. Initialize a new Binary object with ```myBinary = Binary()```. This will create a default 0 binary number. You can also create a Binary number from a string of 0s and 1s (up to 16 digits) by writing ```myBinary = Binary("0101010")```. Use simple operators to add, subtract, multiply and divide Binary objects, ex. ```result = Binary("01") + Binary("1010")```. You can also compare Binary objects with the equals operator, ex. ```Binary("01") == Binary("01")```.

## Credits
Developed by Benjamin Henning
