from machine import Pin, ADC
import time
led = Pin(2, Pin.OUT)         
ldr = ADC(Pin(34))           
ldr.atten(ADC.ATTN_11DB)      
print("--- SMART LIGHTING SYSTEM INITIALIZED ---")
while True:
    light_level = ldr.read() 
    
    print(f"Current Ambient Light Level: {light_level}")
    
    if light_level > 2000:
        led.value(1)           
        print("STATUS: Dark detected! -> Streetlight ON 🟡")
    else:
        led.value(0)          
        print("STATUS: Daylight detected. -> Streetlight OFF ❌")
        
    time.sleep(1)             
