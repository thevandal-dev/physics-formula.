# PHYSICS FORMULAS
# Created by: Celestine

# 1. Final Velocity
def final_velocity(u, a, t):
    return u + (a * t)


# 2. Force
def force(m, a):
    return m * a


# 3. Weight
def weight(m, g):
    return m * g


# 4. Power
def power(work, time):
    return work / time


# 5. Kinetic Energy
def kinetic_energy(m, v):
    return 0.5 * m * (v ** 2)


# Display sample results
if __name__ == "__main__":
    print("Final Velocity:", final_velocity(10, 2, 5), "m/s")
    print("Force:", force(5, 3), "N")
    print("Weight:", weight(10, 9.8), "N")
    print("Power:", power(100, 5), "W")
    print("Kinetic Energy:", kinetic_energy(4, 6), "J")
