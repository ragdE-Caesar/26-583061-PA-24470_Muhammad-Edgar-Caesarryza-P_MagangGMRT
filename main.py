import numpy as np
import matplotlib.pyplot as plt

def forward_kinematics(theta1, theta2, l1, l2):
    """
    Calculate the forward kinematics for a 2-DoF robotic leg.

    Parameters:
    theta1 (float): Angle of the first joint in radians.
    theta2 (float): Angle of the second joint in radians.
    l1 (float): Length of the first link.
    l2 (float): Length of the second link.

    Returns:
    tuple: (x, y) coordinates of the end effector.
    """
    # Calculate the position of the end effector
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    
    return x, y

print("Forward Kinematics for a 2-DoF Robotic Leg")
print("Enter the angles (in degrees) and lengths of the links:")
# Get user input for angles and lengths
theta1_deg = float(input("Angle of the first joint (theta1) in degrees: "))
theta2_deg = float(input("Angle of the second joint (theta2) in degrees: "))
l1 = float(input("Length of the first link (l1): "))
l2 = float(input("Length of the second link (l2): "))

# Convert angles from degrees to radians
theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)

# Calculate the forward kinematics
x, y = forward_kinematics(theta1, theta2, l1, l2)

print(f"The end effector is at position ({x:.2f}, {y:.2f})")