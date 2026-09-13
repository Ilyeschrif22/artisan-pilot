import subprocess
import pyfiglet
from colorama import init, Fore, Style

def install_composer():
    print("Installing Composer...")

    result = subprocess.run(["cmd", "/c", "composer", "install"],text=True)

    print(result.stdout)

    if result.stderr:
        print("Error:", result.stderr)

def run_application():
    print("Running the application...")

    result = subprocess.run(["cmd", "/c", "php", "artisan", "serve"],text=True)

    print(result.stdout)

    if result.stderr:
        print("Error:", result.stderr)

def database_migration():
    print("Migrating the database...")

    result = subprocess.run(["cmd", "/c", "php", "artisan", "migrate"],text=True)

    print(result.stdout)

    if result.stderr:
        print("Error:", result.stderr)

def clear_cache():
    print("Clearing the cache...")

    result = subprocess.run(
        ["cmd", "/c", "php", "artisan", "optimize:clear"],
        text=True,
        capture_output=True
    )

    print(result.stdout)

    if result.stderr:
        print("Error:", result.stderr)
    
    print("this might take a while, please wait...")
    # Refresh Composer autoload
    result = subprocess.run(
        ["cmd", "/c", "composer", "dump-autoload"],
        text=True,
        capture_output=True
    )

    print(result.stdout)

    if result.stderr:
        print("Error:", result.stderr)

def list_routes():
    print("Listing routes...")

    result = subprocess.run(["cmd", "/c", "php", "artisan", "route:list"],text=True)

    print(result.stdout)

    if result.stderr:
        print("Error:", result.stderr)

def menu():
    print("1. composer install")
    print("2. create .env")
    print("3. migrate database")
    print("4. start application")
    print("5. clear cache")
    print("6. routes list")

    choice = input("Enter your choice: ")
    return choice

def response():
     while True:
        choice = menu()
        if choice == "1":
            install_composer()
        elif choice == "2":
            print("Creating .env file...")
        elif choice == "3":
            database_migration()
        elif choice == "4":
            run_application()
        elif choice == "5":
            clear_cache()
        elif choice == "6":
            list_routes()
        else:
            print("Invalid choice. Please try again.")

def print_banner():
    ascii_art = pyfiglet.figlet_format("artisan-pilot", font="slant")
    print(Fore.CYAN + ascii_art)
    print(Fore.WHITE + "    Laravel artisan, on autopilot  " + Fore.YELLOW + "by ilyes" + Fore.WHITE + "    version " + Fore.GREEN + "1.0.0")
    print()

def main():
    print("Welcome to Artisan Pilot!")
    init(autoreset=True)  # makes colorama work properly on Windows terminal
    
    print_banner()
    response()


if __name__ == "__main__":
    main()