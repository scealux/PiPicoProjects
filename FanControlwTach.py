from machine import Pin, ADC, PWM
import utime, _thread, math

pot = ADC(Pin(28))
tach = Pin(26, Pin.IN)
out = PWM(Pin(22))

count = 0
RPM = 0

ping1 = utime.ticks_ms()
print("Start time: " + str(ping1))

out.freq(25000) #25kHz
def counter(self):
    global count
    count += 1
    
tach.irq(handler = counter, trigger = Pin.IRQ_FALLING)

while True:
    #Check time difference, update RPM
    CurrentTime = utime.ticks_ms()
    timeDiff =  utime.ticks_diff(CurrentTime, ping1)
    if timeDiff > 1000:
        #print("timeDiff = "+ str(timeDiff))
        RPM = (1000/timeDiff * count) * 30
        count = 0
        ping1 = utime.ticks_ms()
    PotVal = pot.read_u16()
    PotPercent = round((PotVal / 65535)*100)
    #print(str(PotPercent) + " " + str(RPM) + "rpm")
    print(str(PotPercent) + ", " +str(RPM))
    out.duty_u16(PotVal)
    utime.sleep(0.5)
