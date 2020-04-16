#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    def divide(x,y):
        if y ==0:
            print("cannot divide 0!")
            return
        else:
            return x/y
    
    choice =input("Please choose:\n+,Plus\n-,Minus\n*,multiply\n/,divide\nPlease input:(+/-/*//):")
    num1 = float(input("First operand:"))
    num2 = float(input("Second Operand:"))
    if choice is '+':
        print("{}+{}={}".format(num1,num2,num1+num2))
    elif choice is '-':
        print("{}-{}={}".format(num1,num2,num1-num2))
    elif choice is '*':
        print("{}x{}={}".format(num1,num2,num1*num2))
    elif choice is '/':
        print("{}/{}={}".format(num1,num2,divide(num1,num2)))
    else:
        print("Illegal operator!!")
