# ShoDork
ShoDork is a command-line tool for searching Shodan using a list of dorks and saving the resulting IP addresses to a file.

# Requirements

- Python 3.x
- Shodan API key (get it [here](https://account.shodan.io/register))

# Installation

Clone the repository: `git clone https://github.com/helloyourld/ShoDork.git`

Navigate to the project directory: `cd ShoDork`

Install the dependencies: `pip3 install -r requirements.txt`

# Usage

To look up single dork, run: `python3 shodork.py -q <single-dork>`

To look up a list of dorks from a file, run: `python3 shodork.py -f <filename>`

**Note: File must a text file containing a list of dorks (one per line).**

ShoDork will output the results to a file named ips.txt.

Example

`python3 shodork.py -q port:80`

`python3 shodork.py -f dorks.txt`

# Acknowledgments

Shodan for providing the API used in this tool.

Feel free to modify and distribute this tool as you wish. If you find any bugs or have suggestions for improvement, please create an issue on this repository.
