# required values imported from math
# the math module is a standard module in python
from math import pi, tan, cos

# assign the values given to each of the variables of the equation

# constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Given values
y0 = 1  # Height of the barrel (m)
x = 0.5  # Horizontal distance (m)
theta_deg = 80  # Elevation angle in degrees
v0 = 44  # Initial velocity (m/s)

# Convert theta from degrees to radians
# Conversion formula: radians = degrees * (pi / 180)
theta = theta_deg * (pi / 180)

# Calculate the height (y) using the formula
y = y0 + x * tan(theta) - (g * x**2) / (2 * (v0 * cos(theta))**2)

# Output the result
# f-string format used to display result
# f-string allows you to embed Python expressions inside the curly braces
# :.2f is a format specifier that formats the value of y to 2 decimal places (for readability)
print(f"The height of the projectile is: {y:.2f} meters")
