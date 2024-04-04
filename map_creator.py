from map import *
from combat_sys import *
def map1(size):
    n = size
    if (n >=30):
        k = n // 6
        l = n // 8
        my_map = Map(n, n)
        my_map.trees(11)
        my_map.canyon(1, n - 2, n, 0, n)
        my_map.quicksand(2, k, k + 20, k, k+20)
        my_map.passport(3, n*7//10, n*7//10+5, n*27//100, n*27//100+5)
        my_map.sword(4, l, l+5,  l*6, l*6+5)
        my_map.aliens_invasion(5, n*9//10, n*9//10+10, n//2-5, n//2+5)
        my_map.hunters_house(6, n*5//8-4, n*5//8+6, n//10, n//10+8)
        my_map.river(7, 0, l*2, l*2+2, l*3, l*3+21)
        my_map.river(7, 2, 0, l*2+2, l*3+20, l*5+22)
        my_map.river(7, 0, 0, 2, l*5+22, n)
        my_map.mountains(8, 0, 2, n*7//20+5, l*5+21)
        my_map.mountains(8, n//4, n, 0, 2)
        my_map.secta(9, k*4+5, k*4+15, k*4+5, k*4+15)
        my_map.ocean(10, 0, n, n-2, n)
        my_map.highway(12, 0, 4, 0, n*7//20+5)
        my_map.village(13, 0, n//4, 0, 3)
        my_map.simulation(14, n//2+17, n//2+21, 0, 2)
        my_map.enemy(15)


    else:
        my_map = Map(n, n)
        my_map.trees(6)
        my_map.canyon(1, n - 2, n, 0, n)
        my_map.quicksand(3, 2, 4, 2, 4)
        my_map.river(2, 2, 3, 9, 4, 8)
        my_map.secta(4, 5, 7, 5, 7)
        my_map.ocean(5, 0, n, n-1, n)
        my_map.highway(7, 0, 10, 0, 1)
        my_map.village(8, 0, 1, 0, 10)



    return (my_map)
