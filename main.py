import time
import os
import subprocess

# Function to simulate loading
def load_app():
    print("LOADING!!!")
    progress_stages = [
        '#########  (15%)',
        '########################## (30%)',
        '############################################## (60%)',
        '######################################################################### (80%)',
        '####################################################################################### (100%)'
    ]
    for stage in progress_stages:
        print(f'\r{stage}', end='')
        time.sleep(1)
    print("\n")
    os.system('clear')

# Function to display MENU in ASCII art
def display_menu():
    menu_art = """
    
    ███    ███ ███████ ███    ██ ██    ██ 
    ████  ████ ██      ████   ██ ██    ██ 
    ██ ████ ██ █████   ██ ██  ██ ██    ██ 
    ██  ██  ██ ██      ██  ██ ██ ██    ██ 
    ██      ██ ███████ ██   ████  ██████  
                                          
    """
    print(menu_art)
	print("Written by: Ashik Karki")
	print("Email: karkiashik5@gmail.com")

# Helper function to run shell commands and capture output
def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Function to handle menu options
def main_menu():
    options = [
        "systeminfo", "hardwareinfo", "pciinfo", "securecopy", 
        "logininfo", "uptime", "cronjobs", "pwd", 
        "service restart", "ping", "uncompress(bz2)", 
        "uncompress(gz)", "compress(tar)", "Quit"
    ]

    while True:
        print("\n".join([f"{i + 1}. {opt}" for i, opt in enumerate(options)]))
        choice = input("Please enter your choice: ")

        if choice == '1':  # systeminfo
            run_command("uname -a")
        elif choice == '2':  # hardwareinfo
            run_command("lshw")
        elif choice == '3':  # pciinfo
            run_command("lspci")
        elif choice == '4':  # securecopy
            username = input("Enter remote user's name: ")
            ip = input("Enter remote user's IP or domain name: ")
            remote_path = input("Enter full path of remote file: ")
            save_path = input("Enter path to be saved: ")
            run_command(f"scp {username}@{ip}:{remote_path} {save_path}")
        elif choice == '5':  # logininfo
            run_command("pinky")
        elif choice == '6':  # uptime
            run_command("uptime")
        elif choice == '7':  # cronjobs
            run_command("crontab -l")
        elif choice == '8':  # pwd
            run_command("pwd")
        elif choice == '9':  # service restart
            service = input("Enter service name: ")
            run_command(f"sudo systemctl restart {service}")
        elif choice == '10':  # ping
            ip = input("Enter IP or domain name: ")
            run_command(f"ping -c 4 {ip}")
        elif choice == '11':  # uncompress(bz2)
            filepath = input("Enter file path: ")
            filename = input("Enter file name: ")
            extract_path = input("Enter path to be extracted: ")
            print_progress()
            run_command(f"tar -jxvf {filepath}/{filename} -C {extract_path}")
        elif choice == '12':  # uncompress(gz)
            filepath = input("Enter file path: ")
            filename = input("Enter file name: ")
            extract_path = input("Enter path to be extracted: ")
            print_progress()
            run_command(f"tar -zxvf {filepath}/{filename} -C {extract_path}")
        elif choice == '13':  # compress(tar)
            filename = input("Enter file name for compression: ")
            path = input("Enter path which needs to be compressed: ")
            run_command(f"tar -cvf {filename} {path}")
        elif choice == '14':  # Quit
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

# Function to simulate compression/uncompression progress
def print_progress():
    stages = [
        '#####                 (33%)',
        '##############        (66%)',
        '####################  (100%)'
    ]
    for stage in stages:
        print(f'\r{stage}', end='')
        time.sleep(1)
    print('\n')

# Main function to load the app and display menu
def main():
    load_app()
    display_menu()
    main_menu()

if __name__ == "__main__":
    main()
