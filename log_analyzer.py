"""Count failed SSH logins in a Linux auth.log file."""

import csv
from importlib.resources import path
import re                            
from collections import Counter      

LOG_FILE = "sample_logs/sample_auth.log"  

FAILED_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)


def parse_log(path):
    """Read the log and return two Counters: failures per user, per IP."""
    user_counts = Counter()          
    ip_counts = Counter()            

    with open(path, encoding="utf-8") as log:   
        for line in log:                         
            match = FAILED_PATTERN.search(line)  # does this line match?
            if match:                            # None means "no match"
                user_counts[match.group("user")] += 1   
                ip_counts[match.group("ip")] += 1     

    return user_counts, ip_counts


def print_counts(title, counts):
    """Print a heading, then each item and its count, highest first."""
    print(f"\n{title}")
    print("-" * len(title))                   
    for name, count in counts.most_common():     
        print(f"{name:<20}{count}")              # name padded to 20 characters


def main():
    user_counts, ip_counts = parse_log(LOG_FILE)
    total = sum(ip_counts.values())             
    print(f"Total failed logins: {total}")
    print_counts("Failed logins by username", user_counts)
    print_counts("Failed logins by IP address", ip_counts)


    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ip", "failed_logins", "flagged"])   
        for ip, count in ip_counts.most_common():              
            writer.writerow([ip, count, count > 5])            
    print("\nResults saved to results.csv")


if __name__ == "__main__":   
    main()

