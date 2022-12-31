'''
    This file contains the template for Assignment3.  For testing it, I will place it
    in a different directory, call the function <vidrach_itky_leda>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

import sys

def vidrach_itky_leda(input_file_path, output_file_path):
    '''
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''
    with open(input_file_path) as infile:
        n = int(infile.readline())
        board = [[int(x) for x in line.split(',')] for line in infile]
        infile.close()
        
        
    # red,   blue
    start_phase, dest_phase = [[0, 0], [n-1, n-1]], [[n-1, n-1], [0,0]]
    queue = [start_phase]
    visited = [ False for i in range(n*n*n*n) ]
    
    counter = 0
    
    while(queue):
        cur_phase_size = len(queue)
        
        # Check the same layer 
        for i in range(cur_phase_size):
            vertex = queue.pop(0)
            red_x, red_y = vertex[0]
            blue_x, blue_y = vertex[1]
            red_val , blue_val = board[red_x][red_y], board[blue_x][blue_y]
            
            # Move point
            if not visited[red_x*n*n*n+red_y*n*n+blue_x*n+blue_y]:
                visited[red_x*n*n*n+red_y*n*n+blue_x*n+blue_y] = True
                #move red check four directions
                # down
                if (
                        red_x+blue_val < n and 
                        not (red_x+blue_val == blue_x and red_y == blue_y) 
                    ): 
                    queue.append([[red_x+blue_val, red_y], [blue_x, blue_y]])
                    # Check if a phase is dest
                    if [[red_x+blue_val, red_y], [blue_x, blue_y]] == dest_phase:
                        counter += 1
                        out = open(output_file_path, "w")
                        out.write(str(counter))
                        out.close()
                        sys.exit()
                        break
                # up
                if (
                        red_x-blue_val >= 0 and
                        not (red_x-blue_val == blue_x and red_y == blue_y) 
                    ): 
                    queue.append([[red_x-blue_val, red_y], [blue_x, blue_y]])
                    # Check if a phase is dest
                    if [[red_x-blue_val, red_y], [blue_x, blue_y]] == dest_phase:
                        counter += 1
                        out = open(output_file_path, "w")
                        out.write(str(counter))
                        out.close()
                        sys.exit()
                        break
                # right
                if (
                        red_y+blue_val < n and
                        not (red_x == blue_x and red_y+blue_val == blue_y)
                    ):
                    queue.append([[red_x, red_y+blue_val], [blue_x, blue_y]])
                    # Check if a phase is dest
                    if [[red_x, red_y+blue_val], [blue_x, blue_y]] == dest_phase:
                        counter += 1
                        out = open(output_file_path, "w")
                        out.write(str(counter))
                        out.close()
                        sys.exit()
                        break
                # left
                if (
                        red_y-blue_val >= 0 and
                        not (red_x == blue_x and red_y-blue_val == blue_y)
                    ):
                    queue.append([[red_x, red_y-blue_val], [blue_x, blue_y]])
                    # Check if a phase is dest
                    if [[red_x, red_y-blue_val], [blue_x, blue_y]] == dest_phase:
                        counter += 1
                        out = open(output_file_path, "w")
                        out.write(str(counter))
                        out.close()
                        sys.exit()
                        break
                
                #move blue check four directions
                # down
                if (
                        blue_x + red_val < n and 
                        not (blue_x+red_val == red_x and blue_y == red_y)
                    ):
                    queue.append([[red_x, red_y], [blue_x+red_val, blue_y]])
                    # Check if a phase is dest
                    if [[red_x, red_y], [blue_x+red_val, blue_y]] == dest_phase:
                        counter += 1
                        out = open(output_file_path, "w")
                        out.write(str(counter))
                        out.close()
                        sys.exit()
                        break
                # up
                if (
                        blue_x - red_val >= 0 and 
                        not (blue_x-red_val == red_x and blue_y == red_y)
                    ):
                    queue.append([[red_x, red_y], [blue_x-red_val, blue_y]])
                    # Check if a phase is dest
                    if [[red_x, red_y], [blue_x-red_val, blue_y]] == dest_phase:
                        counter += 1
                        out = open(output_file_path, "w")
                        out.write(str(counter))
                        out.close()
                        sys.exit()
                        break
                # right
                if (
                        blue_y + red_val < n and 
                        not (blue_x == red_x and blue_y+red_val == red_y)
                    ):
                    queue.append([[red_x, red_y], [blue_x, blue_y+red_val]])
                    # Check if a phase is dest
                    if [[red_x, red_y], [blue_x, blue_y+red_val]] == dest_phase:
                        counter += 1
                        out = open(output_file_path, "w")
                        out.write(str(counter))
                        out.close()
                        sys.exit()
                        break
                # left
                if (
                        blue_y - red_val >= 0 and 
                        not (blue_x == red_x and blue_y-red_val == red_y)
                    ):
                    queue.append([[red_x, red_y], [blue_x, blue_y-red_val]])
                    # Check if a phase is dest
                    if [[red_x, red_y], [blue_x, blue_y-red_val]] == dest_phase:
                        counter += 1
                        out = open(output_file_path, "w")
                        out.write(str(counter))
                        out.close()
                        sys.exit()
                        break
        
        counter += 1     
    
    out = open(output_file_path, "w")
    out.write(str(-1))
    out.close()
    
    pass

vidrach_itky_leda('input0.in', 'input0.out')
