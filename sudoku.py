import re, solver, copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def print_puzzle(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j],end=" ")
        print()

unsolved = [[0 for i in range(9)] for i in range(9)]

browser = webdriver.Firefox()
browser.get('http://www.websudoku.com/?level=4')
browser.switch_to.frame(browser.find_element_by_xpath('html / frameset / frame'))

cells = browser.find_element_by_id('puzzle_grid').find_elements_by_tag_name('input')

for i,cell in enumerate(cells):
    value = cell.get_attribute('value')
    if value != '':
        unsolved[i//9][i%9]=int(value)

print("Unsolved puzzle:")
print_puzzle(unsolved)

solved = copy.deepcopy(unsolved)
if solver.solve_sudoku(solved):
    print("Solved puzzle:")
    print_puzzle(solved)
else:
    print('No solution exists')

for i,cell in enumerate(cells):
    cell.send_keys(str(solved[i//9][i%9]))

#clean this line
browser.find_elements_by_tag_name('input')[92].click()
