# problem 1
def sum_values(x, y=0):
    return x+y

# problem 2
def tot_seconds(h,m,s):
    return 3600*h+60*m+s

# problem 3
def my_print(S,N=0):
    print(' '*N+S)

# problem 4
def get_chars(S,X):
    if X<len(S):
        return S[X], S[-X]
    else:
        return "error"
    
# problem 5
def is_less_than(x,y=1):
    return x<y**2

# problem 6
def minimum(x,y,z):
    if x<=y and x<=z:
        return x
    elif y<=x and y<=z:
        return y
    else:
        return z
    
# problem 7
def multiples(n):
    x = n
    while x<100:
        print(x)
        x = x+n
    
# problem 8
def get_product(n):
    p = 1
    for i in range(n):
        p = p*int(input('insert integer: '))
    return p

# problem 9
def get_sum(L,n=None):
    s = 0
    for el in L:
        if n==None or el<n:
            s += el
    return s
        
# problem 10
def find_min_max(L):
    min_i = 0
    max_i = 0
    m = M = L[0]
    for i in range(len(L)):
        if L[i]<m:
            min_i = i
            m = L[i]
        if L[i]>M:
            max_i = 0
            M = L[i]
    return min_i, max_i

# problem 11
def is_palindrome(s):
    for i in range(len(s)//2):
        if not s1[i]==s1[-1-i]:
            return False
    return True

# problem 12
def sum_all(L):
    s = 0
    for subL in L:
        for el in subL:
            s += el
    return s

# problem 13
def is_sorted(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            return False
    return True

# problem 14
def mod_list(L):
    L.remove(0)
    L.remove(-1)
    
# problem 15
def get_list_from_tuple(T,n):
    L = list(T)
    if n<len(L):
        L.remove(n)
    return L


