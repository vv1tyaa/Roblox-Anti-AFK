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
    print("[3] - Custom")
    print("[4] - Credits")

def get_interval(interval):
    return random.randint(60, 600) if interval is None else interval

def action(keys, hold_time):
    random.shuffle(keys)
    for key in keys:
        keyboard.press(key)
        time.sleep(hold_time)
        keyboard.release(key)
        time.sleep(0.05)

def custom_action(custom_actions):
    total_actions = len(custom_actions)
    for i, action_item in enumerate(custom_actions):
        key = action_item['key']
        hold = action_item['hold']
        keyboard.press(key)
        time.sleep(hold)
        keyboard.release(key)
        
        if i < total_actions - 1:
            interval = action_item.get('interval', 0)
            if interval > 0:
                time.sleep(interval)

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
    print(">>> ", end="", flush=True)

def custom_setup():
    clear_screen()
    print("=== Custom Anti-AFK Setup ===")
    print("You will define a sequence of key presses (max 32 actions).")
    print("For each action, specify the key, hold duration, and interval to the next action.")
    print("Commands: 'back' - go to previous action, 'done' - finish, 'reset' - clear all actions\n")
    
    custom_actions = []
    action_num = 1
    
    while len(custom_actions) < 32:
        print(f"Action {action_num} (current: {len(custom_actions)}):")
        
        print("  Key (w, a, s, d, space):")
        key = input("  >>> ").lower().strip()
        
        if key == 'done':
            break
        if key == 'back':
            if custom_actions:
                removed = custom_actions.pop()
                action_num -= 1
                print(f"  Removed action {action_num} ({removed['key']} {removed['hold']}s)\n")
            else:
                print("  No actions to go back to.\n")
            continue
        if key == 'reset':
            custom_actions.clear()
            action_num = 1
            print("  All actions cleared.\n")
            continue
        
        if key not in ['w', 'a', 's', 'd', 'space']:
            print("  Invalid key. Use w, a, s, d, or space.\n")
            continue
        
        print("  Hold duration (seconds):")
        hold_input = input("  >>> ").lower().strip()
        if hold_input == 'back':
            continue
        if hold_input == 'reset':
            custom_actions.clear()
            action_num = 1
            print("  All actions cleared.\n")
            continue
        if hold_input == 'done':
            break
        
        try:
            hold = float(hold_input)
            if hold <= 0:
                print("  Hold duration must be positive.\n")
                continue
        except ValueError:
            print("  Invalid number.\n")
            continue
        
        print("  Interval to next action (seconds, 0 for no delay):")
        interval_input = input("  >>> ").lower().strip()
        if interval_input == 'back':
            continue
        if interval_input == 'reset':
            custom_actions.clear()
            action_num = 1
            print("  All actions cleared.\n")
            continue
        if interval_input == 'done':
            break
        
        try:
            interval = float(interval_input)
            if interval < 0:
                print("  Interval cannot be negative.\n")
                continue
        except ValueError:
            print("  Invalid number.\n")
            continue
        
        custom_actions.append({
            'key': key,
            'hold': hold,
            'interval': interval
        })
        action_num += 1
        print()
    
    if not custom_actions:
        print("No actions defined. Using default (W 0.2s).")
        custom_actions = [{'key': 'w', 'hold': 0.2, 'interval': 0}]
    
    if custom_actions and custom_actions[-1].get('interval', 0) > 0:
        custom_actions[-1]['interval'] = 0
    
    print(f"\nCustom sequence saved! ({len(custom_actions)} actions)")
    print("Press Enter to continue...")
    input()
    clear_screen()
    print_ascii_art()
    print(">>> ", end="", flush=True)
    
    return custom_actions

def main_menu():
    if os.name == 'nt':
        os.system('mode con cols=120 lines=40')
        os.system('title Anti-AFK by vv1tyaa')
    
    clear_screen()
    maximize_console()
    time.sleep(0.1)
    print_ascii_art()
    
    custom_actions = None
    custom_interval_type = None
    custom_interval_value = None
    
    while True:
        print(">>> ", end="")
        choice = input().strip()
        print()
        
        if choice == '4':
            credits()
            continue
        
        if choice == '3':
            custom_actions = custom_setup()
            clear_screen()
            print_ascii_art()
            print("Select overall interval type for custom mode:")
            print("[1] - Random intervals")
            print("[2] - Fixed interval")
            interval_choice = input(">>> ").strip()
            print()
            if interval_choice == 'back':
                clear_screen()
                print_ascii_art()
                continue
            if interval_choice == '3':
                credits()
                continue
            custom_interval_type = interval_choice
            if interval_choice == '1':
                custom_interval_value = None
            elif interval_choice == '2':
                print("Enter interval in seconds:")
                interval_val = input(">>> ").strip()
                if interval_val == 'back':
                    clear_screen()
                    print_ascii_art()
                    continue
                try:
                    custom_interval_value = int(interval_val)
                except ValueError:
                    print("Invalid number. Using default 100.\n")
                    custom_interval_value = 100
            else:
                print("Invalid choice. Using default.\n")
                custom_interval_value = None
            print()
            break
        
        if choice in ['1', '2']:
            break
        
        print("Invalid choice. Press 1, 2, 3 or 4.\n")
        print()
    
    if choice == '3':
        while True:
            roblox_window = get_roblox_window()
            if roblox_window:
                bring_to_foreground(roblox_window)
                custom_action(custom_actions)
            else:
                print("Roblox not found. Waiting...\n")
            
            time.sleep(get_interval(custom_interval_value))
        
        return
    
    interval_choice = choice
    
    while True:
        print("[1] - All keys")
        print("[2] - Movement keys")
        print("[3] - Jump Key")
        mode_choice = input(">>> ").lower().strip()
        print()
        
        if mode_choice == 'back':
            clear_screen()
            print_ascii_art()
            continue
        
        if mode_choice in ['1', '2', '3']:
            break
        
        print("Invalid choice.\n")
        print()
    
    while True:
        if interval_choice == '1':
            interval = None
            break
        else:
            print("Enter interval in seconds:")
            interval_input = input(">>> ").lower().strip()
            print()
            if interval_input == 'back':
                clear_screen()
                print_ascii_art()
                continue
            try:
                interval = int(interval_input)
                break
            except ValueError:
                print("Invalid number.\n")
                print()
    
    keys = {
        '1': ['space', 'w', 'a', 's', 'd'],
        '2': ['w', 'a', 's', 'd'],
        '3': ['space']
    }.get(mode_choice, ['space'])
    
    print("Press duration mode:")
    print("[1] - Short (0.2 seconds)")
    print("[2] - Medium (1 second)")
    print("[3] - Long (3 seconds)")
    print("[4] - Custom (enter your own)")
    
    hold_choice = input(">>> ").lower().strip()
    print()
    
    if hold_choice == 'back':
        clear_screen()
        print_ascii_art()
        main_menu()
        return
    
    if ' ' in hold_choice:
        parts = hold_choice.split()
        if parts[0] == '4' and len(parts) > 1:
            try:
                hold_time = float(parts[1])
                if hold_time <= 0:
                    print("Invalid value. Using default 0.2.\n")
                    hold_time = 0.2
            except:
                print("Invalid input. Using default 0.2.\n")
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
        print("Enter hold duration in seconds:")
        hold_input = input(">>> ")
        print()
        if hold_input == 'back':
            clear_screen()
            print_ascii_art()
            main_menu()
            return
        try:
            hold_time = float(hold_input)
            if hold_time <= 0:
                print("Invalid value. Using default 0.2.\n")
                hold_time = 0.2
        except:
            print("Invalid input. Using default 0.2.\n")
            hold_time = 0.2
    else:
        print("Invalid choice. Using default 0.2.\n")
        hold_time = 0.2
    
    print(f"Hold duration set to {hold_time} seconds.\n")
    
    while True:
        roblox_window = get_roblox_window()
        if roblox_window:
            bring_to_foreground(roblox_window)
            action(keys, hold_time)
        else:
            print("Roblox not found. Waiting...\n")
        
        time.sleep(get_interval(interval))

if __name__ == '__main__':
    main_menu()
