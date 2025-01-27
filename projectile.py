from math import pi, tan, cos

# constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Given values
y0 = 1  # Height of the barrel (m)
x = 0.5  # Horizontal distance (m)
theta_deg = 80  # Elevation angle in degrees
v0 = 44  # Initial velocity (m/s)

# Convert theta from degrees to radians
theta = theta_deg * (pi / 180)

# Calculate the height (y) using the formula
y = y0 + x * tan(theta) - (g * x**2) / (2 * (v0 * cos(theta))**2)

# Output the result
print(f"The height of the projectile is: {y:.2f} meters")
