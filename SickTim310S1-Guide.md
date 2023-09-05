# SICK TIM310S1 GUIDE
>:warning: Ubuntu 22.04, Python 3.10.12

>:pencil: Andrea Ruo

## 1. Introduction
This code allows you to retrieve measurements obtained from the TIM310S1 LaserScanner. You can customize the acquisition radius (with a limit of 4 meters) and the desired circumference arc chord value. The program will automatically calculate the range of angles needed to acquire data within a 270-degree interval.

## 2. Prerequisites
Download and install the following packages:
    
```bash
sudo python3 -m pip install pyusb
python3 -m pip install pysicktim
```
Allow non-root access: 
```bash
sudo nano /etc/udev/rules.d/sick-tim5xx.rules
```
And write the following line:
```bash
SUBSYSTEM=="usb", ACTION=="add", ATTR{idVendor}=="19a2", ATTR{idProduct}=="5001", GROUP="plugdev"
```
Press ``CTRL+X``, ``Y`` and ``ENTER`` to save and exit. Then:
```bash
sudo reboot
```

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

## 3. Scan.py
Go to ``examples``>``scan.py``
### 3.1. Settings
In the script you can change the following parameters into desired values:
```python
# Set parameters
d_max = 2.0				# Maximum distance to measure in meters
circumference_chord = 1 # Chord length desired of the circumference a d_max distance
```

### 3.2. How it works
When you run the script, you will have the distance received from the LaserScanner in the terminal. In particular, will be printed the following sentences:
```python
if average<0.0001:
	print("Free space")
elif average<=(d_max/2):
	print(f"WARNING, Nearby obstacle: {average} meters")
else: # Between d_max/2 and d_max
	print(f"Approaching obstacle: {average} meters")
```
It is possible to interrupt the script instanly by pressing ``CTRL+C``. When you do it, the script will plot the distances received from the LaserScanner.

## 4. Telegram.py
Go to ``examples``>``telegram.py``

### 4.1. How it works
This script allows you to know several functions available within the library pysicktim. 