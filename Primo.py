# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:20:53 2021

@author: Samaung
"""

def primo(num):
    verificador=0
    contador=2
    for i in range(1, num-1):
        i=i+1
        resto=num%i #retorna o resto da divisão de num por i
        if (resto==0)&(verificador==0):
            print("O número {0} não é primo, pois é divisível por:".format(num))
            print(i)
            verificador=1
        elif (resto==0):
            print(i)
        else:
            contador=contador+1
    if contador==num:
        print("O número {0} é primo.".format(num))
        
    if num==1:
        print("O número 1 não é primo.")