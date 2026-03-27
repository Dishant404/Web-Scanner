Dishant Web Scanner 🛡️

Dishant Web Scanner is a simple web security tool that helps you check the safety of websites. It scans for security headers, open ports, and SSL certificates.

Features
✅ Security Header Check – See if important HTTP headers are present:
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
X-Frame-Options
X-XSS-Protection
🔌 Port Scanner – Scan common ports like 80, 443, 22, 8080, etc. to find open services.
🔐 SSL Certificate Check – Check if the website has a valid SSL certificate and see its issuer and expiry date.
💻 Easy Command-Line Interface – Simple input and clear results with a cool ASCII banner.
Installation
Make sure Python 3 is installed.
Install required Python package:
pip install requests
Clone the repository:
git clone https://github.com/Dishant404/dishant-web-scanner.git
cd dishant-web-scanner
How to Use
Run the scanner:
python3 scanner.py
Enter the website URL when asked:
Enter website (example: https://example.com):
Wait for results. The scanner will show:
Security headers
Open ports
SSL certificate details

Sample Output:

[+] Checking Security Headers...
[✔] Content-Security-Policy is present
[✘] Strict-Transport-Security is missing

[+] Scanning Common Ports...
[OPEN] Port 80
[OPEN] Port 443

[+] Checking SSL Certificate...
[✔] SSL Certificate Found
Issuer: [('organizationName', 'Let's Encrypt')]
Valid Till: Mar 30 12:00:00 2026 GMT
Contributing

You can help make this tool better by:

Adding more ports to scan
Checking HTTPS redirect enforcement
Adding vulnerability tests like XSS or SQL injection
Improving the CLI interface
License

This project is open source under the MIT License.

Author

Dishant404 – GitHub

Developed by: https.dishant.ceh
