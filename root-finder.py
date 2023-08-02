# FIND THE SQUARE ROOT OF A NUMBER ( NEWTON'S METHOD )
def newtonsqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!= approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx

inp1=newtonsqrt(int(input("write your number\n")))
print(inp1)
