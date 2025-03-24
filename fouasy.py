import requests
import time
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    menu = f"""
{Fore.CYAN}
8888888888                                           
888                                                  
888                                                  
8888888  .d88b.  888  888  8888b.  .d8888b  888  888 
888     d88""88b 888  888     "88b 88K      888  888 
888     888  888 888  888 .d888888 "Y8888b. 888  888 
888     Y88..88P Y88b 888 888  888      X88 Y88b 888 
888      "Y88P"   "Y88888 "Y888888  88888P'  "Y88888 
                                                 888 
                                            Y8b d88P 
                                             "Y88P"{Style.RESET_ALL}
{Fore.RED}0.{Style.RESET_ALL} Leave
{Fore.GREEN}1.{Style.RESET_ALL} Webhook Spammer

=================================================
"""
    print(menu)

def log_message(status, message, status_color):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}]{status_color}{status} {status_color}{message}{Style.RESET_ALL}")

def send_webhook(webhook_url, content):
    while True:
        response = requests.post(webhook_url, json={"content": content})
        
        if response.status_code == 204:
            log_message(f"[{Fore.GREEN}+]{Style.RESET_ALL}", "SENT MESSAGE SUCCESSFUL", Fore.GREEN)
        elif response.status_code == 429:
            retry_after = response.json().get("retry_after", 1) / 1000
            log_message(f"[{Fore.RED}-]{Style.RESET_ALL}", "WEBHOOK RATE LIMITED", Fore.RED)
            time.sleep(retry_after)
        elif response.status_code == 404:
            log_message(f"[{Fore.RED}-]{Style.RESET_ALL}", "WEBHOOK DOESN'T EXIST. STOPPING...", Fore.RED)
            break
        else:
            log_message(f"[{Fore.RED}-]{Style.RESET_ALL}", f"UNKNOWN ERROR: {response.status_code}", Fore.RED)
            break
        
        time.sleep(0.00000001)

if __name__ == "__main__":
    clear_screen()
    print_menu()
    choice = input("Select an option: ")
    if choice == "1":
        webhook_url = input("Insert WebHook url: ")
        content = input("Insert the spammed message: ")
        send_webhook(webhook_url, content)
    elif choice == "0":
        print("Stopping...")
        exit()
    else:
        print("Option not valid. Retry")


# JKLY WAS HERE
