import sys
import struct
import json

from AStar import *

'''
Note: Reverse GIMP coordinates
'''

def get_line(data):
    pos = 0
    while pos < len(data):
        if data[pos] == ord('\n'):
            break
        pos += 1
    
    if pos >= 0:
        return data[:pos], data[pos+1:]
    else:
        return None, data

def get_row(row_number, row_length, data):
    start = row_number * row_length
    end   = start + row_length
    return data[start:end]
def get_col(col_number, col_length, data):
    col = [0] * col_length
    for i in range(col_length):
        col[i] = data[i][col_number]
    return col

def save_board(board, max_color=255, filename='board_out.pgm'):
    f = open(filename, 'wb')
    
    height = len(board)
    width  = len(board[0])
    
    f.write('P5\n{} {}\n{}\n'.format(width, height, max_color).encode('utf-8'))
    print('Writing board: {}x{}'.format(width, height))
    for row in board:
        for col in row:
            f.write(struct.pack('B', col))
    f.close()

def parse_header(data):
    # P5\n# CREATOR: GIMP PNM Filter Version 1.1\n1518 1177\n255
    header, data = get_line(data)
    if header != b'P5':
        print('[-] Invalid header!')
        sys.exit(0)
    
    size, data = get_line(data)
    while size[0] == ord('#'):
        size, data = get_line(data)
    
    size = size.decode('utf-8').split(' ')
    
    map_width  = int(size[0])
    map_height = int(size[1])
    
    color, data = get_line(data)
    color = color.decode('utf-8')
    max_color  = int(color)
    
    return map_width, map_height, max_color, data

def initial_transform(board):
    # Convert board to binary
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != max_color: board[i][j] = 0
            else: board[i][j] = 255

def path_find(board, start_coord, end_coord):
    astar = AStar(board)
    node = astar.findPath(start_coord, end_coord)
    
    if not node:
        print('No path found')
        return None
    
    current = node
    path = []
    path_cost = 0
    while current:
        print('\tPoint: [{:0>2d}, {:0>2d}] | G: {:0>4d} | H: {:0>4d} | Cost: {:0>4d}'.format(current.point[0], current.point[1], current.g, current.h, current.getCost()))
        path.append(current.point)
        path_cost += current.getCost()
        current = current.parent
    print('Path Cost: {}'.format(path_cost))
    return node

# Do we need to display a usage???
if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1].find('-h') >= 0):
    print('usage: {} [options] ...'.format(sys.argv[0]))
    print('Only processes .PGM files')
    print('\timage contrast - [image-file]')
    print('\tpathfinding    - [path-file] [image-file] [start] [end]')
    sys.exit(0)

data = open(sys.argv[1], 'rb').read()
width, height, max_color, data = parse_header(data)

# Load board
board = []
for i in range(height-1):
    # Convert row to array
    board.append(list(get_row(i, width, data)))

if len(sys.argv) == 2:
    initial_transform(board)
elif len(sys.argv) >= 3:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] % 255:
                board[i][j] = 0
            else:
                board[i][j] = 1
    try:
        with open('mapping.json', 'r') as f:
            mappings = json.load(f)
    except:
        with open('./pgm/mapping.json', 'r') as f:
            mappings = json.load(f)

    start_room = sys.argv[3]
    end_room   = sys.argv[4]
    start = mappings[start_room[:2]][int(start_room[2])][start_room[2:]]
    end   = mappings[end_room[:2]][int(end_room[2])][end_room[2:]]
    
    if board[start[0]][start[1]] != 0 or board[end[0]][end[1]] != 0:
        print("Invalid points on path: ({}, {}):{}, ({}, {}):{}".format(start[0], start[1], board[start[0]][start[1]], end[0], end[1], board[end[0]][end[1]]))
        sys.exit(0)
    
    node = path_find(board, start, end)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                board[i][j] = 255

    data = open(sys.argv[2], 'rb').read()
    width, height, max_color, data = parse_header(data)

    # Load board
    board = []
    for i in range(height-1):
        # Convert row to array
        board.append(list(get_row(i, width, data)))

    current = node
    while current:
        y = current.point[0]
        x = current.point[1]

        LINE_SIZE = 10
        for i in range(-LINE_SIZE, LINE_SIZE+1):
            for j in range(-LINE_SIZE, LINE_SIZE+1):
                board[y+i][x+j] = 128

        current = current.parent

save_board(board)
