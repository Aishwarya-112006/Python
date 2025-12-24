'''Decorators:tools for decoration/or form login section'''
#write a function that is a decorator to measure the execution time of a function
import time#used for calulation time
def timer(func):#decorator function
    def wrapper(*args,**kwargs):#wrapper function to wrap the original function,takes unlimited arguments
        start_time=time.time()#start time
        result=func(*args,**kwargs)#call the original function
        end_time=time.time()#end time
        execution_time=end_time-start_time#calculate execution time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")#print execution time
        return result#return the result of the original function
    return wrapper#return the wrapper function
@timer#apply the decorator to the example function
def example_function(n):#example function to demonstrate the decorator
    time.sleep(n)
example_function(2)#call the example function with argument 2 seconds
