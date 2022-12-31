import numpy as np

def vankin_max_score(input_file_path, output_file_path):
    with open(input_file_path) as infile:
        n = int(infile.readline())
        score = [[int(x) for x in line.split(',')] for line in infile]
        # print(n)
        # print(score)
        infile.close()

    x = np.empty([n, n], dtype=int)
    maxScore = 0
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == n - 1 and j == n - 1:
                x[i][j] = score[i][j]
                maxScore = x[i][j]
            elif i == n - 1: #last row
                x[i][j] = score[i][j] + max(x[i][j + 1], 0)
            elif j == n - 1: #last col
                x[i][j] = score[i][j] + max(x[i + 1][j], 0)
            else:
                x[i][j] = score[i][j] + max(x[i + 1][j], x[i][j + 1])

            maxScore = max(maxScore, x[i][j])
            # print(maxScore)

    out = open(output_file_path, "w")
    out.write(str(maxScore))
    out.close()

    #return maxScore

#vankin_max_score('test1000.in', 'test1000.out')