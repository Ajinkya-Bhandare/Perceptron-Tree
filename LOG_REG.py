import numpy as np
import log as l

e = 2.7

class Log_Reg():
    def __init__( self, learning_rate, iterations ) :        
        self.learning_rate = learning_rate        
        self.iterations = iterations
        print(self.iterations,self.learning_rate)

    def sigmoid(self,x):
        return 1/(1+e**-x)

    def sigmoid_appx(self,X):
        w = []
        for i in X:
            if i<-2:
                w.append(0)
            elif i>2:
                w.append(1)
            else :
                w.append(x/4+1/2)
        return np.array(w)

    def pred(self,X,a,b):
        W = np.dot(X,a)+b
        return self.sigmoid(W)

    def loss(self,Y):
        if Y==0:
            print("hello1")
            return 1000
        elif Y==1:
            return 0
        else:
            return -np.log(Y)

    def cost(self,X,Y,a,b):
        Y_pred = self.pred(X,a,b)
        cost = 0
        l = len(Y)
        for i in range(l):
            y = Y[i]
            if y==0:
                cost+=self.loss(1-Y_pred[i])
            else:
                cost+=self.loss(Y_pred[i])
        return cost

    def grad(self,X,Y,a,b,lr=0.05):
        c = self.cost(X,Y,a,b)
        ca = []
        t = np.identity(self.num_features)*lr
        for i in range(self.num_features):
            ca.append(c-self.cost(X,Y,a+t[i],b))
        ca = np.array(ca)
        cb = c-self.cost(X,Y,a,b+lr)
        return (ca)/lr,cb/lr

    def update_weight(self,a,b,X,Y):
        (grad_a,grad_b) = self.grad(X,Y,a,b)
        self.a = self.a + grad_a * self.learning_rate
        self.b = self.b + grad_b * self.learning_rate

    def random_init(self):
        self.a = np.ones(self.num_features)
        self.b = 1
        
    def fit(self,X,Y):
        self.X = X
        self.Y = Y
        self.num = X.shape[0]
        self.num_features = X.shape[1]
        self.random_init()
        l = []
        for i in range(self.iterations) :
            l.append(self.cost(X,Y,self.a,self.b))
            self.update_weight(self.a,self.b,self.X,self.Y)            
        l.append(self.cost(self.X,self.Y,self.a,self.b))
        return l
    
class Log_Reg_appx():
    def __init__( self, learning_rate, iterations ) :        
        self.learning_rate = learning_rate        
        self.iterations = iterations
        print(self.iterations,self.learning_rate)


    def sigmoid_appx(self,x):
        w = []
        for i in x:
            if i<-2:
                w.append(0)
            elif i>2:
                w.append(1)
            else :
                w.append(i/4+1/2)
        return 1/(1+e**-x)#np.sigmoid(w)

    def pred(self,X,a,b):
        W = np.dot(X,a)+b
        return self.sigmoid_appx(W)

    def loss(self,Y):
        if Y==0:
            #print('hello')
            return 1000
        elif Y==1:
            return 0
        else:
            return -l.log(Y)

    def cost(self,X,Y,a,b):
        Y_pred = self.pred(X,a,b)
        cost = 0
        l = len(Y)
        for i in range(l):
            y = Y[i]
            if y==0:    #IF TRUE VALUE == 0 
                cost+=self.loss(1-Y_pred[i])
            else:       #IF TURE VALUE == 1
                cost+=self.loss(Y_pred[i])
        return cost
#!!!!!!!------NEED WORK --------!!!!!!!!!!!
    def grad(self,X,Y,a,b,lr=0.05):
        c = self.cost(X,Y,a,b)
        ca = []
        t = np.identity(self.num_features)*lr
        for i in range(self.num_features):
            ca.append(c-self.cost(X,Y,a+t[i],b))
        ca = np.array(ca)
        cb = c-self.cost(X,Y,a,b+lr)
        ca = ca
        cb = cb
        return (ca)/lr,cb/lr
#!!!!!!!------NEED WORK --------!!!!!!!!!!!

    def update_weight(self,a,b,X,Y):
        (grad_a,grad_b) = self.grad(X,Y,a,b)
        # print(a,b)
        self.a = self.a + grad_a * self.learning_rate
        self.b = self.b + grad_b * self.learning_rate
        return grad_a,grad_b
    def random_init(self):
        self.a = np.ones(self.num_features)
        self.b = 1
        
    def fit(self,X,Y):
        self.X = X
        self.Y = Y
        self.num = X.shape[0]
        self.num_features = X.shape[1]
        self.random_init()
        l = []
        ga,gb = [],[]
        wa,wb = [],[]
        for i in range(self.iterations) :
            l.append(self.cost(X,Y,self.a,self.b))
            (w1,w2) = self.update_weight(self.a,self.b,self.X,self.Y)
            ga.append(w1),gb.append(w2),wa.append(self.a),wb.append(self.b)
        l.append(self.cost(self.X,self.Y,self.a,self.b))
        return l,ga,gb,wa,wb