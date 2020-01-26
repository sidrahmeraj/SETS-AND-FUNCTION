#!/usr/bin/env python
# coding: utf-8

# In[3]:


# SETS
def sets():
    print("SETS")
    
    a=int(input("ENTER NUMBER OF INPUTS YOU WANT TO ENTER:"))
    
    A=[]
    for i in range(a):
        b=input("ENTER VALUES YOU WANT TO ENTER:")
        A.append(b)
        
    B=[]
    b=int(input("ENTER NUMBER OF INPUTS YOU WANT TO ENTER:"))
    for j in range(b):
        c=input("ENTER VALUES YOU WANT TO ENTER:")
        B.append(c)
        
    C=[]

    #INTERSECTION    
    def INTERSECTION(X,Z):
        l=[]
        for i in range(len(X)):
            for k in range(len(Z)):
                if X[i]==Z[k]:
                    l.append(Z[k])
        return l

    #UNION:
    u=[]
    def UNION(X,Y):
        for i in range(len(X)):
            u.append(X[i])

        for j in range(len(Y)):

                u.append(Y[j])
        q=[]
        for i in range(len(u)):
            if u[i] not in q:
                q.append(u[i])
        return q

    #EMPTY SET LAW
    D=INTERSECTION(A,C)
    E=UNION(A,C)

    if D==C and E==A:
        print("EMPTY LAW PROVED!")
    else:
        print("EMPTY LAW NOT PROVED!")

    #IDEMPOTENCY LAW:  
    F=INTERSECTION(A,A)
    G=UNION(A,A)

    if F==G:

        print("IDEMPOTENCY LAW PROVED!")
    else:
        print("IDEMPOTENCY LAW NOT PROVED!")

    #ABSORPTION LAW:

    k=INTERSECTION(A,B)
    g=UNION(A,k)

    j=UNION(A,B)
    m=INTERSECTION(A,j)

    if g==m:
        print("ABSORPTION LAW PROVED!")

    else:
        print("ABSORPTION LAW NOT PROVED!")

    #COMMUTATIVE LAW:

    H=INTERSECTION(A,B)
    I=INTERSECTION(B,A)
    J=UNION(A,B)
    K=UNION(B,A)
    if H==I and J==K:
        print("COMMUTATIVE LAW PROVED!")
    else:
        print("COMMUTATIVE LAW NOT PROVED!")

    #ASSOCIATIVE LAW
    L=INTERSECTION(B,C)
    M=INTERSECTION(A,L)

    N=INTERSECTION(A,B)
    O=INTERSECTION(N,C)

    P=UNION(B,C)
    Q=UNION(A,P)

    R=UNION(A,B)
    S=UNION(R,C)

    if L==M and N==O and P==Q and R==S:
        print("ASSOCIATIVE LAW PROVED!")

    else: 
        print("ASSOCIATIVE LAW NOT PROVED!")


#FUNCTION:
def functionplot():
    print("")
    print("FUNCTION")
    print("")
    print("WE HAVE FOLLOWING DEFINED FUNCTION FOR GRAPH PLOTTING:\n(1)x^2\n(2)x^3\n(3)sin(x)\n(4)sin(x)cos(x)\n(5)exp(x)\n(6)sin(2*x)sin(3*x)\n(7)2sin(x)sin(x/2)\n(8)sin(x)/x")
    print("")
    a=int(input("Enter number between 1-8:"))
    if a==1:
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-5,5,100)
        y = x**2
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,y, 'r') 
        plt.show()

    if a==2:
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-5,5,100)
        y = x**3
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,y, 'g')
        plt.show()

    if a==3:
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-np.pi,np.pi,100)
        y = np.sin(x)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,y, 'b')
        plt.show()

    if a==4:
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-np.pi,np.pi,100)
        y = np.sin(x)
        z = np.cos(x)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,y, 'c', label='y=sin(x)')
        plt.plot(x,z, 'm', label='y=cos(x)')
        plt.legend(loc='upper left')
        plt.show()

    if a==5:
            import matplotlib.pyplot as plt
            import numpy as np
            x = np.linspace(-2,2,100)
            y = np.exp(x)
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('zero')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            plt.plot(x,y, 'y', label='y=e^x')
            plt.legend(loc='upper left')
            plt.show()

    if a==6:
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-np.pi,np.pi,100)
        p = np.sin(x) 
        q = np.sin(2*x) 
        r = np.sin(3*x) 
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,p, 'b-', label='y=sin(x)')
        plt.plot(x,q, 'c-', label='y=sin(2x)')
        plt.plot(x,r, 'm-', label='y=sin(3x)')
        plt.legend(loc='upper left')
        plt.show()

    if a==7:
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-np.pi,np.pi,100)
        p = 2*np.sin(x) 
        q = np.sin(x) 
        r = np.sin(x/2)  
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,p, 'b-', label='y=2sin(x)')
        plt.plot(x,q, 'c-', label='y=sin(x)')
        plt.plot(x,r, 'm-', label='y=sin(x/2)')
        plt.legend(loc='upper left')
        plt.show()

    if a==8:
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-20,20,500)
        y = np.sin(x)/x 
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x,y, 'b-', label='y=sin(x)/x')
        plt.plot(x,2*y, 'c-', label='y=2sin(x)/x')
        plt.plot(x,-y, 'm-', label='y=-sin(x)/x')
        plt.legend(loc='upper left')
        plt.show()
        
#functionplot()

def invfunctionplot():
    print("")
    print("INVERSE FUNCTION PLOT")
    print("")
    print("Press 1 for INVERSE SIN FUNCTION\nPress 2 for INVERSE COS FUNCTION:")
    b=int(input("Enter number:"))
    if b==1:
        import numpy as np 
        import matplotlib.pyplot as plt

        in_array = []
        n=int(input("Number of input: "))
        for i in range(n):
            a=int(input("Enter numbers: "))
            in_array.append(a)
        print ("Input array : ", in_array) 

        arcsin_Values = np.arcsin(in_array) 
        print ("\nInverse Sine values : \n", arcsin_Values) 

        in_array = np.linspace(-np.pi, np.pi, 12) 
        out_array1 = np.sin(in_array) 
        out_array2 = np.arcsin(in_array) 

        print("in_array : ", in_array) 
        print("\nout_array with sin : ", out_array1) 
        print("\nout_arraywith arcsin : ", out_array1) 


        plt.plot(in_array, out_array1, 
                        color = 'blue', marker = "*") 

        plt.plot(in_array, out_array2, 
                        color = 'red', marker = "o") 

        plt.title("blue : numpy.sin() \nred : numpy.arcsin()") 
        plt.xlabel("X") 
        plt.ylabel("Y") 
        plt.show() 

    if b==2:
            import numpy as np 
            import matplotlib.pyplot as plt

            in_array = []
            n=int(input("Number of input: "))
            for i in range(n):
                a=int(input(" Enter number: "))
                in_array.append(a)
            print ("Input array : ", in_array) 

            arccos_Values = np.arccos(in_array) 
            print ("\nInverse Cos values : \n", arccos_Values) 

            in_array = np.linspace(-np.pi, np.pi, 12) 
            out_array1 = np.cos(in_array) 
            out_array2 = np.arccos(in_array) 

            print("in_array : ", in_array) 
            print("\nout_array with cos : ", out_array1) 
            print("\nout_arraywith arccos : ", out_array1) 


            plt.plot(in_array, out_array1, 
                            color = 'blue', marker = "*") 

            plt.plot(in_array, out_array2, 
                            color = 'red', marker = "o") 

            plt.title("blue : numpy.cos() \nred : numpy.arccos()") 
            plt.xlabel("X") 
            plt.ylabel("Y") 
            plt.show()
            

def INV():
    print("")
    print("INVERSE OF GIVEN FUNCTION:")
    def fun(x):
        return (x-3) / 2

    def inverse(x):
        return 2*x + 3

    result = fun(2)
    print("fun(2) = {}".format(result))

    inv = inverse(result)

    print("inverse(result) = {}".format(inv))

sets()
functionplot()
invfunctionplot()
INV()


# In[ ]:




