from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# import time


# Setup
SIZE_VALUE = '9'    # From 3 to 9
SHOW_BROWSER = False
fileName = "puzzle.txt"

# Selenium init
options = webdriver.ChromeOptions()
if not SHOW_BROWSER:
    options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://sumplete.com')
generated_html = driver.page_source


newPuzzle_button = driver.find_element(By.ID, "new")


# Solving first puzzle for open hidden menu
cheat_solve = driver.find_elements(By.CLASS_NAME, 'cell.number')
for div in cheat_solve:
    class_name = div.get_attribute('class')
    if class_name == 'cell number':
        div.click()
        # time.sleep(1)


# Checking puzzle size
select_size = Select(driver.find_element(By.ID, 'size'))
select_size.select_by_value(SIZE_VALUE)
newPuzzle_button.click()
# time.sleep(2)


# Parsing new puzzle datas
generated_html = driver.page_source
puzzlenumbers = driver.find_element(By.ID, 'grid').text.split('\n')
size = int(pow((len(puzzlenumbers) + 1), 1/2))

# Display puzzle
pn = puzzlenumbers
for i in range(size-1):
    row = pn[i*size:i*size+size-1]
    row_a = pn[i*size+size-1]
    row_str = "{:>5}" * (size-1) + "   |{:>3}"
    row_str = row_str.format(*row, row_a)
    print(row_str)

print("-" * (5 * size - 2))
row_a = pn[(size-1)*size:]
row_str = "{:>5}" * (size-1)
row_str = row_str.format(*row_a)
print(row_str)


# Saving into txt file
with open(fileName, 'w') as f:
    v_sums = pn[(size - 1) * size:]
    h_sums = []
    for i in range(1, size):
        h_sums.append(pn.pop(i * (size - 1)))
    puzzle = pn[:-9]
    f.write(','.join(puzzle) + '\n')
    f.write(','.join(h_sums) + '\n')
    f.write(','.join(v_sums) + '\n')


if SHOW_BROWSER:
    input()
driver.quit()
