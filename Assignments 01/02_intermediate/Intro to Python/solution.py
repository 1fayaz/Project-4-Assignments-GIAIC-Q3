# 🌌 Milestone 1: Weight on Mars

def mars_conversion():
    try:
        weight = float(input("Enter your weight on Earth: "))
        mars_equivalent = round(weight * 0.378, 2)
        print(f"Your weight on Mars would be: {mars_equivalent} kg")
    except ValueError:
        print("Please enter a valid number!")




# 🪐 Milestone 2: Weight on Any Planet


def weight_on_planet():
    gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    try:
        earth_weight = float(input("Enter your Earth weight (kg): "))
        planet = input("Choose a planet: ").capitalize()

        if planet in gravity:
            adjusted_weight = round(earth_weight * gravity[planet], 2)
            print(f"On {planet}, you'd weigh approximately {adjusted_weight} kg.")
        else:
            print("⚠️ That planet isn't in the list. Please check your spelling!")
    except ValueError:
        print("❗ Invalid input! Please enter a number for weight.")

mars_conversion()
weight_on_planet()
