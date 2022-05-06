a = float(input())
b = float(input())
c = float(input())
d = ((b*b) - (4*a*c))
print(d**(0.5))
if d<=0:
    print(f"d<0, корней нет D={d}")
else:
    x1 = (((-1*b)-(d**(0.5)))/(2*a))
    x2 = (((-1*b)+(d**(0.5)))/(2*a))
    print(f"x1={x1}; x2={x2}")
