#  Subdomain Collector with MongoDB & Subfinder
```
 _____       _     _   _                       _ 
/  ___|     | |   | | | |                     | |
\ `--. _   _| |__ | |_| | ___  _   _ _ __   __| |
 `--. \ | | | '_ \|  _  |/ _ \| | | | '_ \ / _` |
/\__/ / |_| | |_) | | | | (_) | |_| | | | | (_| |
\____/ \__,_|_.__/\_| |_/\___/ \__,_|_| |_|\__,_|
```
This Python script collects subdomains for a given list of domains using [Subfinder](https://github.com/projectdiscovery/subfinder) and stores the results in a MongoDB database. It avoids duplicates, keeps a timestamp for each entry, and automates subdomain enumeration for scope-based domain lists.

---


## 📌 Features

- Uses `subfinder` to enumerate subdomains
- Prevents duplicate entries using MongoDB queries
- Stores subdomains with a timestamp
- Automatically loads a list of domains from a MongoDB `Scope` collection

---

## ⚙️ Requirements

Make sure you have the following installed:

- Python 3.6+
- MongoDB (running locally or remotely)
- [Subfinder](https://github.com/projectdiscovery/subfinder) (must be available in your system PATH)
- Python dependencies:

```bash
pip install pymongo
