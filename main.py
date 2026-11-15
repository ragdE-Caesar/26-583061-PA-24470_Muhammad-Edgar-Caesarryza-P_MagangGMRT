import numpy as np
import matplotlib.pyplot as plt

def forward_kinematics(theta1, theta2, l1, l2):
    
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    
    return x, y

print("Forward Kinematics for a 2-DoF Robotic Leg")
theta1_deg = float(input("Angle of the first joint (theta1) in degrees: "))
theta2_deg = float(input("Angle of the second joint (theta2) in degrees: "))
l1 = float(input("Length of the first link (l1): "))
l2 = float(input("Length of the second link (l2): "))

theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)

x, y = forward_kinematics(theta1, theta2, l1, l2)

print(f"The end effector is at position ({x:.2f}, {y:.2f})")