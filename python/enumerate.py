# import sys
# import subprocess
# import json
# import requests
# import os
# import re

# def main():
#     if len(sys.argv) != 2:
#         print(json.dumps({"error": "Usage: enumerate.py <domain>"}))
#         return

#     domain = sys.argv[1]
#     output_file = "output.txt"

#     try:
#         subprocess.run(
#             ["C:\\amass\\amass.exe", "enum", "-passive", "-d", domain, "-o", output_file, "-timeout", "20"],
#             check=True,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True,
            
#         )
#     except subprocess.CalledProcessError as e:
#         print(json.dumps({"error": e.stderr}))
#         return

#     if not os.path.exists(output_file):
#         print(json.dumps({"error": "Output file not generated."}))
#         return

#     subdomains = set()

#     with open(output_file, "r") as f:
#         for line in f:
#             match = re.match(r'^([a-zA-Z0-9.-]+)\s+\(FQDN\)', line)
#             if match:
#                 fqdn = match.group(1)
#                 if fqdn.endswith("." + domain) or fqdn == domain:
#                     subdomains.add(fqdn)

#     # Optional: Check which ones are live via HTTPS
#     active = []
#     for sub in subdomains:
#         try:
#             r = requests.head(f"https://{sub}", timeout=3, allow_redirects=True)
#             if r.status_code < 400:
#                 active.append(sub)
#         except:
#             pass

#     print(json.dumps({
#         "domain": domain,
#         "active_subdomains": active
#     }))

# if __name__ == "__main__":
#     main()



import sys
import subprocess
import json
import requests
import os
import re

def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: enumerate.py <domain>"}))
        return

    domain = sys.argv[1]
    output_file = "output.txt"

    try:
        subprocess.run(
            ["C:\\amass\\amass.exe", "enum", "-passive", "-d", domain, "-o", output_file, "-timeout", "20"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(json.dumps({"error": e.stderr}))
        return

    if not os.path.exists(output_file):
        print(json.dumps({"error": "Output file not generated."}))
        return

    subdomains = set()
    with open(output_file, "r") as f:
        for line in f:
            match = re.match(r'^([a-zA-Z0-9.-]+)\s+\(FQDN\)', line)
            if match:
                fqdn = match.group(1)
                if fqdn.endswith("." + domain) or fqdn == domain:
                    subdomains.add(fqdn)

    active = []
    for sub in subdomains:
        try:
            r = requests.head(f"https://{sub}", timeout=3, allow_redirects=True)
            if r.status_code < 400:
                active.append(sub)
        except:
            pass

    # Simple findings
    interesting = [s for s in active if 'test' in s or 'dev' in s or 'beta' in s]
    risks = [s for s in active if 'admin' in s or 'internal' in s or 'private' in s]

    print(json.dumps({
        "domain": domain,
        "total_subdomains_found": len(subdomains),
        "active_subdomains_count": len(active),
        "active_subdomains": active,
        "interesting_subdomains": interesting,
        "potential_risks": risks,
        "summary": f"Found {len(subdomains)} subdomains, of which {len(active)} are active."
    }))
    
if __name__ == "__main__":
    main()
