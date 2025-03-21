import datetime
import os
import random
import subprocess

def log_contribution():
    filename = "daily_contributions.txt"
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    entry = f"[{current_date}] Automated daily contribution logged.\n"
    
    with open(filename, "a") as file:
        file.write(entry)
    
    print(f"Entry added: {entry.strip()}")

def commit_to_github():
    os.system("git add daily_contributions.txt")
    os.system(f"git commit -m 'Automated commit for {datetime.datetime.now().strftime('%Y-%m-%d')}'")
    os.system("git push origin main")

def should_commit_today(probability=0.7):
    return random.random() < probability

if __name__ == "__main__":
    if should_commit_today():
        log_contribution()
        commit_to_github()
    else:
        print("Skipping commit today.")
