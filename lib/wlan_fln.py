import network
import time

print('FLN.setup')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('FRITZ!Powerline 1240E', '71957628506954499377')
for x in range(5):
    print('.', end='')
    time.sleep(1)
else:
    print('\nwlan.ifconfig: ', end='')
print(wlan.ifconfig())
print('fln.done')
