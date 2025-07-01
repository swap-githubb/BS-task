# 🕵️ Passive Subdomain Reconnaissance Tool

This project automates **passive reconnaissance** of a target domain using [OWASP Amass](https://github.com/owasp-amass/amass). It performs subdomain enumeration, validates active subdomains, and returns a structured report using a **Python script** and an **Express.js API**.

---

## 🚀 Features

- 🔍 Passive subdomain enumeration with Amass
- 🌐 Detection of live subdomains via HTTPS
- 🧠 Identification of interesting subdomains
- 🧾 Summary report with total, active, and risky subdomains
- 📡 REST API for automated domain scanning

---

## 📁 Project Structure

```text
recon-project/
├── python/
│ └── enumerate.py # Python script to run Amass and process results
├── node/
│ └── server.js # Express.js API server to trigger the Python script
├── output.txt # Generated temp output by Amass
└── README.md # Documentation file (this file)
```


---

## 🧰 Prerequisites

- **Windows OS**
- **Python 3.8+**
- **Node.js 18+**
- **Amass installed** (`amass.exe` path set properly)

---

## ⚙️ Setup Instructions

### 1. Download & Install Amass

- Download Amass binary for Windows from:  
  https://github.com/owasp/amass/releases  
- Extract and place `amass.exe` inside: C:\amass\amass.exe

Make sure this is the correct path in your script.

---

### 2. Python Setup

```bash
pip install requests
```

### 3. Node.js Setup
- Navigate to the node/ directory:

```bash
npm init -y
npm install express
```

---

### ▶️ How to Run
#### ✅ Use Express API Server

- Start the server:
```bash
cd node/
node server.js
```
- Then visit this URL in your browser: http://localhost:8000/enum/iana.org (I have tested on this url)

### 📊 Sample JSON Output

- This was the output obtained:
```json
{
  "domain": "iana.org",
  "total_subdomains_found": 46,
  "active_subdomains_count": 16,
  "active_subdomains": [
    "rzm-ote.iana.org",
    "beta.iana.org",
    "feedback.iana.org",
    "pen.iana.org",
    "lists.iana.org",
    "rzm.iana.org",
    "data.iana.org",
    "rsync.iana.org",
    "www.iana.org",
    "recursive.iana.org",
    "sle-dashboard.iana.org",
    "handbook.int.iana.org",
    "rs.iana.org",
    "iana.org",
    "ftp.iana.org",
    "res-dom.iana.org"
  ],
  "interesting_subdomains": [
    "beta.iana.org"
  ],
  "potential_risks": [],
  "summary": "Found 46 subdomains, of which 16 are active."
}
```

---

### 🧠 What Is Considered “Interesting”?
- Subdomains like:
beta.iana.org

- May indicate internal, staging, or debug interfaces
- These may pose risks if unintentionally exposed.




