import random
import keyboard
import time
import pygetwindow as gw
import ctypes
import os

SendInput = ctypes.windll.user32.SendInput

key_map = {
    'w': 'w',
    'a': 'a',
    's': 's',
    'd': 'd',
    'space': 'space'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    print(r"""
_______    ______ _______    ______   ____________    ________    ________   ______   _____     _____            _____         
\      |  |      |\      |  |      | /            \  /        \  /        \ |\     \ |     |  /      |_        /      |_       
 |     /  /     /| |     /  /     /||\___/\  \\___/||\         \/         /|\ \     \|     | /         \      /         \      
 |\    \  \    |/  |\    \  \    |/  \|____\  \___|/| \            /\____/ | \ \           ||     /\    \    |     /\    \     
 \ \    \ |    |   \ \    \ |    |         |  |     |  \______/\   \     | |  \ \____      ||    |  |    \   |    |  |    \    
  \|     \|    |    \|     \|    |    __  /   / __   \ |      | \   \____|/    \|___/     /||     \/      \  |     \/      \   
   |\         /|     |\         /|   /  \/   /_/  |   \|______|  \   \             /     / ||\      /\     \ |\      /\     \  
   | \_______/ |     | \_______/ |  |____________/|            \  \___\           /_____/  /| \_____\ \_____\| \_____\ \_____\ 
    \ |     | /       \ |     | /   |           | /             \ |   |           |     | / | |     | |     || |     | |     | 
     \|_____|/         \|_____|/    |___________|/               \|___|           |_____|/   \|_____|\|_____| \|_____|\|_____|
    """)
    print("\n~~~~~ vv1tyaa's Anti-AFK")
    print("[1] - Random intervals")
    print("[2] - Fixed interval")
    print("[3] - Credits")

def get_interval(interval):
    return random.randint(60, 600) if interval is None else interval

def action(keys, hold_time):
    random.shuffle(keys)
    for key in keys:
        keyboard.press(key)
        time.sleep(hold_time)
        keyboard.release(key)
        time.sleep(0.05)

def get_roblox_window():
    windows = gw.getWindowsWithTitle("Roblox")
    if not windows:
        return None
    for window in windows:
        if "Roblox" in window.title:
            return window
    return None

def bring_to_foreground(window):
    try:
        if window.isMinimized:
            window.restore()
        window.activate()
        time.sleep(0.5)
    except Exception as e:
        print(f"Error activating window: {e}")

def maximize_console():
    if os.name == 'nt':
        try:
            kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
            user32 = ctypes.WinDLL('user32', use_last_error=True)
            hwnd = kernel32.GetConsoleWindow()
            user32.ShowWindow(hwnd, 3)
            time.sleep(0.05)
        except:
            pass

def credits():
    clear_screen()
    print("~ Created by vv1tyaa")
    print("")
    print("Press enter to return ...")
    input()
    clear_screen()
    maximize_console()
    time.sleep(0.2)
    clear_screen()
    print_ascii_art()
    print("\n>>> ", end="", flush=True)

def main_menu():
    if os.name == 'nt':
        os.system('mode con cols=120 lines=40')
        os.system('title Anti-AFK by vv1tyaa')
    
    clear_screen()
    maximize_console()
    time.sleep(0.1)
    print_ascii_art()
    
    while True:
        choice = input("\n>>> ")
        
        if choice == '3':
            credits()
            continue
        
        if choice in ['1', '2']:
            break
        
        print("Invalid choice. Press 1, 2 or 3.")
    
    interval_choice = choice
    mode_choice = input('[1] All keys\n[2] Movement keys\n[3] Jump Key\n>>> ')
    
    interval = None if interval_choice == '1' else int(input('Enter interval in seconds: '))
    
    keys = {
        '1': ['space', 'w', 'a', 's', 'd'],
        '2': ['w', 'a', 's', 'd'],
        '3': ['space']
    }.get(mode_choice, ['space'])
    
    print("\nPress duration mode:")
    print("[1] - Short (0.2 seconds)")
    print("[2] - Medium (1 second)")
    print("[3] - Long (3 seconds)")
    print("[4] - Custom (enter your own)")
    
    hold_choice = input(">>> ")
    
    if ' ' in hold_choice:
        parts = hold_choice.split()
        if parts[0] == '4' and len(parts) > 1:
            try:
                hold_time = float(parts[1])
                if hold_time <= 0:
                    print("Invalid value. Using default 0.2.")
                    hold_time = 0.2
            except:
                print("Invalid input. Using default 0.2.")
                hold_time = 0.2
        else:
            hold_time = 0.2
    elif hold_choice == '1':
        hold_time = 0.2
    elif hold_choice == '2':
        hold_time = 1.0
    elif hold_choice == '3':
        hold_time = 3.0
    elif hold_choice == '4':
        try:
            hold_time = float(input("Enter hold duration in seconds: "))
            if hold_time <= 0:
                print("Invalid value. Using default 0.2.")
                hold_time = 0.2
        except:
            print("Invalid input. Using default 0.2.")
            hold_time = 0.2
    else:
        print("Invalid choice. Using default 0.2.")
        hold_time = 0.2
    
    print(f"Hold duration set to {hold_time} seconds.")
    
    while True:
        roblox_window = get_roblox_window()
        if roblox_window:
            bring_to_foreground(roblox_window)
            action(keys, hold_time)
        else:
            print("Roblox not found. Waiting...")
        
        time.sleep(get_interval(interval))

if __name__ == '__main__':
    main_menu()