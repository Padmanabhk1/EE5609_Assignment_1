from sympy import symbols, Eq, solve

a, b = symbols('a b')

eq1 = Eq(2*a + b - 4,0)
eq2 = Eq(a - 2*b + 3,0)

y=solve((eq1,eq2), (a, b))

print(y)

#print('a = {sol_dict[a]}')
#print('b = {sol_dict[b]}')

c, d = symbols('c d')

eq3 = Eq(5*c - d - 11,0)
eq4 = Eq(4*c + 3*d - 24,0)

z=solve((eq3,eq4), (c, d))

print(z)

