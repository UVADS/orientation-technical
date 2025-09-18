







import random
import matplotlib.pyplot as plt

# Simulate 10 spins
wheel = ["0", "00"] + [str(n) for n in range(1, 37)]
results = []
for _ in range(10):
    spin = random.choice(wheel)
    print(spin)
    results.append(spin)

# Create roulette wheel visualization
import numpy as np

# American roulette wheel order
wheel_order = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1, '00', 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]

# Create the wheel
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
angles = np.linspace(0, 2*np.pi, len(wheel_order), endpoint=False)

# Color scheme: red and black alternating, green for 0 and 00
colors = []
for num in wheel_order:
    if num == 0 or num == '00':
        colors.append('green')
    elif str(num) in ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']:
        colors.append('red')
    else:
        colors.append('black')

# Draw the wheel
for i, (angle, num, color) in enumerate(zip(angles, wheel_order, colors)):
    # Highlight if this number was spun
    alpha = 1.0 if str(num) in results else 0.3
    wedge_width = 2*np.pi/len(wheel_order)
    
    ax.bar(angle, 1, width=wedge_width, color=color, alpha=alpha, edgecolor='white', linewidth=2)
    
    # Add number labels
    text_color = 'white' if color == 'black' else 'white'
    ax.text(angle, 0.7, str(num), ha='center', va='center', color=text_color, fontweight='bold', fontsize=8)

ax.set_ylim(0, 1)
ax.set_theta_zero_location('N')
ax.set_title('Roulette Wheel - Highlighted Numbers Were Spun', pad=20, fontsize=14)
ax.set_rticks([])
plt.tight_layout()
plt.savefig('roulette_wheel.png', dpi=300, bbox_inches='tight')
plt.show()


