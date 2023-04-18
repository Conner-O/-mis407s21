def generate_ax_plus_b(a, b):
    # Define and return the function `g(x)` that computes the specified result
        def g(x):
            return a * x + b
        return g

a = float(input("Enter a: "))
b = float(input("Enter b: "))
linear_function = generate_ax_plus_b(a, b)
x = float(input("Enter x: "))
print("Result of a*x + b:", linear_function(x))