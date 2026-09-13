
<img width="1338" height="479" alt="image" src="https://github.com/user-attachments/assets/4dbbead8-c5a6-49a9-82a6-8337103f185f" />

# Artisan Pilot

A simple Python CLI for Windows that streamlines common Laravel setup and development commands.
## Requirements

- Python 3.8 or newer
- PHP and Composer installed (required to run Laravel/artisan commands)
- A Laravel project (the script should be run from inside your Laravel project folder)

## Installation

1. Clone or download this repository into your Laravel project folder.

2. Install the required Python libraries:

```bash
pip install pyfiglet colorama
```
## Usage

Run the script from inside your Laravel project directory:

```bash
python artisan-pilot.py
```

You will see a menu with the following options:

```
1. composer install
2. create .env
3. migrate database
4. start application
5. clear cache
6. routes list
7. Create model
8. Create controller
9. Create migration
0. Exit
```

Enter the number corresponding to the action you want to run, and Artisan Pilot will execute the matching command for you.

