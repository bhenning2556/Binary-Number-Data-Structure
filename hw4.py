'''
file: hw4.py
author: Benjamin Henning
project: ISTA 350 Hw4
created: 3/2/2020
purpose: This module contains code for a Binary object, which is a new data type to hold binary numbers. The object can be initilized with a string of a binary number, or left blank for a Binary number intialized to 0. The object stores the binary number in a 16-bit array. The class uses function overloading to implement the python operators =, +, -, <, abs(), int(), and str().
'''
import re
import numpy as np
import functools

@functools.total_ordering
class Binary:
    def __init__(self, string='0'):
        '''
        This constructor method takes a single argument, string, and makes a Binary object with one instance variable, bit_array. bit_array is 16 chars long and of type int. It holds the data from the argument string, padded with zeros on the left if the input string is less than 16 chars long. I used a Regular expression to check that the input string was no longer than 16 chars and only contained 0 or 1; A runtime error is raised if those conditions are not met. The bit_array is initialized to empty (16 zeroes) if the input string is it's default value, or an empty string.

        Parameters:
            string - default "0". A string holding only 0s or 1s to be put into the bit_array.
        '''
        p = re.compile(r'\A([01]{0,16})\Z')
        if not bool(p.match(string)):
            raise RuntimeError('Input string must contain only 0 and 1, and no longer than 16 chars. Could not parse {}'.format(string))

        self.bit_array = np.zeros(16, dtype=int)
        if string:
            if string[0] == "1":
                self.bit_array += 1
            for i in range(0, len(string)):
                self.bit_array[16 - len(string) + i] = int(string[i])

    def __eq__(self, other):
        '''
        This function overloads the "=" operator. it will iterate over the bit_array in self and other, and if there are any elements that aren't equal, the method will return False. If the whole bit_array is iterated over and all elements are the same, the method returns True.

        Returns: True or False.
        '''
        for i in range(0, 16):
            if self.bit_array[i] != other.bit_array[i]:
                return False
        return True

    def __repr__(self):
        '''
        Makes a string representation of a Binary object. The bit_array is iterated through and each number is concatenated to a string, which is returned.

        Returns: string.
        '''
        s = ''
        for item in self.bit_array:
            s += str(item)
        return s

    def __add__(self, other):
        '''
        This magic method overloads the "+" operator. The method performs binary addition by iterating over the two bit_arrays element by element, adding the summed elements to a 'result' bit_array, which is returned after the loop. If the result of the addition requires more than 16 bits, a RuntimeError is raised.

        Parameters:
            other - A Binary object to add to self.

        Returns: A new Binary object.
        '''
        result_num = np.empty(16, dtype=int)
        carry = 0
        
        for i in range(15, -1, -1):
            bit_sum = self.bit_array[i] + other.bit_array[i] + carry
            result_num[i] = bit_sum % 2
            carry = bit_sum > 1
            
        if self.bit_array[0] == other.bit_array[0] != result_num[0]:
            raise RuntimeError("Binary: overflow")
                
        return Binary(''.join([str(i) for i in result_num]))

    def __neg__(self):
        '''
        This method overloads the negation operator '-'. It returns a new Binary object representing the negation of self. The method uses a for loop to flip all the bits, then uses the add method to add 1 to complete the binary subtraction operation.

        Returns: A new Binary object.
        '''
        new_array = Binary()
        for i in range(0, 16):
            if self.bit_array[i] == 0:
                new_array.bit_array[i] = 1
            else:
                new_array.bit_array[i] = 0
        return new_array + Binary('0000000000000001')

    def __sub__(self, other):
        '''
        This method overloads the subtraction operator '-'. It uses the already established add and sub methods to return a new binary object representating the other object subtracted from the binary object.
        
        Parameters:
            other - A Binary object to subtract from self.

        Returns: a new Binary object.
        '''
        return Binary(str(self)) + (-Binary(str(other)))
    
    def __int__(self):
        '''
        This method overloads the int type operator. It returns an int representation of the binary number stored in bit_array.

        Returns: int
        '''
        array = self.bit_array
        neg = 1
        if self == Binary("1000000000000000"):
            return -32768
        if array[0] == 1:
            neg = -1
            array = (-Binary(str(self))).bit_array
        decimal = count = 0
        for i in range(15, -1, -1):
            decimal += array[i]*(2**count)
            count += 1
        return decimal.item() * neg

    def __lt__(self, other):
        '''
        This magic method compares two Binary objects. It returns true if the self object is less than the other object, and false if the self object is greater than or equal to the other object. My algorithm for this is pretty simple, first I check for negative numbers, then loop through both the bit_arrays, and at the first index in the arrays where the loop encounters a 1 in one of the arrays and a 0 in the other, it will return True or False. If the function loops through the whole array and there are no differences, than they are equal, in which case False will be returned.

        Parameters:
            other - A binary object to compare self to.
        
        Returns: True or False
        '''
        if self.bit_array[0] == 1 and other.bit_array[0] == 0:
            return True
        if self.bit_array[0] == 0 and other.bit_array[0] == 1:
            return False            
        for i in range(1, 16):
            if self.bit_array[i] < other.bit_array[i]:
                return True
            elif self.bit_array[i] > other.bit_array[i]:
                return False
        return False

    def __abs__(self):
        '''
        This method overloads the absolute value operator with a simple conditional statement.

        Returns: A new Binary object.
        '''
        if self.bit_array[0] == 0:
            return Binary(str(self))
        else:
            return -Binary(str(self))