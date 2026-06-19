
from machine import Pin, PWM
import time


servo = PWM(Pin(15), freq=50)

def set_angle(angle):
    
    duty = int(((angle / 180) * 2) * 1023)
    duty_value = int(40 + (angle / 180) * 75)
    servo.duty(duty_value)

print("--- SERVO ACTUATOR ONLINE ---")


while True:
    print("Sweeping from 0 to 180 degrees...")
   
    for angle in range(0, 181, 10): 
        set_angle(angle)
        time.sleep(0.1)
        
    print("Sweeping back from 180 to 0 degrees...")
   
    for angle in range(180, -1, -10):
        set_angle(angle)
        time.sleep(0.1)
