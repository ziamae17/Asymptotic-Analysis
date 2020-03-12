#Kezzia Mae Y. Abella
#Asymptotic Analysis

import matplotlib.pyplot as plt
import math
import time

n = int(input("Please enter value of number: "))
userInput = []

def logarithmic(n):
    return math.log(n)

def linearithmic(n):
    return n*math.log(n)
    
def linear(n):
    return n

def quadratic(n):
    return n*n

def polynomial(n):
    return n**3
    
def exponential(n):
    return 2**n


logarithmicRunTime = []
linearithmicRunTime = []
linearRunTime = []
quadraticRunTime = []
polynomialRunTime = []
exponentialRunTime = []


while n < 100000:
    n += 10
    userInput.append(n)

    startTime = time.time()
    (logarithmic(n))
    logarithmicRunTime.append(time.time()-startTime)

    startTime1 = time.time()
    (linearithmic(n))
    linearithmicRunTime.append(time.time()-startTime1)

    startTime2 = time.time()
    (linear(n))
    linearRunTime.append(time.time()-startTime2)

    startTime3 = time.time()
    (quadratic(n))
    quadraticRunTime.append(time.time()-startTime3)

    startTime4 = time.time()
    (polynomial(n))
    polynomialRunTime.append(time.time()-startTime4)

    startTime5 = time.time()
    (exponential(n))
    exponentialRunTime.append(time.time()-startTime5)


plt.plot(logarithmicRunTime, userInput, label = "Logarithmic")
plt.plot(linearithmicRunTime, userInput, label = "Linearithmic")
plt.plot(linearRunTime, userInput, label = "Linear")
plt.plot(quadraticRunTime, userInput, label = "Quadratic")
plt.plot(polynomialRunTime, userInput, label = "Polynomial")
plt.plot(exponentialRunTime, userInput, label = "Exponential")
plt.xlabel("Runtime")
plt.ylabel("Value of Functions")
plt.title("Asymptotic Analysis")
plt.legend(["Logarithmic","Linearithmic","Linear","Quadratic","Polynomial","Exponential"])
plt.show()


