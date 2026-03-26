import requests

def scan_website(url):

    vulnerabilities = []

    try:
        response = requests.get(url)

        # Missing security headers
        if "X-Frame-Options" not in response.headers:
            vulnerabilities.append(("Missing X-Frame-Options", "Medium"))

        if "Content-Security-Policy" not in response.headers:
            vulnerabilities.append(("Missing CSP Header", "High"))

        # Server information leak
        if "Server" in response.headers:
            vulnerabilities.append(("Server Information Leak", "Low"))

        # Test SQL injection parameter
        test_url = url + "?id=1'"
        r = requests.get(test_url)

        if "sql" in r.text.lower():
            vulnerabilities.append(("Possible SQL Injection", "Critical"))

        # Test XSS
        test_xss = url + "?q=<script>alert(1)</script>"
        r2 = requests.get(test_xss)

        if "<script>" in r2.text:
            vulnerabilities.append(("Possible XSS", "High"))

    except:
        print("Target not reachable")

    return vulnerabilities


if __name__ == "__main__":

    target = input("Enter target URL: ")

    results = scan_website(target)

    print("\nScan Results:\n")

    for v in results:
        print(v[0], "-", v[1])