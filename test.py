import wiringpi2 as wiringpi

wiringpi.wiringPiSetup()

print wiringpi.digitalRead(1)
print wiringpi.analogRead(1)
