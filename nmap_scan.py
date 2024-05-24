# To run script: python nmap_scan.py <target IP> <output_file> 
# Example: python nmap_scan.py 192.168.x.x scan_results.txt

import subprocess
import sys

def run_nmap(target, output_file):
    try:
        # Run the Nmap command
        result = subprocess.run(['nmap',  '-O', '-sV', '-oN', output_file, target], check=True, text=True, capture_output=True)
        print(f"Nmap scan completed succeccfully. Results saved to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Nmap scan failed. Error: {e.stderr}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nmap_scan.py <target> <output_file>")
        sys.exit(1)

    target = sys.argv[1]
    output_file = sys.argv [2]

    run_nmap(target, output_file)  