import LOG_REG

# U = AX+B
# Y = SIGMOID(U)

L = LOG_REG.Log_Reg(learning_rate=0.01,iterations=100) #NORMAL LOGISTIC REGRESSION
c = L.fit(X,Y) # RETURNS THE COST FUNCTION

L1 = LOG_REG.Log_Reg_appx(learning_rate=0.01,iterations=100) #LOGISTIC REGRESSION USING APPROXIMATION
c1,ga,gb,wa,wb = L1.fit(X,Y) #RETURNS COST , GRADIENTS , WEIGHTS ,
