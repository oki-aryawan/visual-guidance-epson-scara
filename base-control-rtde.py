from asyncio import wait

from epsonrc.commands import connect, go, go_here, begin
import time

# 1. Connect to controller
if not connect('192.168.1.22', 5000):
    print("Failed to connect. Exiting.")
    exit()

# 2. Initialize system
begin(
    speed=20,
    speedfactor=70,
    power='Low'
)

i = 0

for i in range(10):
    go(200, 500, -30, -400)
    time.sleep(1)
    go(200, 600, -50, -500)
    time.sleep(1)
    go(-20, 600, -70, -400)
    time.sleep(1)
    go(-20, 500, -100, -500)
    time.sleep(1)
    i = i + 1
