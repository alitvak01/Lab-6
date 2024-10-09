#Authors are Aliza Litvak & Olivia Beck
def total(n):
    total = 0
    for step in range (1,n):
        if n % step == 0:
            total = total + step
    return total

def perfect():
    n = int(input("gimme a number \n"))
    perfect = total(n)
    if perfect == n:
        return True
    else:
        return False

print (perfect())
