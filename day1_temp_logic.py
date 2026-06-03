temp = int(input("Enter the temperature of embedded micro-controller chip(in celsius)"))
if temp<=40:
  status = "System running optimal."
  action = "Cooling fan: OFF."
elif 40<temp<=75:
  status = "Warning: Elevated thermal profile."
  action = "Cooling fan: LOW SPEED."
elif temp>75:
  status = "CRITICAL OVERHEAT!"
  action = "Cooling fan: MAX SPEED"
else:
  status = "No temperature found"
  action = "Please enter temperature"

print("\n" + "="*35)
print(f"RECEVIER STATUS:{status}")
print(f"COMMAND ACTION:{action}")
print("="*35)
