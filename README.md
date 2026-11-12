# SSH Failed Login Analyzer

A Python script that reads a Linux SSH log (auth.log format) and counts failed logins by username and by IP address. It saves the IP counts to a CSV file and flags any IP with more than 5 failures.

 It only uses a fake sample log I made, with example IP addresses (192.0.2.x, 198.51.100.x, 203.0.113.x). No real logs or real data are included.

## How to run

You need Python 3. No extra packages are needed.

```
python3 log_analyzer.py
```

It reads `sample_logs/sample_auth.log` and saves the results to `results.csv`.

## Sample output

```
Total failed logins: 13

Failed logins by username
-------------------------
root                6
admin               2
test                1
oracle              1
ubuntu              1
bob                 1
alice               1

Failed logins by IP address
---------------------------
203.0.113.10        7
198.51.100.23       4
192.0.2.77          1
192.0.2.5           1

Results saved to results.csv
```

In the sample, 203.0.113.10 tried to log in as root many times in a few seconds, which looks like a brute-force attempt. It is the only IP flagged in the CSV.

  ## Problems I ran into

My first run showed 0 failed logins. I checked the input with `wc -l` and `grep -c`
and found the sample log file was empty because I hadn't saved it. After fixing that,
the script found 13 failures, which matched my count by hand.

<img width="1388" height="857" alt="Image" src="https://github.com/user-attachments/assets/44fae058-9c87-488e-85e9-53f826f70094" />


## What I learned

- Using a regular expression to find failed login lines and pull out the username and IP
- Counting with Counter from the collections module
- Writing a CSV file with the csv module
- Reading Python error messages to fix my own bugs
- Using git to save my work in commits

## Limitations

- Only tested on the sample log, not on a real server
- The log file and the threshold are set in the code
- Only counts "Failed password" lines
