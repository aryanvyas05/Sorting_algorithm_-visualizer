import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
BAR_WIDTH = 3
NUM_BARS = WIDTH // BAR_WIDTH

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")
clock = pygame.time.Clock()

def draw_bars(arr):
    screen.fill(BLACK) 
    for i, height in enumerate(arr):
        pygame.draw.rect(screen, WHITE, (i * BAR_WIDTH, HEIGHT - height, BAR_WIDTH, height))
    pygame.display.update()

def draw_single_bar(index, height, color=WHITE):
    pygame.draw.rect(screen, BLACK, (index * BAR_WIDTH, 0, BAR_WIDTH, HEIGHT))
    pygame.draw.rect(screen, color, (index * BAR_WIDTH, HEIGHT - height, BAR_WIDTH, height))
    pygame.display.update((index * BAR_WIDTH, 0, BAR_WIDTH, HEIGHT))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_single_bar(j, arr[j])
                draw_single_bar(j + 1, arr[j + 1])
                swapped = True
        pygame.event.pump()
        if not swapped:
            break
def insertion_sort(arr):
    for i in range(1, (len(arr))):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            draw_single_bar(j + 1, arr[j + 1])
            j -= 1
            pygame.event.pump()
        arr[j+1] = key
        draw_single_bar(j + 1, arr[j + 1])

def main():
    arr = random.sample(range(10, HEIGHT), NUM_BARS)
    print("Running Bubble Sort...")
    bubble_sort(arr)

    pygame.time.wait(2000)

    arr = random.sample(range(10, HEIGHT), NUM_BARS)
    print("Running Insertion Sort...")
    draw_bars(arr)
    insertion_sort(arr)

    pygame.time.wait(2000)

    pygame.quit()

main()
