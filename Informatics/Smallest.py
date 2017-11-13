## This program talks about the None being used instead of infinity.
## Usage
## x = [30,28,45,67,23,54]
## smallest(x)

def smallest(x):
    smallest  = None
    ## this sets the value of smallest to the first element of x
    for i in x:
    ## 'is' is stronger than '==' more used in terms of true and false statement
        if smallest is None :
            smallest = i
        elif i <smallest:
            smallest = i
    print (smallest)
############################################################
