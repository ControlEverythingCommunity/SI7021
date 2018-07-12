# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# SI7021
# This code is designed to work with the SI7021_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Humidity?sku=SI7021_I2CS#tabs-0-product_tabset-2



import smbus
import time


bus = smbus.SMBus(1)

# SI7021 address, 0x40(64)
# Read data, 2 bytes, Humidity MSB first
rh = bus.read_i2c_block_data(0x40, 0xE5, 2) 
#what really happens here is that master sends a 0xE5 command (measure RH, hold master mode) and read 2 bytes back
#if you read 3 bytes the last one is the CRC!
time.sleep(0.1)
# Convert the data
humidity = ((rh[0] * 256 + rh[1]) * 125 / 65536.0) - 6


# SI7021 address, 0x40(64)
# Read data , 2 bytes, Temperature MSB first
temp = bus.read_i2c_block_data(0x40, 0xE3,2)
#what really happens here is that master sends a 0xE3 command (measure temperature, hold master mode) and read 2 bytes back 
#if you read 3 bytes the last one is the CRC!
time.sleep(0.1)

# Convert the data
cTemp = ((temp[0] * 256 + temp[1]) * 175.72 / 65536.0) - 46.85
fTemp = cTemp * 1.8 + 32

# Output data to screen

print ("Humidity %%RH: %.2f%%" %humidity)
print ("Temperature Celsius: %.2f°C" %cTemp)
print ("Temperature Fahrenheit: %.2f°F" %fTemp)
