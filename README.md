# Virtual Voltmeter
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

A RPI Pico and/or Arduino and Python based ecosystem that will make a virtual voltmeter appear on screen that updates real time and can be used by streamers  who wish to show voltages on the screen as well. 

Best Suited for hardware development streamers and content creators. 

The voltmeter cannot read reverse polarity and voltages >25 volts right now because of the resistor divider used. Feel free to hack at the device and code if ambitious. I have used the arduino based voltage detector modules that have a 30K and 7.5K resistor ladder.

# Hardware.
- Upload code to your favorite dev board with Serial communication capabilities. (code in /hardware)
(Tested with Arduino and RPI Pico)
- Connect the parts as described in the schematic in the /hardware folder. 
- Fit in enclosure that you can 3d print (files provided for 2 styles in /hardware )
- Enjoy. 
- Download the 3D Files either from the folder or from printables: https://www.printables.com/model/497685-voltmeter-with-a-pi-pico-that-casts-the-data-to-a-

# Software
- Download the setup.exe file from the v1.0.0 Release. (Check releases tab.)
- Finish the setup (Don't worry. Does not contain any viruses. Just python code that scans the serial port to give a o/p)
- In the startup page, type the com port the voltmeter is connected to as is (eg: COM3 (or) com3)
- Enjoy

# Setting up streaming with software
- (Tested with OBS only)
- Start the voltameter software. 
- Start OBS.
- Add a source
- Add a window capture
- Choose the virtual multimeter from the dropdown
- [scanning.exe]: vIRTUAL MULTIMETER ESCcrasci
- After setting it at the posistion of choice
- Right click on the multimeter scene in OBS and presws on filters
- Press on the + and add chroma key
- Choose custom key colour type
- Select colour and add HTML code #00FFFF
- Once done, save and you are good to go. 
- It will look somewhat like this

SEE VIDEO BELOW FOR COMPLETE SETUP


https://github.com/atulravi/virtualmultimeter/assets/70395057/c0b2f832-0102-4875-b9c9-df2db2375dfc

# Platform
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)

# Device pictures:
Please note that the inline socket version that can be directly plugged into a multimeter is still in development and will be released soon. Until then, either frankenstien it in the multimeter of your choice, or add a 7 segment display and use it as a seperate device.
- PostBox enclosure type
![20230530_190719](https://github.com/atulravi/virtualmultimeter/assets/70395057/886c8601-9f3b-4395-b558-80452144dd57)
![20230530_183022](https://github.com/atulravi/virtualmultimeter/assets/70395057/d5579a00-fdb0-4b23-a273-0104083aa9fa)
![20230530_184754](https://github.com/atulravi/virtualmultimeter/assets/70395057/8eaf6398-b166-4471-b4b6-18d12a969307)
![20230530_184802](https://github.com/atulravi/virtualmultimeter/assets/70395057/f4b91710-fa15-4bba-998d-dce4134e4bcd)

# Frankenstiend in to a DMM

![IMG_20230523_130229](https://github.com/atulravi/virtualmultimeter/assets/70395057/21cccf3f-9548-4838-b2d3-94e37126521e)
![IMG_20230523_130126](https://github.com/atulravi/virtualmultimeter/assets/70395057/298bda2b-9f75-4905-9c20-87a471f65506)
![IMG_20230523_130141](https://github.com/atulravi/virtualmultimeter/assets/70395057/77543f32-330d-46b6-87f9-51fa0e103909)

(BEWARE. IF YOU RUIN YOUR DMM, I TAKE NO RESPONSIBILITY. RISKS ARE INVOLVED WITH OSSH)
