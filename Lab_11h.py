
def kinetic_energy(mass, velocity):
    kinetic_energy_value = 0.5 * mass * velocity**2
    return kinetic_energy_value

def main(num_calc):
    for x in range(num_calc):
        mass = float(input("Enter the object's mass: "))
        velocity = float(input("Enter the object's velocity: "))
        ke = kinetic_energy(mass, velocity)
        print(f'Mass: {mass}, Velocity: {velocity} Kinetic Energy: {ke}')
        
num_calc = int(input('Enter number of calculations: ')) 
 
main(num_calc)
        