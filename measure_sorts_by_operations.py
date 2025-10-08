#https://matplotlib.org/stable/tutorials/pyplot.html

import matplotlib.pyplot as plt
from bubble import bubble
from bubble import bubble2
from bubble import bubble3
from bubble import bubble4
from selection import selection
from insertion import insertion
import random
import copy


def measure_sorts():
    list_sizes = [n for n in range (10,1000,10)]
    bubble_operations = []
    bubble2_operations = []
    bubble3_operations = []
    bubble4_operations = []
    selection_operations = []
    insertion_operations = []
    for i in range(10,1000,10):
        arr = [random.randint(0, i**2) for x in range(i)]
        
        bubble_operations.append(bubble(copy.deepcopy(arr))[1])
        bubble2_operations.append(bubble2(copy.deepcopy(arr))[1])
        bubble3_operations.append(bubble3(copy.deepcopy(arr))[1])
        bubble4_operations.append(bubble4(copy.deepcopy(arr))[1])
        selection_operations.append(selection(copy.deepcopy(arr))[1])
        insertion_operations.append(insertion(copy.deepcopy(arr))[1])

    plt.plot(list_sizes, bubble_operations, label="bubble", color="green")
    plt.plot(list_sizes, bubble2_operations, label="bubble2", color="lime")
    plt.plot(list_sizes, bubble3_operations, label="bubble3", color="black")
    plt.plot(list_sizes, bubble4_operations, label="cocktail shaker", color="red")
    plt.plot(list_sizes, selection_operations, label="selection", color="blue")
    plt.plot(list_sizes, insertion_operations, label="insertion", color="purple")
    plt.legend()
    plt.show()
    return 

measure_sorts()