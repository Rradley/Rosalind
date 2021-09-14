# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:03:53 2021

@author: rob
"""
def DPCHANGE (money,coins):
    minimumNoCoins = [0]*(money + 1)
        
    for i in range (1,money + 1):
        minimumNoCoins[i] = 999999999999999
        for j in range (0,len(coins)):            
            #IF the value of money is greater than the current denomination coin
            if i >= coins[j]:                             
                #IF minNoCoin[i] - current coin + 1 is less than current minNoCoin, Current = new
                if (minimumNoCoins[i - coins[j]] + 1 ) < minimumNoCoins[i]:
                    minimumNoCoins[i] = minimumNoCoins[i - coins[j]] + 1
            
    #return minimumNoCoins
    return minimumNoCoins[money]

money = 16813
coins = [1,3,5,12,14,22]

print(DPCHANGE(money, coins))