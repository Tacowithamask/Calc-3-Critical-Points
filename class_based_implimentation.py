#********************************************************************************************************#
# A function that takes an input of a mathematical function consisting
# of a single, or possibly two variables, and then prints the functions derivative
# and the x and or y values in which the derivative is equivalent to zero.
#********************************************************************************************************#


import math
import mpmath
import sympy
from sympy import roots, symbols, Eq, solve, diff, sympify
e = math.e

class Function:

    def __init__(self, function: str, var1 : str, var2 : str = '') -> None:
        self.f = sympify(function)
        self.var1 = symbols(var1)
        if var2 == '':
            self.var2 = ''
        else:
            self.var2 = symbols(var2)
        self.f_var1 = diff(self.f, self.var1)
        self.f_var2 = diff(self.f, self.var2)
        self.f_var1_var1 = diff(self.f_var1, self.var1)
        self.f_var2_var2 = diff(self.f_var2, self.var2)
        self.f_var1_var2 = diff(self.f_var1, self.var2)

    def __str__(self) -> str:
        return f"{self.f}"
    
    def typeof(self) -> list:
        D = sympify((self.f_var1_var1 * self.f_var2_var2) - self.f_var1_var2 ** 2 )
        solutions = self.multi_critical()
        if solutions == "No critical points.":
            return "None"
        else:
            results=[]
            for x_val, y_val in solutions:
                if D.evalf(subs = {self.var1:x_val, self.var2:y_val})>0:
                    if self.f_var1_var1.evalf(subs = {self.var2:x_val})>0:
                        results.append("minimum")
                    else:
                        results.append("maximum")
                elif D.evalf(subs = {self.var1:x_val, self.var2:y_val}) == 0:
                    results.append("No information.")
                else:
                    results.append("saddle point")
            return results  
      
    def multi_critical(self) -> list:
        solutions =  solve((self.f_var1, self.f_var2),(self.var1,self.var2))

        if not solutions:
            return "No Critical Points"
        if isinstance(solutions, dict):
            x_val = solutions['x']
            y_val = solutions['y']
            evaluated = [(x_val, y_val)]
            return evaluated
        else:
            evaluated = []
            for x_str, y_str in solutions:
                try:
                    x_val = round((x_str.evalf()),4)
                except TypeError:
                    x_val = x_str
                try:
                    y_val = round((y_str.evalf()),4)
                except TypeError:
                    y_val = y_str
                evaluated.append((x_val,y_val))
            filtered_values = [
                (x_eval, y_eval)
                for (x_eval, y_eval), (x_str, y_str) in zip(evaluated,solutions)
                if x_str.is_real and y_str.is_real
            ]
            return filtered_values 
    
    def derivative(self) -> str:
        return f"Derivative with respect to {self.var1} is {diff(self.f, self.var1)}, derivative with respect to {self.var2} is {diff(self.f, self.var2)}"
        
    def print(self) -> None:
        print(f"Critical Poitns are: {self.multi_critical()}")
        print(f"Type of Critical Points are: {self.typeof()}")
        print(self.derivative())


myFunction = Function("x**2*y**2 + x**3 + y**3*x + x", 'x', 'y')

myFunction.print()
