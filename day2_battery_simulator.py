battery_level=0
while battery_level < 100:
  battery_level = battery_level+20
  print(f"Charging...{battery_level}")
else:
  print("Battery Fully Charged! Disconnecting power source.")
