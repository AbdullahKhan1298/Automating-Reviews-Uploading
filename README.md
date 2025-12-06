# Reviews Uploader — Automating Reviews Posting to a REST API

**Objective**  
A small automation project that reads customer review text files from disk, normalizes them into JSON, and posts them to a running web service. The project was built to practice working with REST APIs, automating repetitive tasks, and visualizing the results via a simple HTML table for easy review.

**Why I built this**  
I wanted a compact, real-world exercise to practice REST API interactions and automation: instead of uploading reviews one-by-one, this script reads a folder of text files, converts their contents to structured JSON, and uploads them automatically. The project also includes a minimal web UI (an HTML table) to display the stored reviews.



## What’s included
- `src/uploader.py` — main uploader script (reads `data/feedback/`, posts JSON to the server)
- `mock_server.py` — lightweight Flask server for local testing (stores posted reviews in memory and serves an HTML view)
- `data/feedback/` — sample review `.txt` files (7 examples)
- `requirements.txt` — Python dependencies (`requests`, `flask`) for testing locally
- `demo/` — screenshots for documentation and portfolio use
- `.gitignore` — ignores virtual env and cache files


**Folder Structure**
<img width="321" height="565" alt="folder_structure" src="https://github.com/user-attachments/assets/375c03a0-a63f-44b3-92e9-14cce96ec76c" />


**Getting Requests from Server**
<img width="1544" height="983" alt="getting-server-requests" src="https://github.com/user-attachments/assets/54577b4c-38ec-4cfe-9e1d-7e208ce8d3f9" />

**Output**
<img width="1914" height="631" alt="feedback_webpage" src="https://github.com/user-attachments/assets/9466e7c7-766d-49d1-afad-1819988fb1e5" />



