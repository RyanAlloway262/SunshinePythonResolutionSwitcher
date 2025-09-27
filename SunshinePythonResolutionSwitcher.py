import time
import subprocess
import re
import pywintypes
import win32api
import win32con
import json


# Path to the Sunshine log file
CONF_FILE = "config.json"

# Function to change resolution
def change_resolution(resolution: str, rate: str):
    string_r = resolution.split('x')
    height = int(string_r[1]) 
    width = int(string_r[0])
    rate = int(rate)

    try:
        print(f"Changing resolution to {resolution} @ {rate}Hz")
        devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
        devmode.PelsWidth = width
        devmode.PelsHeight = height
        devmode.BitsPerPel = 32
        devmode.DisplayFrequency = rate
        devmode.Fields = (
            win32con.DM_PELSWIDTH |
            win32con.DM_PELSHEIGHT |
            win32con.DM_BITSPERPEL |
            win32con.DM_DISPLAYFREQUENCY
        )
        result = win32api.ChangeDisplaySettings(devmode, 0)
        if result == win32con.DISP_CHANGE_SUCCESSFUL:
            print(f"Resolution changed to {width}x{height} @ {rate}Hz")
        else:
            print(f"Failed to change resolution. Error code: {result}")

    except subprocess.CalledProcessError as e:
        print(f"Error changing resolution: {e}")

# Function to monitor log file
def monitor_log(LOG_FILE, HEIGHT, WIDTH, REFRESHRATE):
    print(f"Monitoring log file: {LOG_FILE}")
    
    # Open the log file in read mode and seek to the end (like `tail -F`)
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)  # Go to the end of the file

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            # Look for resolution change
            if "Debug: mode -- " in line:
                match_res = re.search(r"(\d+x\d+)", line)
                match_rate = re.search(r"\d+x\d+x(\d+)", line)

                if match_res and match_rate:
                    resolution = match_res.group(1)
                    rate = match_rate.group(1)
                    print(f"Client connected: {resolution} @ {rate}Hz")
                    change_resolution(resolution, rate)

            # Look for client disconnection
            if "CLIENT DISCONNECTED" in line:
                print(f"Client disconnected, reverting to {WIDTH}x{HEIGHT} @ {REFRESHRATE}")
                change_resolution(f"{WIDTH}x{HEIGHT}", f"{REFRESHRATE}")


if __name__ == "__main__":
    with open(CONF_FILE) as f:
        config = json.load(f)
    
    sunshineLogLocation = config["Sunshine_Log_Location"] 
    baseResolutionHeight = config["Base_Resolution_Height"]
    baseResolutionWidth = config["Base_Resolution_Width"]
    baseRefreshRate = config["Base_Refresh_Rate"]
    
    monitor_log(sunshineLogLocation, baseResolutionHeight, baseResolutionWidth, baseRefreshRate)
