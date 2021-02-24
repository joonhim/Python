from decimal import Decimal
def gcd(a,b):
        if b==0:
                return a
        else:
                return gcd(b,a%b)
x = int(input('Enter the value of x = '))
y = int(input('Enter the value of y = '))
no = int(input('Enter the value of text = '))
z = x*y
u = (x-1)*(y-1)

for e in range(2,u):
        if gcd(e,u)== 1:
                break
for i in range(1,10):
        s = 1 + i*u
        if s % e == 0:
                d = int(s/e)
                break
ctt = Decimal(0)
ctt =pow(no,e)
ct = ctt % z

dtt = Decimal(0)
dtt = pow(ct,d)
dt = dtt % z
print('n = '+str(z)+' e = '+str(e)+' t = '+str(u)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))
