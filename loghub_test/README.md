## Test on real SSH logs(Loghub)

Initially I experimented with fake logs, although in this part I used separate Loghub test which has public research dataset that includes real IP addresses.

## Dataset
I used the OpenSSH sample (2,000 lines from a lab server) from Loghub i.e a public research collection of system logs. I haven't added the raw log file I this repository. The results file in the folder comes from that dates and includes its IP addresses. 

## How I ran it
From the main project folder:

```
mkdir real_logs
curl -L -o real_logs/OpenSSH_2k.log https://raw.githubusercontent.com/logpai/loghub/master/OpenSSH/OpenSSH_2k.log
```

Then I changed `LOG_FILE` in `log_analyzer.py` to `real_logs/OpenSSH_2k.log`
and ran `python3 log_analyzer.py`. The `.gitignore` blocks `.log` files, so the
raw log could not be committed by accident.

<img width="1299" height="810" alt="Screenshot 2026-11-12 at 4 27 10 PM" src="https://github.com/user-attachments/assets/056ed44f-502e-4816-bc26-af5dee800378" />

## Results

- 519 failed password attempts found
- 23 source IP addresses and 62 usernames
- root was the most targeted username with 370 attempts
- 8 IPs had more than 5 failures
- One IP made 286 of the 519 attempts (over half), which looks like a single
  automated brute-force 
- Full results per IP: [loghub_results.csv]


<img width="1388" height="857" alt="Screenshot 2026-11-12 at 4 09 59 PM" src="https://github.com/user-attachments/assets/f584abca-d367-44cb-a5d0-893c7c86de7b" />
