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

def typeof(function,var1,var2):
    x,y = symbols(f"{var1} {var2}")
    f = sympify(function)
    f_x = diff(f,x)
    f_xx = diff(f_x,x)
    f_y = diff(f,y)
    f_yy = diff(f_y,y)
    f_xy = diff(f_x,y)
    D = sympify((f_xx*f_yy)-f_xy**2)
    solutions = multi_critical(function, var1, var2)
    if solutions == "No critical points.":
        return "None"
    else:
        results=[]
        for x_val, y_val in solutions:
            if D.evalf(subs = {x:x_val, y:y_val})>0:
                if f_xx.evalf(subs = {x:x_val})>0:
                    results.append("minimum")
                else:
                    results.append("maximum")
            elif D.evalf(subs = {x:x_val, y:y_val}) == 0:
                results.append("No information.")
            else:
                results.append("saddle point")
        return results

def derivative(function, var1):
    x = symbols(f'{var1}')
    f = sympify(function)
    return diff(f,x)

def multiderivative(function, var1, var2):
    x,y=symbols(f"{var1} {var2}")
    f = sympify(function)
    return (str(derivative(f,x))+", with respect to x, and " + str(derivative(f,y)) + " with respect to y.")

def critical(function, var1):
    x = symbols(f'{var1}')
    f = sympify(function)
    derivative = diff(f,x)
    return solve(derivative,x)

def multi_critical(function,var1,var2):
    x,y = symbols(f"{var1} {var2}")
    f = sympify(function)
    partial_x = diff(f,x)
    partial_y = diff(f,y)
    solutions =  solve((partial_x,partial_y),(x,y))
    if not solutions:
        return "No critical points."
    else:
        evaluated = []
        for x_str, y_str in solutions:
            x_val = round((x_str.evalf()),4)
            y_val = round((y_str.evalf()),4)
            evaluated.append((x_val,y_val))
        filtered_values = [
            (x_eval, y_eval)
            for (x_eval, y_eval), (x_str, y_str) in zip(evaluated,solutions)
            if x_str.is_real and y_str.is_real
        ]
        return filtered_values

def main():
    choice = int(input("If you want to use a multivariable function, input 1: "))
    if choice == 1:
        function = input("Enter a function of two variables, x and y (example x**2+y**2): ")
        var1 = input("Enter the first variable of the function: ")
        var2 = input("Enter the second variable of the function: ")
        print(f"The derivative is {multiderivative(function, var1, var2)}\n")
        print(f"The critical points are, {multi_critical(function,var1,var2)}")
        print(f"The types of critical points are, {typeof(function,var1,var2)}")
    else:
        function = input("Enter a function of a single variable (example x**2): ")
        var1 = input("Enter the first variable of the function: ")
        print(f"The derivative is {derivative(function, var1)}\n")
        print(f"The critical points are, {critical(function,var1)}")
    return

if __name__ == "__main__":
    main()

