# 🔍 Python Port Scanner

A minimal command‑line port scanner written in pure Python. Give it one or more targets (IPv4 address or hostname), choose how many ports you want to probe, and the script will quickly report which ports are open and, when possible, grab the service banner.

Why another port scanner?This project is intentionally small—under 100 lines—to be easy to read, tweak, and extend. It’s a great starting point if you’re learning network programming or need a lightweight scanner to embed in a bigger tool.


# ✨ Features

Scan a single host or multiple hosts (comma‑separated) in one run

Banner grabbing – fetch up to 1 KB from open sockets to identify running services

Accepts hostnames or raw IP addresses (uses IPy to validate/convert)

Adjustable speed/accuracy – change the socket timeout to trade accuracy for speed

Zero external dependencies beyond IPy


🚀 Quick Start

# Clone the repo
$ git clone https://github.com/youruser/python-port-scanner.git
$ cd python-port-scanner

# (Optional) create a virtual environment
$ python -m venv .venv && source .venv/bin/activate

# Install the single dependency
$ pip3 install IPy

# Run the scanner
$ python port_scanner.py

You’ll be prompted for the target(s) and the number of ports to scan.


⚙️ Usage Examples

Scan the first 1000 ports of a single host

$ python port_scanner.py
[+] Enter target/s to scan (split multiple targets with ,): scanme.nmap.org
[+] Enter number of ports you want to scan: 1000

Scan multiple hosts

$ python port_scanner.py
[+] Enter target/s to scan (split multiple targets with ,): 192.168.1.10,example.com,10.0.0.5
[+] Enter number of ports you want to scan: 500

Tweak the timeout (edit scan_port)

If you need higher accuracy (at the cost of speed), increase the timeout:

sock.settimeout(1)  # default is 0.5 seconds


# 🗂️ Project Structure

python-port-scanner/
├── port_scanner.py      # main script (≈90 lines)
└── README.md            # you are here


# 🛠️ How It Works (High Level)

Input parsing – Accept a single string of targets, split on commas, and normalise each to an IPv4 address with IPy/socket.gethostbyname().

Port loop – For every port in range(1, n) create a TCP socket and attempt to connect().

Timeout – Sockets time out after 0.5 s (configurable) to keep the scan quick.

Banner grabbing – If a connection succeeds, attempt to recv(1024) bytes to capture the service banner.

Output – Print [+] Open port {port}: {banner} or simply [+] Open port {port} if no banner is returned.

Because closed/filtered ports raise exceptions, they’re silently ignored to keep the output clean.


# 📋 Requirements

Python 3.7 or newer

IPy (install via pip)


# 👤 Original Author - Mohamed Ezzat - mohamedaezzat.guthub.io

I would highly recommend checking out his GitHub. he has great hands-on projects to learn concepts. 


