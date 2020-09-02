import numpy as np
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

matrixA = []
for i in open("./matrixA.txt"):
    row = [int(x) for x in i.split(",")]
    matrixA.append(row)

matrixB = []
for j in open("./matrixB.txt"):
    row = [int(x) for x in j.split(",")]
    matrixB.append(row)

matrixA = np.array(matrixA)
matrixB = np.array(matrixB)

ans = matrixA.dot(matrixB)
ans.sort(axis=1)

np.savetxt("Q1_ans.txt", ans, fmt="%d", delimiter="\r\n")
