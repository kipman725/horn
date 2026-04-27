#Symbolic computation calculator
import sympy
from sympy import *
z = symbols('z', positive=True)
k_e = symbols('k_e', positive=True)
t = symbols('t', positive=True)
A0 = symbols('A0', positive=True)
theta_i = symbols('theta_i', positive=True)
hyp_area = A0*(cosh(k_e*z/2)+t*sinh(k_e*z/2))**2
hyp_area = hyp_area.subs(t, 1)
hyp_r = simplify(sqrt(hyp_area/pi))
hyp_r_div = simplify(diff(hyp_r, z))
conic_r_div = tan(theta_i/2)
#checksol = 2*log((2*tan(theta_i/2)/k_e)*sqrt(pi/2))/k_e
solution = solve([hyp_r_div - conic_r_div], [z], dict=True)
simp = logcombine(simplify(factor(solution[0])))
print((latex(hyp_r)))
#num_sol = simp.subs([(t, 0.6), (A0, 4.8664e-04), (theta_i, 1.8884), (k_e, 13.189)])
#print(num_sol)