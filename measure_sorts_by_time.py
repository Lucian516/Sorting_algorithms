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
    bubble_times = []
    bubble2_times = []
    bubble3_times = []
    bubble4_times = []
    selection_times = []
    insertion_times = []
    for i in range(10,1000,10):
        arr = [random.randint(0, i**2) for x in range(i)]

        
        bubble_times.append(bubble(copy.deepcopy(arr))[0])
        bubble2_times.append(bubble2(copy.deepcopy(arr))[0])
        bubble3_times.append(bubble3(copy.deepcopy(arr))[0])
        bubble4_times.append(bubble4(copy.deepcopy(arr))[0])
        selection_times.append(selection(copy.deepcopy(arr))[0])
        insertion_times.append(insertion(copy.deepcopy(arr))[0])

    plt.plot(list_sizes, bubble_times, label="bubble", color="green")
    plt.plot(list_sizes, bubble2_times, label="bubble2", color="lime")
    plt.plot(list_sizes, bubble3_times, label="bubble3", color="yellow")
    plt.plot(list_sizes, bubble4_times, label="cocktail shaker", color="red")
    plt.plot(list_sizes, selection_times, label="selection", color="blue")
    plt.plot(list_sizes, insertion_times, label="insertion", color="purple")
    plt.legend()
    plt.show()
    return 

measure_sorts()