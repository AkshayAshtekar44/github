#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" Author--  Akshay Ashtekar
    Date--   28/07/2018
    comment-- This code shows python advance concept
                Generators use.
"""

""" Summary:
           1) When you write a generator within a function then it becomes a generator function. 
	   2)The generator is used to optimized the memory usage and increases the execution speed. 
	   3) The major advantage of using generators is, it saves the state of generative function, thus We can reuse the previous state of 		     function.

"""

def process_generator(num_list):
    for num in num_list:
        yield num*num  #yield is used to return the value.

def optimized_generator(num_list):
    num_list = (x*x for x in num_list)  #when you iterate list in this way its become generator.
    for num in num_list:
        print "The square of Number is {}".format(num)

def main():
    num_list = [1,2,3,4,5,6,7,8]

    """ calling the generator function """
    processed_list = process_generator(num_list)

    """ print the next element using next()"""
    print processed_list.next()
    print processed_list.next()
    print processed_list.next()

    """ Calling optimized generator function"""
    optimized_generator(num_list)

    print processed_list.next()

    print "cloning repo....."

if __name__ == '__main__':
    main()
