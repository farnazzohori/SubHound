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
```
#🛠️ How It Works
Connects to MongoDB at mongodb://localhost:27017/

Reads a list of domains from the Scope collection in the Sh4z0 database

Runs subfinder on each domain to discover subdomains

For each discovered subdomain:

Strips empty lines and whitespace

Checks if it's already in the Domian collection

If not, inserts it with a timestamp
##Example MongoDB Structure
Database: Sh4z0
Collection: Scope
```
{
  "Domian": "example.com"
}
Collection: Domian
}
```

```
{
  "domian": "sub.example.com",
  "timestamp": "2025-08-07 12:34:56"
}
```
