print("Performance: keep the room comfortable and save energy")
print("Environment: one room with a temperature sensor and a people counter")
print("Actuators: cooler, heater, eco mode")
print("Sensors: temperature reading, number of people in the room")

percepts = [
    [30, 2],
    [27, 1],
    [19, 3],
    [22, 0],
    [24, 1],
]

print("sample percepts (temperature, people):")
for p in percepts:
    print(p)
