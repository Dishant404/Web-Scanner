Dishant Web Scanner 🛡️

Dishant Web Scanner is a beginner-friendly web security tool designed to help you quickly check the security posture of websites. It performs security header checks, common port scans, and SSL certificate verification.

Features
Security Header Check ✅
Checks if essential HTTP security headers are present:
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
X-Frame-Options
X-XSS-Protection
Port Scanner 🔌
Scans common ports (21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080) to identify open services.
SSL Certificate Check 🔐
Verifies if a website has a valid SSL certificate, and displays issuer and expiration date.
Clean CLI Interface 💻
Includes an ASCII banner and structured console output for readability.
Installation

Make sure you have Python 3 installed. Then, install the required dependencies:

pip install requests

Clone the repository:

git clone https://github.com/Dishant404/dishant-web-scanner.git
cd dishant-web-scanner
Usage

Run the scanner using Python:

python3 scanner.py

Enter the website URL when prompted:

Enter website (example: https://example.com): 

The scanner will display:

Security headers status
Open ports on the target host
SSL certificate details

Sample output:

[+] Checking Security Headers...
[✔] Content-Security-Policy is present
[✘] Strict-Transport-Security is missing
...

[+] Scanning Common Ports...
[OPEN] Port 80
[OPEN] Port 443
...

[+] Checking SSL Certificate...
[✔] SSL Certificate Found
Issuer: [('organizationName', 'Let's Encrypt')]
Valid Till: Mar 30 12:00:00 2026 GMT
Contributing

Contributions are welcome! You can improve the scanner by:

Adding more ports for scanning
Implementing HTTPS enforcement checks
Adding vulnerability scanning (XSS, SQLi)
Creating a GUI or CLI enhancements
License

This project is open source and licensed under the MIT License.

Author

Dishant404 – GitHub

Developed by: https.dishant.ceh
