import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Zadanie 4
weights_list = [2**i for i in range(7, -1, -1)]
wagi = np.array(weights_list)
bin_count = np.random.randint(0, 2, 8)
def bin_value(weights, bin_count):
    return np.dot(weights, bin_count)
print("Weights:", wagi)
print("bin_count:", bin_count)
decimal_value = bin_value(wagi, bin_count)
print("Decimal value:", decimal_value)
#Zadanie 5
matrix = np.random.randint(0, 100, size=(5, 5))
max_value = matrix.max()
min_value = matrix.min()
max_in_rows = matrix.max(axis=1)
max_in_columns = matrix.max(axis=0)
sum_in_rows = matrix.sum(axis=1)
print(matrix)
print(max_value)
print(min_value)
print(max_in_rows)
print(max_in_columns)
print(sum_in_rows)
#Zadanie 6
#A
tablica_A = np.zeros((3, 3), dtype=int)
tablica_A[2, :] = 1
print("A:")
print(tablica_A)

#B
tablica_B = np.zeros((3, 3), dtype=int)
tablica_B[:, 1] = 1
print("\nB:")
print(tablica_B)

#C
tablica_C = np.zeros((3, 3), dtype=int)
tablica_C[1, :] = 1
print("\nC:")
print(tablica_C)

#D
tablica_D = np.zeros((3, 3), dtype=int)
tablica_D[:, 1] = 1 
tablica_D[1, :] = 1 
print("\nD:")
print(tablica_D)

#E
tablica_E = np.zeros((3, 3), dtype=int)
tablica_E[:, 1] = 1
tablica_E[2, :] = 1
print("\nE:")
print(tablica_E, "\n")

#Zad. 7
import math
m=[
    [0,1,0],
    [1,0,1],
    [0,1,0]
]
def rev(m):
    for i in range((len(m))**2):
        r=i%len(m)
        c=math.floor(i/len(m))
        if m[r][c]==0:
          m[r][c]=1
        else:
           m[r][c]=0
        if i==2 or i==5:
           c+=1
    return m
print(rev(m), "\n")
#Zad. 8
m = np.random.randint(0, 100, size=(5, 5))
print("Macierz 5x5:")
print(matrix)
wieksze_than_20 = matrix[matrix > 20]
count_wieksze_than_20 = wieksze_than_20.size
mean_value = matrix.mean()
print("\nElementy wieksze niż 20:", wieksze_than_20)
print("Liczba elementow wiekszych niz 20:", count_wieksze_than_20)
print("Srednia wartosc dla calej tablicy:", mean_value)