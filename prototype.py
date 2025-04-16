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

def typeof(function,var1,var2=None):
    if var2!=None:
        x,y = symbols(f"{var1} {var2}")
        f = sympify(function)
        f_x = diff(f,x)
        f_xx = diff(f_x,x)
        f_y = diff(f,y)
        f_yy = diff(f_y,y)
        f_xy = diff(f_x,y)
        D = sympify((f_xx*f_yy)-f_xy**2)
        solutions = critical(function, var1, var2)
        if solutions == "No critical points.":
            return "None"
        elif type(solutions) is dict:
            evaluated = []
            evaluated.append((solutions[x],solutions[y]))
            return evaluated
        else:
            results=[]
            for x_val, y_val in solutions:
                if D.evalf(subs = {x:x_val, y:y_val})>0:
                    if f_xx.evalf(subs = {x:x_val, y:y_val})>0:
                        results.append("minimum")
                    else:
                        results.append("maximum")
                elif D.evalf(subs = {x:x_val, y:y_val}) == 0:
                    for x_str,y_str in solutions:
                        funcatzero = f.evalf(subs = {x:float(x_str), y:float(y_str)})
                        deltapos = f.evalf(subs={x:float(x_str)+0.1, y:float(y_str)+0.1})
                        deltaneg = f.evalf(subs={x:float(x_str)-0.1, y:float(y_str)-0.1})
                        if (funcatzero<deltapos)&(funcatzero<deltaneg):
                            results.append("minimum")
                        elif (funcatzero>deltapos)&(funcatzero>deltaneg):
                            results.append("maximum")
                        else:
                            results.append("saddle point")
                else:
                    results.append("saddle point")
            return results
    else:
        x = symbols(var1)
        f = sympify(function)
        f_x = diff(f, x)
        f_xx = diff(f_x, x)

        list = []
        for x_val in critical(f, x):
            if f_xx.evalf(subs={x: x_val}) > 0:
                list.append("minimum")
            elif f_xx.evalf(subs={x: x_val}) < 0:
                list.append("maximum")
            elif f_xx.evalf(subs={x: x_val}) == 0:
                if ((f_x.evalf(subs={x: float(x_val) - 0.1})) > 0) & ((f.evalf(subs={x: float(x_val) + 0.1}) < 0)):
                    list.append("maximum")
                elif ((f_x.evalf(subs={x: float(x_val) - 0.1})) > 0) & ((f.evalf(subs={x: float(x_val) + 0.1}) > 0)):
                    list.append("Not a relative minimum or maximum")
                elif ((f_x.evalf(subs={x: float(x_val) - 0.1})) < 0) & ((f.evalf(subs={x: float(x_val) + 0.1}) < 0)):
                    list.append("Not a relative minimum or maximum")
                elif ((f_x.evalf(subs={x: float(x_val) - 0.1})) < 0) & ((f.evalf(subs={x: float(x_val) + 0.1}) > 0)):
                    list.append("minimum")
        return list

def derivative(function, var1, var2=None):
    if var2!=None:
        x, y = symbols(f"{var1} {var2}")
        f = sympify(function)
        return (str(derivative(f, x)) + ", with respect to x, and " + str(derivative(f, y)) + " with respect to y.")
    else:
        x = symbols(f'{var1}')
        f = sympify(function)
        return diff(f,x)

def critical(function, var1, var2=None):
    if var2!=None:
        x, y = symbols(f"{var1} {var2}")
        f = sympify(function)
        partial_x = diff(f, x)
        partial_y = diff(f, y)
        solutions = solve((partial_x, partial_y), (x, y))
        if not solutions:
            return "No critical points."
        elif type(solutions) is dict:
            evaluated = []
            evaluated.append((solutions[x],solutions[y]))
        else:
            evaluated = []
            for x_str, y_str in solutions:
                x_val = (x_str.evalf())
                y_val = (y_str.evalf())
                evaluated.append((x_val, y_val))
            filtered_values = [
                (x_eval, y_eval)
                for (x_eval, y_eval), (x_str, y_str) in zip(evaluated, solutions)
                if x_str.is_real and y_str.is_real
            ]
            return filtered_values
    else:
        x = symbols(f'{var1}')
        f = sympify(function)
        derivative = diff(f,x)
        return solve(derivative,x)

def main():
    choice = int(input("If you want to use a multivariable function, input 1: "))
    if choice == 1:
        function = input("Enter a function of two variables, x and y (example x**2+y**2): ")
        var1 = input("Enter the first variable of the function: ")
        var2 = input("Enter the second variable of the function: ")
        print(f"The derivative is {derivative(function, var1, var2)}")
        print(f"The critical point(s) are, {critical(function,var1,var2)}")
        print(f"The types of critical point(s) are, {typeof(function,var1,var2)}")
    else:
        function = input("Enter a function of a single variable (example x**2): ")
        var1 = input("Enter the first variable of the function: ")
        print(f"The derivative is {derivative(function, var1)}\n")
        print(f"The critical point(s) are, {critical(function,var1)}")
        print(f"The types of critical point(s) are, {typeof(function,var1)}")
    return

if __name__ == "__main__":
    main()

