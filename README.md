# SunshinePythonResolutionSwitcher
Python resolution switcher for Windows 11 machines when using sunshine to remote control pc. 

# Installation - using packaged EXE file

 1. Download the source code via zip.
 2. Open the dist folder in file explorer.
 3. Edit the config.json using notedpad.
 - Modify the Sunshine log location to where the sunshine logs are stored (Note in sunshine you
    need verbose logging for this to work).    
  - Set your base resolution height, width, and refreshrate. Due to the implementation of this,
    set a resolution and refreshrate that your system has been configured for before. Any configuration that is not visible in the windows display settings is not a valid option. You may need to use a custom resolution tool to add or delete valid resolution values.

# Building from Scratch
1. Download the sorce code via zip file or cloning repo etc.
2. Extract the contents of the ziped folder to a location of your choice.
3. Use the following command to install python packages to build the python program from scratch. (Requires python3 to be installed) 
     - pip install pywin32
     - pip install pyinstaller
4. Right click inside the folder and open a terminal in the location of SunshinePythonResolutionSwitcher.py

   <img width="1028" height="548" alt="image" src="https://github.com/user-attachments/assets/a687861f-d1d0-40b5-928f-aebad883eded" />

5. Paste the following command into your terminal window.
    - pyinstaller --onefile --noconsole SunshinePythonResolutionSwitcher.py -y && copy config.json dist\config.json



# Configuring script to automatically start with Windows 11
1. Open task manager and on the right hand panel click on startup apps.
   - <img width="236" height="390" alt="image" src="https://github.com/user-attachments/assets/2ed4c504-3efc-4587-80a2-6181adf9e025" />

2. Click on the run new task button on the top of the page.
   - <img width="135" height="44" alt="image" src="https://github.com/user-attachments/assets/72f2171e-3068-4336-a48c-4e61e8d7937c" />

3. The Create new task window will open, press browse and select the SunshinePythonResolutionSwitcher.exe
4. Thats it! Now the script will now be a task that runs on startup. 
