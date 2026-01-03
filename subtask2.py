n = 0
s = 0

x = int(input("Enter a number: "))

while x != -1:
    if n == 0:
        m = x
    else:
        if x < m:
            m = x

    n = n + 1
    s = s + x

    x = int(input("Enter a number: "))

if n == 0:
    m = -1
    a = -1
else:
    a = s / n

print("n =", n)
print("s =", s)
print("m =", m)
print("a =", a)
#it looks like I learned how to use git today