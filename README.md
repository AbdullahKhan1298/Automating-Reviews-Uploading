# Reviews Uploader — Automating Reviews Posting to a REST API

**Objective**  
A small automation project that reads customer review text files from disk, normalizes them into JSON, and posts them to a running web service. The project was built to practice working with REST APIs, automating repetitive tasks, and visualizing the results via a simple HTML table for easy review.

**Why I built this**  
I wanted a compact, real-world exercise to practice REST API interactions and automation: instead of uploading reviews one-by-one, this script reads a folder of text files, converts their contents to structured JSON, and uploads them automatically. The project also includes a minimal web UI (an HTML table) to display the stored reviews.

---

## What’s included
- `src/uploader.py` — main uploader script (reads `data/feedback/`, posts JSON to the server)
- `mock_server.py` — lightweight Flask server for local testing (stores posted reviews in memory and serves an HTML view)
- `data/feedback/` — sample review `.txt` files (7 examples)
- `requirements.txt` — Python dependencies (`requests`, `flask`) for testing locally
- `demo/` — screenshots for documentation and portfolio use
- `.gitignore` — ignores virtual env and cache files

