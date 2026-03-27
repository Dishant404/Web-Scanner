# Dishant Web Scanner 🛡️

**Dishant Web Scanner** is a simple and easy-to-use web security tool. It helps you check a website’s security by scanning for security headers, open ports, and SSL certificates.

---

## Features

- ✅ **Security Header Check**  
  Checks important HTTP headers to see if the website is secure:  
  - Content-Security-Policy  
  - Strict-Transport-Security  
  - X-Content-Type-Options  
  - X-Frame-Options  
  - X-XSS-Protection  

- 🔌 **Port Scanner**  
  Scans common ports like 21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080 to find open services.

- 🔐 **SSL Certificate Check**  
  Verifies if the website has a valid SSL certificate and shows the issuer and expiration date.

- 💻 **Easy CLI Interface**  
  Clean ASCII banner and structured output for quick results.

---

## Installation

1. Make sure **Python 3** is installed on your system.
2. Install the required Python library:

```bash
pip install requests
```
#Clone this repository:
```bash
git clone https://github.com/Dishant404/web-scanner.git
cd dishant-web-scanner
```
#Usage
1. Run the scanner:
```bash
python3 scanner.py
```
2. Enter the website URL when prompted:
```bash
Enter website (example: https://example.com):
```  
3. The scanner will show:
   
•Security headers

•Open ports

•SSL certificate details

#Example Output:
```bash
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
```
Contributing

Contributions are welcome! You can help improve this tool by:

Adding more ports to scan
Checking HTTPS enforcement
Adding vulnerability tests like XSS or SQL injection
Enhancing the CLI interface

License

This project is open source under the MIT License.

Author

Dishant404 – GitHub

Developed by: https.dishant.ceh
