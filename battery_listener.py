""" Module to monitoring the notebook battery and show a message box when the battery is critical
    The Critical Level can be configured editing file config.json
    """

import os
import subprocess
import time



zenity_box = '\
zenity --title "Bateria em nivel critico"  --warning \
--text="Bateria em {}% \n O computador será desligado quando atingir 7%." \
--width=350 --height=20 \
--ok-label="Adiar" '

def battery_level():
        #Verify the notebook battery using a linux package named ACPI

        battery_str = str(subprocess.check_output("acpi"))
        #print(battery_str)
        #Apply regular expressions to kwow the battery level
        #and the time remaing
        battery_str = battery_str.split(',')
        battery = int(battery_str[1].replace('%',''))
        #print(battery_level)
        time_remaining = battery_str[2][1:9]
        #print(time_remaining)
        return battery


def main():
    critical_level = 15
    read = battery_level()
    last_read = 100

    while True:
        print(read)

        #read = battery_level()

        #Verify if battery read is equal critical level
        if read == critical_level and not read == last_read:

            #Show the warning box
            os.system(zenity_box.format(battery_level()))
            last_read = read

        if read == 7 and not read == last_read:

            #Suspend the OS
            os.system("systemctl suspend")
            last_read = read

        time.sleep(60)
    

if __name__ == '__main__':

     main()
