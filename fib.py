#this python program produces the fib of any arbitrary nth term 


from functools import lru_cache
@lru_cache()

def fib(a):
    if(a<=2):
        return 1
    else: 
        return fib(a-1)+fib(a-2)


def program():
    a= int(input("Key in fib nth term"))
    print(fib(a))
    trial = str(input("Do you wanna check for another nth term?: Y/N"))
    if trial=="N":
        return('Do visit again!')
        
    else:
        return(program())
print(program())

#yay the program ends here