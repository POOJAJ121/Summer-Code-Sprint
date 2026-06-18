from machine import Pin, time_pulse_us 
import time

trigger = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)
led = Pin(2, Pin.OUT)

def get_distance():
  
    trigger.value(0)
    time.sleep_us(2)
    
    
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    
   
    duration = time_pulse_us(echo, 1, 1000000) 
    
   
    distance_cm = (duration * 0.0343) / 2
    return distance_cm

print("--- RADAR SYSTEM ONLINE ---")


while True:
    dist = get_distance()
    
    if dist > 0:
        print(f"Target Distance: {dist:.1f} cm")
        
       
        if dist < 20.0:
            led.value(1)  
            print("⚠️ CRITICAL PROXIMITY ALERT! Braking system engaged! ⚠️")
        else:
            led.value(0)  
            print("Status: Path Clear ✅")
            
    time.sleep(0.5)
