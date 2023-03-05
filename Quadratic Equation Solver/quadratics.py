import matplotlib.pyplot as plt
import numpy as np
import math
import sympy
import re


# Standard Form
class QuadraticExpression():

    def __init__(self):
        # Pattern should be in the form: 
        # 1) ax**2+bx+c 
        # 2) ax^2+bx+c
        # If a, b, or c is 1, it should be stated! 
        # Valid: 1x**2-1x
        # Invalid: x**2-x
        function = input("Quadratic Expression: ")        
        # Integer Pattern: pattern = r"^(-?\d*)x ?(?:\^|\*\*) ?2(?: ?([+-]?\d*)x)?(?: ?([+-]?\d*))?$"
        # Integer & Float Pattern: pattern = r"^(-?\d*(?:\.\d*)?)x ?(?:\^|\*\*) ?2(?: ?([+-]?\d*(?:\.\d*)?)x)?(?: ?([+-]?\d*(?:\.\d*)?))?$"
        pattern = r"^(-?\d*(?:\.\d*)?)x ?(?:\^|\*\*) ?2(?: ?([+-]?\d*(?:\.\d*)?)x)?(?: ?([+-]?\d*(?:\.\d*)?))?$"
        if re.match(pattern, function, re.IGNORECASE):
            matches = re.match(pattern, function, re.IGNORECASE)
            coefficients = list(matches.groups())
            for i in range(len(coefficients)):
                if coefficients[i] is None:
                    coefficients[i] = 0.0
                else:
                    try:
                        coefficients[i] = float(coefficients[i])
                    except:
                        coefficients[i] = 0.0
            self._coefficients = coefficients
            self._a = self._coefficients[0]
            self._b = self._coefficients[1]
            self._c = self._coefficients[2]

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Coefficient 'a' must be a number.")
        if value == 0:
            raise ValueError("Coefficient 'a' cannot be zero.")
        self._a = float(value)
    
    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Coefficient 'b' must be a number.")
        self._b = float(value)
    
    @property
    def c(self):
        return self._c
    
    @c.setter
    def c(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Coefficient 'c' must be a number.")
        self._c = float(value)
    
    @property
    def coefficients(self):
        return tuple(self._coefficients)

    # String Representation of the Quadratic Expression
    def __str__(self):
        a = sympy.symbols("a")
        b = sympy.symbols("b")
        c = sympy.symbols("c")
        x = sympy.symbols("x")
        expr = a * x**2 + b * x + c
        expr = expr.subs([(a, self._a), (b, self._b), (c, self._c)])
        return sympy.pretty(expr)
    
    # Discriminant Formula = b^2 - 4ac
    def discriminant(self):
        return float(self._b ** 2 - 4 * self._a * self._c)
    
    # Quadratic Formula: x1, x2 =  ((-b ± sqrt(b^2 - 4ac)) / 2a)
    def x_intercepts(self):
        if self.discriminant() < 0:
            return "The Equation Has No Real Solutions"
        else:
            x_one = ((-self._b + math.sqrt(self.discriminant())) / (2 * self._a))
            x_two = ((-self._b - math.sqrt(self.discriminant())) / (2 * self._a))
            return x_one, x_two

    def y_intercept(self):
        return float(self._c)
    
    #Axis of Symmetry Formula = -b/2a
    def axis_of_symmetry(self):
        return (-self._b / (2 * self._a))

    # Vertex Formula = (-b/2a, f(-b/2a))
    def vertex(self):
        x_vertex = self.axis_of_symmetry()
        y_vertex = (self._a * (x_vertex ** 2)) + (self._b * (x_vertex)) + (self._c)
        return x_vertex, y_vertex
    
    # Sum of the Roots = -b/a
    def sum_roots(self):
        return -self._b/self._a
    
    # Product of the Roots = c/a
    def product_roots(self):
        return self._c/self._a
    
    def plot(self):
        x = np.linspace(-10, 10, 1000)
        y = (self._a * (x**2)) + (self._b * x) + (self._c)
    
        # Create a new figure and axis object
        fig, ax = plt.subplots()
    
        # Plot the quadratic expression
        ax.plot(x, y)
    
        # Add x and y-axis lines
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
    
        # Add x-intercepts to the plot
        intercepts = self.x_intercepts()
        if intercepts != "The Equation Has No Real Solutions":
            ax.plot(intercepts, [0, 0], 'ro')
        
        # Add vertex to the plot
        vertex = self.vertex()
        ax.plot(vertex[0], vertex[1], 'bo')
    
        # Set the x and y-axis labels
        ax.set_xlabel('x')
        ax.set_ylabel('y')
    
        # Show the plot
        plt.show()

if __name__ == "__main__":
    quadratic = QuadraticExpression()
    print(quadratic)
    print("Discriminant:", quadratic.discriminant())
    print("X-Intercepts:", quadratic.x_intercepts())
    print("Y-Intercept:", quadratic.y_intercept())
    print("Axis of Symmetry:", quadratic.axis_of_symmetry())
    print("Vertex:", quadratic.vertex())
    print("Sum of the Roots:", quadratic.sum_roots())
    print("Product of the Roots:", quadratic.product_roots())
    quadratic.plot()
    print(quadratic.a)
