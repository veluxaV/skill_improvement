fileName = "puzzle.txt"

with open(fileName, 'r') as f:
    puzzle_datas = f.readline().strip().split(',')
    h_sums = f.readline().strip().split(',')
    v_sums = f.readline().strip().split(',')

puzzle_array = []
size = int(pow(len(puzzle_datas), 1 / 2))
for i in range(size):
    puzzle_array.append(puzzle_datas[i * size:i * size + size])


def displayPuzzle(puzzle, h, v):
    for i in range(size):
        row_str = ("{:>5}" * size + "  | {:>3}").format(*puzzle[i], h[i])
        print(row_str)
    print("-" * (5 * size + 2))
    row_str = ("{:>5}" * size).format(*v)
    print(row_str)


displayPuzzle(puzzle_array, h_sums, v_sums)


def solve():
    pass    # TODO
