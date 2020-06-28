#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:35:04 2019

@author: krishsapru
"""

#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.

    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

def avg_price(prices):
    """returns the avg price"""
    t = len(prices)
    total = 0
    for i in range(t):
        v = prices[i]
        total += v 
    avg = total/t
    return avg 

def std_dev(prices):
    """takes a lists and returns the standard deviation"""
    total = 0
    for i in range(len(prices)):
        t = prices[i] -  avg_price(prices)
        total += t ** 2 
    total = total / len(prices)
    result = math.sqrt(total)
    return result 

def max_day(prices):
    """ returns the day of the maximum price"""
    day = 0 
    for i in range(len(prices)):
        if prices[i] > prices[day]:
            day = i 
    return day 
    
def any_below(prices, n):
    """ uses a loop to determine threshold input"""
    for i in range(len(prices)):
        if prices[i] < n:
            return True 
    return False 

def find_plan(prices):
    """takes list and loops to find the best days to buy"""
    n = []
    buy = 0
    sell = 0
    profit = 0
    x = 0
    for i in range(len(prices)):
        rest = prices[i+1:]
        for j in range(len(rest)):
            d = rest[j] - prices[i]
            if d > profit:
                profit = d 
                x = rest[j]
                buy = i
    for y in range(len(prices)) :
        if prices[y] == x:
            sell = y 
    n = [buy] + [sell] + [profit]
    return n 


def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here

            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
