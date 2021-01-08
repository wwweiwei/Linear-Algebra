#Linear Algbra 2018 Assignment 2
# hw2_106070038_myfun import mydet, mysolve_cramer, mysolve_adj
from hw2_106070038_myfun import mydet,mysolve_adj,minor,mysolve_cramer
#import hw2_106070038_myfun 
import numpy as np
from datetime import datetime

A = np.array([[ 1.0,-1.0,-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
              [ 0.0, 0.0, 1.0,-1.0,-1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
              [ 4.0, 6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
              [ 0.0, 6.0,-1.0,-3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
              [ 0.0, 0.0, 0.0, 3.0,-2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
              [ 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,-1.0,-1.0, 0.0, 0.0],
              [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,-1.0,-1.0],
              [ 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 6.0, 0.0, 0.0, 0.0],
              [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0,-1.0,-3.0, 0.0],
              [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0,-2.0]])

b = np.array([[0.0],[0.0],[15.0],[0.0],[10.0],[0.0],[0.0],[0.0],[0.0],[10.0]])
n = A.shape[0]


# compute the determinant of A using numpy
tStart = datetime.now()
#for i in range(1,100):
W=np.linalg.det(A)
#print(np.linalg.det(A))
tEnd = datetime.now()
print("Using numpy,time to solve det is ", tEnd-tStart, " seconds.")

# compute the determinant of A using mydet
tStart = datetime.now()
#for i in range(0,100):
W=mydet(A)
#print(mydet(A))
tEnd = datetime.now()
print("Using mydet,time to solve det is ", (tEnd-tStart), " seconds.")

### your code write in hw2_StudentID_myfun.py ("mydet" function) ###

# solve the linear system and measure the execution time
tStart = datetime.now()
#for i in range(1,100):
x = np.linalg.solve(A, b)
#print(x)
tEnd = datetime.now()
print("Using np.linalg.solve, time to solve Ax=b is ", tEnd-tStart, " seconds.")

# check the correctness
#print("rediduals of np.linalg.solve")
res = np.subtract(np.dot(A, x), b)
#print(res)

# TODO 1. solve Ax=b using adjoint matrix (using mydet)
### your code write in hw2_StudentID_myfun.py ("mysolve_adj" function) ###
#execution time
tStart = datetime.now()
#for i in range(0,100):
x = mysolve_adj(A, b, mydet(A))
#print(x)
tEnd = datetime.now()
print("Using mysolve_adj, time to solve Ax=b is ", tEnd-tStart, " seconds.")
#print("rediduals of mysolve_adj")
res = np.subtract(np.dot(A, x), b)
#print(res)


# TODO 2. solve Ax=b using Cramer's rule (using mydet)
### yo3ur code write in hw2_StudentID_myfun.py ("mysolve_cramer" function) ###
# execution time
tStart = datetime.now()
#for i in range(0,100):
x = mysolve_cramer(A, b, mydet(A))
tEnd = datetime.now()
print("Cramer's rule, Execution Time = ", tEnd-tStart, " seconds.\n")
#print("rediduals of mysolve_cramer")
res = np.subtract(np.dot(A, x), b)
#print(res)

