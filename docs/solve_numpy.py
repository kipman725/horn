#Symbolic computation calculator
import sympy
from sympy import *
init_printing(use_unicode=True)
z = symbols('z', positive=True)
k_e = symbols('k_e', positive=True) 
t = symbols('t', positive=True)
A0 = symbols('A0', positive=True)
theta_i = symbols('theta_i', positive=True)
hyp_area = A0*(cosh(k_e*z/2)+t*sinh(k_e*z/2))**2
#hyp_area = hyp_area.subs(t, 1)
hyp_r = sqrt(hyp_area/pi)
hyp_r_div = simplify(diff(hyp_r, z))
conic_r_div = tan(theta_i/2)
solution = solve([hyp_r_div - conic_r_div], [z], dict=true)
simp = logcombine(simplify(factor(solution[1])))
print(latex(simp))
#num_sol = simp.subs([(t, 0.6), (A0, 4.8664e-04), (theta_i, 1.8884), (k_e, 13.189)])
#print(num_sol)