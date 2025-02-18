# Reddit API Advanced

## Description
This project consists of Python scripts that interact with the Reddit API to retrieve data about subreddits. The tasks involve querying Reddit to obtain subscriber counts, top hot posts, and recursively fetching all hot articles. Additionally, a script parses post titles to count keyword occurrences.

## General Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all Python files should be exactly `#!/usr/bin/python3`
- Libraries must be imported in alphabetical order
- A `README.md` file at the root of the project directory is mandatory
- Code must follow PEP 8 style guidelines
- All files must be executable
- File length will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- The `requests` module must be used for sending HTTP requests to the Reddit API
- Ensure compliance with Reddit API rate limits and set a proper User-Agent

## Tasks
### 0. How many subs?
**File:** `0-subs.py`
- Function: `def number_of_subscribers(subreddit)`
- Queries the Reddit API to return the number of total subscribers for a given subreddit.
- Returns `0` if the subreddit is invalid.

### 1. Top Ten
**File:** `1-top_ten.py`
- Function: `def top_ten(subreddit)`
- Prints the titles of the first 10 hot posts of a subreddit.
- Prints `None` if the subreddit is invalid.

### 2. Recurse it!
**File:** `2-recurse.py`
- Function: `def recurse(subreddit, hot_list=[])`
- Recursively retrieves all hot article titles of a subreddit.
- Returns `None` if the subreddit is invalid.

### 3. Count it!
**File:** `3-count.py`
- Function: `def count_words(subreddit, word_list)`
- Recursively parses the titles of all hot articles and counts occurrences of given keywords (case-insensitive).
- Results are sorted in descending order by count, with ties broken alphabetically.
- Prints nothing if no matches are found or if the subreddit is invalid.

## Repository Structure
```
alu-scripting/
    ├── api_advanced/
    │   ├── 0-subs.py
    │   ├── 1-top_ten.py
    │   ├── 2-recurse.py
    │   ├── 3-count.py
    │   ├── 0-main.py
    │   ├── 1-main.py
    │   ├── 2-main.py
    │   ├── 3-main.py
    │   ├── README.md
```

## Usage
Run the main files with a subreddit name as an argument:
```
python3 0-main.py programming
python3 1-main.py programming
python3 2-main.py programming
python3 3-main.py programming 'python java javascript'
```


