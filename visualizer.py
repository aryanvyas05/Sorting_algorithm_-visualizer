import matplotlib.pyplot as plt
import random

def set_plot_style():
    plt.style.use('dark_background')

def bubble_sort_visualizer(arr, bar_rects):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        update_bars(arr, bar_rects)
    plt.draw() 

def insertion_sort_visualizer(arr, bar_rects):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
        update_bars(arr, bar_rects)
    plt.draw() 

def update_bars(arr, bar_rects):
    for rect, h in zip(bar_rects, arr):
        rect.set_height(h)
    plt.draw() 
    plt.pause(0.05) 

def main():
    set_plot_style()
 
    arr = random.sample(range(1, 500), 200)
 
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge", color='white')
    ax.set_xlim(0, len(arr))
 
    bubble_sort_visualizer(arr, bar_rects)
     
    for rect in bar_rects:
        rect.set_height(0)
    
    arr = random.sample(range(1, 500), 200)
    for rect, h in zip(bar_rects, arr):
        rect.set_height(h)

    insertion_sort_visualizer(arr, bar_rects)

    plt.show()

main()
