# EV Range Calculator

battery_capacity = float(input("Enter battery capacity (kWh): "))
energy_consumption = float(input("Enter energy consumption (kWh/100 km): "))

range_km = (battery_capacity / energy_consumption) * 100

print("\n--- EV Range ---")
print("Battery Capacity:", battery_capacity, "kWh")
print("Energy Consumption:", energy_consumption, "kWh/100 km")
print("Estimated EV Range:", round(range_km, 2), "km")
