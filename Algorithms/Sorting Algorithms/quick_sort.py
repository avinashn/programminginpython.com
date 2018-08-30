#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 12:55:58 2018

@author: avinash
"""


def partition(lst, low, high):
    i = low - 1
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)


lst = []
size = int(input("Enter size of the list: \t"))
for i in range(size):
    element = int(input("Enter an element: \t"))
    lst.append(element)

low = 0
high = len(lst) - 1
quick_sort(lst, low, high)
print("The sorted list: \t", lst)
