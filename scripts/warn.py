import os
import time


def flashBrightness():
    current_bright = os.popen("xbacklight").read().replace("\n", "")

    if(int(float(current_bright)) > 50):
        for i in range(2):
            os.system("xbacklight = 5 -time 250")
            os.system("xbacklight = 100 -time 250")
    else:
        for i in range(2):
            os.system("xbacklight = 100 -time 250")
            os.system("xbacklight = 5 -time 250")

    os.system("xbacklight = " + current_bright)


def getBat(data):
    return data.split(",")[1].replace("%", "")


def getStatus(data):
    return data.split(" ")[2].replace(",", "")


def getOutput():
    output = os.popen("acpi -b").read().split("\n")
    return output[:len(output) - 1]


def notify(percentage):
    os.system("notify-send --expire-time=300000 'Warning' '\nLow battery: " + str(percentage)+ "%'")
    flashBrightness()


def main():
    while(True):
        time.sleep(300)

        # read acpi output and get percentage
        output = getOutput()
        charging = False
        total = 0

        # parse output
        for line in output:
            bat = getBat(line)
            status = getStatus(line)
            total += int(bat)

            if status == "Charging":
                charging = True

        # calculate percentage
        percentage = int((total * 100) / (len(output) * 100))

        # if percentage is below 15: show notification
        if(percentage < 15 and not charging):
            notify(percentage)


if __name__ == "__main__":
    main()
