import getch
import curses
import sys

file = open('/sys/class/backlight/intel_backlight/brightness','r+')
brightness_value = int(file.read()[:-1])

low_limit = 100
high_limit = 7000

if (len(sys.argv) == 3) and (sys.argv[1] == '-l'):
	print("Brightness before: ",brightness_value)
	c_brightness_value = int(sys.argv[2])
	while (c_brightness_value > high_limit) or (c_brightness_value < 1):
		c_brightness_value = int(input('Choose correct value\n'))
	file.write(str(c_brightness_value))
	file.close()
	exit()

if (len(sys.argv) == 2) and (sys.argv[1] == '-L'):
	print(brightness_value)
	c_brightness_value = input('Write brightness you want (1-7000): ')
	while((int(c_brightness_value) > high_limit) or (int(c_brightness_value) < 1)):
		c_brightness_value = input('Choose correct value\n')
	file.write(c_brightness_value)
	file.close()
	exit()
if (len(sys.argv) == 2) and (sys.argv[1] == '-h'):
	print("""-l <value> - specific value of brightness (1-7000) which is setting up 
immediately.
-L - specific value of brightness (1-7000).
-h - Display this help menu.""")
	exit()


print(brightness_value)

key = ''
while key != 'q':
    key = getch.getch()
    if(key == 'w'):
    	if (brightness_value >= high_limit):
    		print("Value of brightness more than 7000, can't increase.\n If you want to maximize screen bright press 0\n")
    		continue
    	print('Increasing by 100 pts\n')
    	brightness_value = brightness_value + 100
    	file.write(str(brightness_value))
    	print(file.read())
    	print(brightness_value)
    elif (key == 's'):
    	if (brightness_value <= low_limit):
    		print("Value of brightness less than 100, can't decrease.\n If you want to minimize screen bright press 1\n")
    		continue
    	print('Decreasing by 100 pts\n')
    	brightness_value = brightness_value - 100
    	file.write(str(brightness_value))
    	print(file.read())
    	print(brightness_value)
    elif (key == '1'):
    	print('Minimum bright\n')
    	file.write('1')
    	print(file.read())
    	brightness_value = 1
    elif (key == '0'):
    	print('Maximum bright\n')
    	file.write('7000')
    	print(file.read())
    	brightness_value = 7000
    else:
    	if (key != 'q'):
    		print('Choose correct variant\n')
    	else:
    		exit()
file.close()
exit()
#xfce4-popup-applicationsmenu