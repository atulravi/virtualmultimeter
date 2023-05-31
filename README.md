# Virtual Voltmeter
A RPI Pico and Python based ecosystem that will make a virtual voltmemetr appear on screen that updates real time and can be used by streamers  who wish to show voltages on the screen as well. 

Best Suited for hardware development streamers and content creators. 

The voltmeter cannot read reverse polarity and voltages >25 volts right now because of the resistor divider used. Feel free to hack at the device and code if ambitious. 

# Hardware.
- Upload code to your favorite dev board with Serial communication capabilities. (code in /hardware)
(Tested with Arduino and RPI Pico)
- Connect the parts as described in the schematic in the /hardware folder. 
- Fit in enclosure that you can 3d print (files provided for 2 styles in /hardware )
- Enjoy. 

# Software
- Download the setup.exe file from the /software/Executables folder
- Finish the setup (Don't worry. Does not contain any viruses. Just python code that scans the serial port to give a o/p)
- In the startup page, type the com port the voltmeter is connected to as is (eg: COM3 (or) com3)
- Enjoy

# Setting up streaming with software
- (Tested with OBS only)
- Start the voltameter software. 
- Start OBS.
- Add a source
- ![image](https://github.com/atulravi/virtualmultimeter/assets/70395057/d4e86d91-9037-4589-b592-66fa32264871)
- Add a window capture
- ![image](https://github.com/atulravi/virtualmultimeter/assets/70395057/901080ee-706f-477e-bdc1-7508a7ef30d5)
- Choose the virtual multimeter from the dropdown
- [scanning.exe]: vIRTUAL MULTIMETER ESCcrasci
- After setting it at the posistion of choice
- Right click on the multimeter scene in OBS and presws on filters
- ![image](https://github.com/atulravi/virtualmultimeter/assets/70395057/904f7881-1219-4725-8a10-cdca87e36406)
- Press on the + and add chroma key
- ![image](https://github.com/atulravi/virtualmultimeter/assets/70395057/369c583d-99f8-4433-bb40-43c13a91d28d)
- Choose custom key colour type
- ![image](https://github.com/atulravi/virtualmultimeter/assets/70395057/06987eff-c960-40f2-b35e-82ef884db330)
- Select colour and add HTML code #00FFFF
- ![image](https://github.com/atulravi/virtualmultimeter/assets/70395057/c3282e1a-5c7a-41df-a597-4c98c7a98cf5)
- Once done, save and you are good to go. 

# Device pictures:
Please note that the inline socket version that can be directly plugged into a multimeter is still in development and will be released soon. Until then, either frankenstien it in the multimeter of your choice, or add a 7 segment display and use it as a seperate device. 
- PostBox enclosure type
![20230530_184754 1]![20230530_190719](https://github.com/atulravi/virtualmultimeter/assets/70395057/ec43698d-8a23-4def-9722-aff314b54116)
![20230530_184754](https://github.com/atulravi/virtualmultimeter/assets/70395057/107829bd-7a2b-4b75-a023-cc90e88a87e5)

(https://github.com/atulravi/virtualmultimeter/assets/70395057/ee1c3f66-1de1-4b3f-8a09-165dc8763705)
# Frankenstiend in to a DMM
![IMG_20230523_130141](https://github.com/atulravi/virtualmultimeter/assets/70395057/43923c6d-7ddd-4d40-840c-bb7679e5dd3c)
![IMG_20230523_130229](https://github.com/atulravi/virtualmultimeter/assets/70395057/d38f3c12-5bbb-4b79-af68-2737288a3691)

(BEWARE. IF YOU RUIN YOUR DMM, I TAKE NO RESPONSIBILITY. RISKS ARE INVOLVED WITH OSSH)
