# Nmap XML to Markdown Parser

This project includes a Python script that parses an Nmap XML output file and formats the data as a markdown file with tables.

## Dependencies

This script depends on the Python `tabulate` library. Install it using pip:

```bash
pip install -r requirements.txt
```

# Usage

After installing the dependencies, you can run the script with:
```
python script.py <path_to_your_nmap.xml>
Replace <path_to_your_nmap.xml> with the path to your Nmap XML file.
```

The script will print the markdown formatted output to the console. If you want to save this output to a markdown file, you can redirect the output like so:

```
python script.py <path_to_your_nmap.xml> > output.md
```

This will create a markdown file named output.md with the results.

# Output Format

For each host in the Nmap XML file, the script will generate a markdown section like the following:

bash

```
## 172.27.4.28

| Port     | Service                                           |
|----------|---------------------------------------------------|
| 22/tcp   | ssh OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) |
| 111/tcp  | rpcbind 2-4 (RPC #100000)                         |
| 9100/tcp | jetdirect?                                        |
```

# Limitations

This script assumes that every port in the Nmap XML file has a 'service' child with 'name', 'product', 'version', and 'extrainfo' attributes. If this is not the case, you may need to adjust the script to fit your exact XML structure.



> It also works with -iL and list of hosts passed to nmap 

Generates results like this 

```
## 172.27.0.222

| Port | Service |
|------|---------|
| 22/tcp | ssh OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) |
| 111/tcp | rpcbind 2-4 (RPC #100000) |
| 179/tcp | tcpwrapped |
| 9100/tcp | jetdirect? |
```
