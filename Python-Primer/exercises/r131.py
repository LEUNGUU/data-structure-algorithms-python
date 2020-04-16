#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ChangeMoney(m,n):
    money_type=(100,50,20,10,5,1,0.5,0.1)
    if m<n:
        print('needs more money to charge!')
        return
    elif m==n:
        print('no need to return money!')
        return
    else:
        result={}
        total=m-n
        for bill in money_type:
            num=total//bill
            result[str(bill)+' yuan']=int(num)
            total=total-num*bill
    return result


if __name__ == '__main__':
    print(ChangeMoney(100, 59.8))
