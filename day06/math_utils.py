def square(n):
    return n*n
def cube(n):
    return n**3
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
if __name__=="__main__":
    print("Testing math_utils.py ")
    print(square(5))