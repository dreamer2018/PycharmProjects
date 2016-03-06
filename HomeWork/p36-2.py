__author__ = 'zhoupan'
def BinarySearch_1(a,x):
    left=0
    right=len(a)-1
    while(left<=right):
        middle=(left+right)/2
        print middle
        if(x==a[middle]):
            return middle
        if(x>a[middle]):
            left=middle
        else:
            right=middle
    return -1
def BinarySearch_2(a,x):
    left=0
    right=len(a)-1
    while(left<right-1):
        middle=(left+right)/2
        print middle
        if(x<a[middle]):
            right=middle
        else:
            left=middle
    if(x==a[left]):
        return left
    else:
        return right
def BinarySearch_3(a,x):
    left=0
    right=len(a)-1
    while(left+1!=right):
        middle=(left+right)/2
        print middle
        if(x>=a[middle]):
            left=middle
        else:
            right=middle
    if(x==a[left]):
        return left
    else:
        return -1
def BinarySearch_4(a,x):
    if( len(a)>0 and x>=a[0]):
        left=0
        right=len(a)-1
        while(left<right):
            middle=(left+right)/2
            print middle
            if(x<a[middle]):
                right=middle-1
            else:
                left=middle
        if(x==a[left]):
            return left
    return -1
def BinarySearch_5(a,x):
    if( len(a)>0 and x>=a[0]):
        left=0
        right=len(a)-1
        while(left<right):
            middle=(left+right+1)/2
            print middle
            if(x<a[middle]):
                right=middle-1
            else:
                left=middle
        if(x==a[left]):
            return left
    return -1
def BinarySearch_6(a,x):
    if( len(a)>0 and x>=a[0]):
        left=0
        right=len(a)-1
        while(left<right):
            middle=(left+right+1)/2
            print middle
            if(x<a[middle]):
                right=middle-1
            else:
                left=middle+1
        if(x==a[left]):
            return left
    return -1
def BinarySearch_7(a,x):
    if( len(a)>0 and x>=a[0]):
        left=0
        right=len(a)-1
        while(left<right):
            print left,right
            middle=(left+right+1)/2
            print middle
            if(x<a[middle]):
                right=middle
            else:
                left=middle
        if(x==a[left]):
            return left
    return -1
a=[1,3,6,9,12,15,19,20]
b=BinarySearch_7(a,3)
print 'b=',b
