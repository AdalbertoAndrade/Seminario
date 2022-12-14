# -*- coding: utf-8 -*-
"""Aula05_Seminario_II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YdMTCbfOmmAYDfjznxl3T27wq5k6E9jJ
"""

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    for i in range(left + 1, right + 1):
        item = arr[i]
        j = i - 1
        while j >= left and arr[j] > item:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = item

    return arr


def merge(left, right):
    left_pointer = right_pointer = 0
    left_len, right_len = len(left), len(right)
    result = []
    while left_pointer < left_len and right_pointer < right_len:
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    
    result.extend(
        left[left_pointer:] if left_pointer < left_len else right[right_pointer:]
    )
    return result


#Esse código foi extraído da url https://github.com/idostik/Timsort/blob/main/tim_sort.py
def tim_sort(arr):
    MIN_RUN = 32
    n = len(arr)

    for i in range(0, n, MIN_RUN):
        run = i + MIN_RUN
        insertion_sort(arr, i, run if run < n - 1 else n - 1)
    
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = start + size * 2 - 1 
            if end > n - 1:
                 end = n - 1
            
            merged_arr = merge(
                arr[start:mid + 1],
                arr[mid + 1:end + 1]
            )
            arr[start:start + len(merged_arr)] = merged_arr

        size *= 2
    
    return arr


#Créditos para https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
def mergesort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

#Créditos para https://stackoverflow.com/questions/18262306/quicksort-with-python
#nome original my_sort
def quicksort(A):
    #p=A[0]
    p=A[len(A)//2]          
    left=[]                                  
    right=[]                                     
    for i in range(1,len(A)):
       if A[i]< p:
         left.append(A[i])         
         if len(left)>1 and len(left)>=len(A)//2:          
            left=quicksort(left)                        
         elif A[i]>p: 
           right.append(A[i])                                
           if len(right)>1 and len(right)>=len(A)//2:        
              right=quicksort(right)
    A=left+[p]+right                                        
    return A

#Créditos para https://python-code.pro/heap-sort-algorithm/
def heapify(arr, n, i):
    # Finding largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    # Building max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)

#Créditos para https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      #print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue


def executa(tipo_ordenacao, num_exec, elementos, ordem):
  hora_inicio = "hora_do_inicio" + str(num_exec)
  tempoexec = 0
  for i in range(num_exec):
    hora_inicio = 0
    hora_inicio = time.time()
    tipo_ordenacao(elementos)
    tempoexec = tempoexec + (time.time() - hora_inicio)
    if ordem == 'a':
      ordenacao = 'ordem aleatória'
    else:
        if ordem == 'c':
          ordenacao = 'ordem crescente'
        else:
          ordenacao = 'ordem decrescente'
    print("Tempo da " + str(i) + " execução --- %s segundos ---" % (time.time() - hora_inicio) , " da " + str(tipo_ordenacao) + " para " + ordenacao)
  tempomedio = tempoexec/10
  print ("Tempo médio de 10 execuções da " + str(tipo_ordenacao) + " = " + str(tempomedio)+ " para " + ordenacao )

  
import random
import numpy as np
import time

if __name__ == '__main__':

    np.random.seed(32)
    ordem1 = list(range(0, 100000))
    ordem2 = list(range(0, 100000))
    ordem3 = list(range(0, 100000))
    random.shuffle(ordem1)
    ordem2.sort()
    ordem3.sort(reverse=True)
    ordem_aleatoria = np.array(ordem1)
    ordem_crescente = np.array(ordem2)
    ordem_decrescente = np.array(ordem3)

    #-------------- Seminário -----------------#
    executa(shellSort,10,ordem_aleatoria,'a')
    executa(shellSort,10,ordem_crescente,'c')
    executa(shellSort,10,ordem_decrescente,'d')

    executa(heapsort,10,ordem_aleatoria,'a')
    executa(heapsort,10,ordem_crescente,'c')
    executa(heapsort,10,ordem_decrescente,'d')

    executa(quicksort,10,ordem_aleatoria,'a')
    executa(quicksort,10,ordem_crescente,'c')
    executa(quicksort,10,ordem_decrescente,'d')

    executa(mergesort,10,ordem_aleatoria,'a')
    executa(mergesort,10,ordem_crescente,'c')
    executa(mergesort,10,ordem_decrescente,'d')

    executa(tim_sort,10,ordem_aleatoria,'a')
    executa(tim_sort,10,ordem_crescente,'c')
    executa(tim_sort,10,ordem_decrescente,'d')