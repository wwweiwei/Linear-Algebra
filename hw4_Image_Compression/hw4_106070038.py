# Linear Algebra 2018 Assignment 4

import imageio as imio
import matplotlib.pyplot as plt
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def fix_k(name,output,k):
    img = rgb2gray(imio.imread(name)) #/Users/user/Desktop/a4/106070038_obj1.jpg
    height, width = np.shape(img)
    print(height, width)
    f1 = plt.subplot(221)
    f1.set_title("(a) Original picture ("+str(height)+"x"+str(width)+")")
    plt.imshow(img, cmap="gray")
    print("k=50")   #size
    
    U, S, V = np.linalg.svd(img, full_matrices=True)
    im1 = np.uint8(np.dot(U[:, :k] * S[:k], V[:k,:]))
    f2 = plt.subplot(222)
    f2.set_title("(b) Compressed with $k$="+str(k))
    plt.imshow(im1, cmap="gray")
    print("ρ:")
    print((height*k+k+k*width)/height/width) #fix k
    f3 = plt.subplot(223)
    f3.set_title("(c) Difference between (a) and (b)")
    plt.imshow(img-im1, cmap="gray")

    sum = 0
    for i in range(height):
        for j in range(width):
            if(img[i,j]):
                sum = sum+abs(img[i,j]-im1[i,j])/img[i,j]
    print("δ:")
    print(sum/width/height) #for loop

    f4 = plt.subplot(224)
    f4.set_title("(d) Singular values of $A$.")
    plt.plot(range(len(S)), S)
    plt.savefig(output)
    plt.show()
    
def fix_rho(name,output,rho):
    img = rgb2gray(imio.imread(name)) #/Users/user/Desktop/a4/106070038_obj1.jpg
    height, width = np.shape(img)
    print(height, width)
    f1 = plt.subplot(221)
    f1.set_title("(a) Original picture ("+str(height)+"x"+str(width)+")")
    plt.imshow(img, cmap="gray")
    k=(0.2*height*width)/(height+1+width)
    print("k:"+str(k))
    k=int(k)
    
    U, S, V = np.linalg.svd(img, full_matrices=True)
    im1 = np.uint8(np.dot(U[:, :k] * S[:k], V[:k,:]))
    f2 = plt.subplot(222)
    f2.set_title("(b) Compressed with $k$="+str(k))
    plt.imshow(im1, cmap="gray")
    print("ρ:")
    print(rho)
    f3 = plt.subplot(223)
    f3.set_title("(c) Difference between (a) and (b)")
    plt.imshow(img-im1, cmap="gray")

    sum = 0
    for i in range(height):
        for j in range(width):
            if(img[i,j]):
                sum = sum+abs(img[i,j]-im1[i,j])/img[i,j]
    print("δ:")
    print(sum/width/height) #for loop

    f4 = plt.subplot(224)
    f4.set_title("(d) Singular values of $A$.")
    plt.plot(range(len(S)), S)
    plt.savefig(output)
    plt.show()
    
def fix_delta(name,output,delta):
    img = rgb2gray(imio.imread(name)) #/Users/user/Desktop/a4/106070038_obj1.jpg
    height, width = np.shape(img)
    print(height, width)
    k=1 
    f1 = plt.subplot(221)
    f1.set_title("(a) Original picture ("+str(height)+"x"+str(width)+")")
    plt.imshow(img, cmap="gray")
    
    U, S, V = np.linalg.svd(img, full_matrices=True)
    im1 = np.uint8(np.dot(U[:, :k] * S[:k], V[:k,:]))
    a=1    
    while(a<delta-0.0025 or a>delta+0.0025):
        sum = 0
        im1 = np.uint8(np.dot(U[:, :k] * S[:k], V[:k,:]))
        for i in range(height):
            for j in range(width):
                if(img[i,j]):
                    sum = sum+abs(img[i,j]-im1[i,j])/img[i,j]
        #print("δ:")
        #print(sum/width/height)
        a=sum/width/height
        if(k>height or k>width):
            print("can't find")
            break
        k+=1
    k-=1
    
    f2 = plt.subplot(222)
    f2.set_title("(b) Compressed with $k$="+str(k))
    plt.imshow(im1, cmap="gray")   
    f3 = plt.subplot(223)
    f3.set_title("(c) Difference between (a) and (b)")
    plt.imshow(img-im1, cmap="gray")
    print("k:"+str(k))
    print("ρ:")
    print((height*k+k+k*width)/height/width)
    print("δ:")
    print(sum/width/height)
    f4 = plt.subplot(224)
    f4.set_title("(d) Singular values of $A$.")
    plt.plot(range(len(S)), S)
    plt.savefig(output)
    plt.show()


fix_k("106070038_obj1.jpg","106070038_obj1_compressed",50)
fix_k("106070038_obj2.jpg","106070038_obj2_compressed",50)
fix_k("106070038_obj3.jpg","106070038_obj3_compressed",50)
fix_k("106070038_obj4.jpg","106070038_obj4_compressed",50)
fix_k("106070038_obj5.jpg","106070038_obj5_compressed",50)

fix_rho("106070038_obj1.jpg","106070038_obj1_rho",0.8)
fix_rho("106070038_obj2.jpg","106070038_obj2_rho",0.8)
fix_rho("106070038_obj3.jpg","106070038_obj3_rho",0.8)
fix_rho("106070038_obj4.jpg","106070038_obj4_rho",0.8)
fix_rho("106070038_obj5.jpg","106070038_obj5_rho",0.8)

fix_delta("106070038_obj1.jpg","106070038_obj1_delta",0.03)
fix_delta("106070038_obj2.jpg","106070038_obj2_delta",0.03)
fix_delta("106070038_obj3.jpg","106070038_obj3_delta",0.03)
fix_delta("106070038_obj4.jpg","106070038_obj4_delta",0.03)
fix_delta("106070038_obj5.jpg","106070038_obj5_delta",0.03)





