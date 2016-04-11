
def deco(func):
    print 'before func called'
    func()
    print 'after func called'
    return func
@deco
def myfunc():
    print "myfunc says:hello world"

def  find_doc(func):
    if func.__doc__ == None :
        print 'has no doc'
    else:
        print 'doc is',func.__doc__
    return func
@find_doc
def func1():
    'func:test function'
    print 'func1 say hello world'
@find_doc
def func2():
    print 'func2 say hello world'
func1()
func2()
#myfunc()
#myfunc()