# On the try and except block You run some code and statements and if it is succesful the try block will get executed other the except block will be executed when there is an anticipatated error

try:
    number=100
    answer=number/0
    print("The answer is ",answer)
except Exception as e:
    print("There is an error",e)