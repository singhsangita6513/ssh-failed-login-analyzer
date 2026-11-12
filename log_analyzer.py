"""Count failed SSH logins in a Linux auth.log file (learning project)."""

import re                            # regular expressions: find text patterns
from collections import Counter      # a dictionary that counts things 

LOG_FILE = "sample_logs/sample_auth.log"   # path to the log I want to read

# Matches lines like:
#   Failed password for root from 203.0.113.5 port 22 ssh2
#   Failed password for invalid user admin from 198.51.100.7 port 22 ssh2
FAILED_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)


def parse_log(path):
    """Read the log and return two Counters: failures per user, per IP."""
    user_counts = Counter()          # e.g. {"root": 5, "admin": 3}
    ip_counts = Counter()            # e.g. {"203.0.113.5": 6}

    with open(path, encoding="utf-8") as log:   # opens the file, closes it after
        for line in log:                         # read one line at a time
            match = FAILED_PATTERN.search(line)  # does this line match?
            if match:                            # None means "no match"
                user_counts[match.group("user")] += 1   # add 1 for this user
                ip_counts[match.group("ip")] += 1       # add 1 for this IP

    return user_counts, ip_counts


def print_counts(title, counts):
    """Print a heading, then each item and its count, highest first."""
    print(f"\n{title}")
    print("-" * len(title))                      # underline as long as title
    for name, count in counts.most_common():     # sorted, biggest first
        print(f"{name:<20}{count}")              # name padded to 20 characters


def main():
    user_counts, ip_counts = parse_log(LOG_FILE)
    total = sum(ip_counts.values())              # every failure has one IP
    print(f"Total failed logins: {total}")
    print_counts("Failed logins by username", user_counts)
    print_counts("Failed logins by IP address", ip_counts)


if __name__ == "__main__":   # run main() only when this file is run directly
    main()