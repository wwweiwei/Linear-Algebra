# Linear Algebra 2018 Assignment 3

import numpy as np
import matplotlib.pyplot as plt
import math as m

# 10 points of a cube
t1=(m.sqrt(5)+1)/2
t2=(m.sqrt(5)-1)/2

points = np.array([[ 0,          0,m.sqrt(t1/m.sqrt(5)),m.sqrt(t2/m.sqrt(5)),-m.sqrt(t2/m.sqrt(5)),-m.sqrt(t1/m.sqrt(5)), 0,           0,-m.sqrt(t1/m.sqrt(5)),-m.sqrt(t2/m.sqrt(5)),m.sqrt(t2/m.sqrt(5)),m.sqrt(t1/m.sqrt(5))],
                   [ 1,1/m.sqrt(5),         1/m.sqrt(5),         1/m.sqrt(5),          1/m.sqrt(5),          1/m.sqrt(5),-1,-1/m.sqrt(5),         -1/m.sqrt(5),         -1/m.sqrt(5),        -1/m.sqrt(5),        -1/m.sqrt(5)],
                   [ 0,2/m.sqrt(5),        t2/m.sqrt(5),       -t1/m.sqrt(5),        -t1/m.sqrt(5),         t2/m.sqrt(5), 0,-2/m.sqrt(5),        -t2/m.sqrt(5),         t1/m.sqrt(5),        t1/m.sqrt(5),      -t2/m.sqrt(5)]])
edges = [[2,1,0],[0,2,3],[0,3,4],[0,4,5],[0,5,1],
         [1,10,2],[2,11,3],[3,7,4],[4,8,5],[5,9,1],
         [6,8,7],[6,9,8],[6,10,9],[6,11,10],[6,7,11],
         [7,8,4],[8,9,5],[9,10,1],[10,11,2],[11,7,3]]

def plotcube1(pt,name):
    """plot a cube described by pt. 
       T is the transition matrix that maps objects from a 3D space to a 2D screen.
       The viewport is at [1/2, 1/2, sqrt(2)/2]"""
    T = np.array([[m.sqrt(2)/m.sqrt(3), 0, -1/m.sqrt(3)],
                  [-1/m.sqrt(12),  m.sqrt(3)/2, -1/m.sqrt(6)]])
    
    def drawAxis():
        """ draw the axes of the 3D space"""
        X = np.dot(T, [[0,1.5],[0,0],[0,0]])
        Y = np.dot(T, [[0,0],[0,1.5],[0,0]])
        Z = np.dot(T, [[0,0],[0,0],[0,1.5]])
        plt.plot(X[0,:], X[1,:], 'b:')
        plt.plot(Y[0,:], Y[1,:], 'b:')
        plt.plot(Z[0,:], Z[1,:], 'b:')
        plt.text(X[0,1], X[1,1], r'x', fontsize=20)
        plt.text(Y[0,1], Y[1,1], r'y', fontsize=20)
        plt.text(Z[0,1]-0.1, Z[1,1], r'z', fontsize=20)

    def visible(p1, p2, p3):
        """output if the face is visible."""
        # write your code here...
        # a=p2-p1
        # b=p3-p1
        # c=np.cross(a,b)
        a=pt[:,p2]-pt[:,p1]
        b=pt[:,p3]-pt[:,p1]
        c=np.cross(a,b)
        d=np.inner(c,[1/2, 1/2, m.sqrt(2)/2])
        #print(a)
        #print(pt[:,p1])
        if(d>0):
            return True
        else:
            return False
        
        
    def mapRectangle(p1, p2, p3, p4):
        """return two 1D arrays: X list and Y list from
           points[:, p1], points[:,p2], points[:, p3], points[:, p4]"""
        A = np.dot(T, pt[:, [p1,p2,p3,p4,p1]])
        return A[0,:], A[1,:]

    def mapTriangle(p1, p2, p3):
        """return two 1D arrays: X list and Y list from
           points[:, p1], points[:,p2], points[:, p3]"""
        A = np.dot(T, pt[:, [p1,p2,p3,p1]])
        return A[0,:], A[1,:]

    for i in range(20):
        X, Y = mapTriangle(edges[i][0],edges[i][1],edges[i][2])
        print(X, Y)
        if(visible(edges[i][0],edges[i][1],edges[i][2])):
            plt.plot(X,Y,'r')    

    plt.axis('equal')
    drawAxis()

    plt.savefig(name)
    fig=plt.figure()


def plotcube(pt,name):
    """plot a cube described by pt. 
       T is the transition matrix that maps objects from a 3D space to a 2D screen.
       The viewport is at [1/2, 1/2, sqrt(2)/2]"""
    T = np.array([[m.sqrt(2)/m.sqrt(3), 0, -1/m.sqrt(3)],
                  [-1/m.sqrt(12),  m.sqrt(3)/2, -1/m.sqrt(6)]])
    
    def drawAxis():
        """ draw the axes of the 3D space"""
        X = np.dot(T, [[0,1.5],[0,0],[0,0]])
        Y = np.dot(T, [[0,0],[0,1.5],[0,0]])
        Z = np.dot(T, [[0,0],[0,0],[0,1.5]])
        plt.plot(X[0,:], X[1,:], 'b:')
        plt.plot(Y[0,:], Y[1,:], 'b:')
        plt.plot(Z[0,:], Z[1,:], 'b:')
        plt.text(X[0,1], X[1,1], r'x', fontsize=20)
        plt.text(Y[0,1], Y[1,1], r'y', fontsize=20)
        plt.text(Z[0,1]-0.1, Z[1,1], r'z', fontsize=20)

    def visible(p1, p2, p3):
            return True
        
    def mapRectangle(p1, p2, p3, p4):
        """return two 1D arrays: X list and Y list from
           points[:, p1], points[:,p2], points[:, p3], points[:, p4]"""
        A = np.dot(T, pt[:, [p1,p2,p3,p4,p1]])
        return A[0,:], A[1,:]

    def mapTriangle(p1, p2, p3):
        """return two 1D arrays: X list and Y list from
           points[:, p1], points[:,p2], points[:, p3]"""
        A = np.dot(T, pt[:, [p1,p2,p3,p1]])
        return A[0,:], A[1,:]

    for i in range(20):
        X, Y = mapTriangle(edges[i][0],edges[i][1],edges[i][2])
        print(X, Y)
        if(visible(edges[i][0],edges[i][1],edges[i][2])):
            plt.plot(X,Y,'r')

        
    plt.axis('equal')
    drawAxis()
  
    plt.savefig(name)
    fig=plt.figure()

# ----------- the main body ----------------------

points0 = np.copy(points)

#skew 
r1 = np.array([[1/m.sqrt(2),0,1/m.sqrt(2)],
               [0,1,0],
               [0,0,1]])
points1 = np.copy(points)
points1 = np.dot(r1, points1)

#rotate x 90 degrees
r2 = np.array([[1, 0, 0],
               [0, m.cos(1/2*(m.pi)), -m.sin(1/2*(m.pi))],
               [0, m.sin(1/2*(m.pi)), m.cos(1/2*(m.pi))]])
points2 = np.copy(points)
points2 = np.dot(r2, points2)

#scaling
r3 = np.array([[5, 0, 0],
               [0, 5, 0],
               [0, 0, 5]])
points3 = np.copy(points)
points3 = np.dot(r3, points3)

#trans(3,5)
r4 = np.array([[1, 0, 3],
               [0, 1, 0],
               [0, 0, 1]])
points4 = np.copy(points)
points4 = np.dot(r4, points4)

#skew+rotate y 45degrees
r5 = np.array([[-1/m.sqrt(2), 1, -1/m.sqrt(2)],
               [-2/m.sqrt(2), 0, 0],
               [-1/m.sqrt(2),-1, -1/m.sqrt(2)]])
points5 = np.copy(points)
points5 = np.dot(r5, points5)

#rotate z 30degrees+scale
r6 = np.array([[m.sqrt(3), -1, 0],
               [1, m.sqrt(3), 0],
               [0, 0, 2]])
points6 = np.copy(points)
points6 = np.dot(r6, points6)

#scale+trans
r7 = np.array([[ 3, 0, 9],
               [ 0, 3, 0],
               [ 0, 0, 3]])
points7 = np.copy(points)
points7 = np.dot(r7, points7)

#trans+skew
r8 = np.array([[1/m.sqrt(2),0,1/m.sqrt(2)],
               [0, 1,0],
               [ 0, 0, 2]])
points8 = np.copy(points)
points8 = np.dot(r8, points8)

plotcube(points0,'106070038_obj0.png')
plotcube1(points0,'106070038_obj0_hid.png')
plotcube(points1,'106070038_obj1.png')
plotcube1(points1,'106070038_obj1_hid.png')
plotcube(points2,'106070038_obj2.png')
plotcube1(points2,'106070038_obj2_hid.png')
plotcube(points3,'106070038_obj3.png')
plotcube1(points3,'106070038_obj3_hid.png')
plotcube(points4,'106070038_obj4.png')
plotcube1(points4,'106070038_obj4_hid.png')
plotcube(points5,'106070038_obj5.png')
plotcube1(points5,'106070038_obj5_hid.png')
plotcube(points6,'106070038_obj6.png')
plotcube1(points6,'106070038_obj6_hid.png')
plotcube(points7,'106070038_obj7.png')
plotcube1(points7,'106070038_obj7_hid.png')
plotcube(points8,'106070038_obj8.png')
plotcube1(points8,'106070038_obj8_hid.png')
