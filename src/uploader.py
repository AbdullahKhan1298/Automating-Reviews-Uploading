#!/usr/bin/env python3
import os
import requests
import argparse
from pathlib import Path
import json

DEFAULT_HOST = "http://127.0.0.1:5000"
DEFAULT_ENDPOINT = "/feedback/"

BASEPATH = "data/feedback/"

def read_feedback_files(basepath):
    feedback_list = []
    files = sorted([f for f in Path(basepath).iterdir() if f.is_file()])
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            title = f.readline().strip()
            name = f.readline().strip()
            date = f.readline().strip()
            feedback = f.read().strip()
        feedback_list.append({
            "title": title,
            "name": name,
            "date": date,
            "feedback": feedback,
            "source_file": file.name
        })
    return feedback_list

def upload_feedback(feedback_list, url, headers=None):
    headers = headers or {'Content-Type':'application/json'}
    for item in feedback_list:
        try:
            resp = requests.post(url, json=item, headers=headers, timeout=10)
            if resp.status_code in (200,201):
                try:
                    data = resp.json()
                    print(f"Created Feedback ID: {data.get('id')}")
                except Exception:
                    print("Posted successfully (no JSON id returned)")
            else:
                print(f"Failed to post {item['source_file']}: status={resp.status_code} text={resp.text}")
        except Exception as e:
            print(f"Error posting {item['source_file']}: {e}")


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Upload local review files to a reviews service.')
    p.add_argument('--host', default=DEFAULT_HOST, help='Host (include http://) e.g. http://127.0.0.1:5000')
    p.add_argument('--endpoint', default=DEFAULT_ENDPOINT, help='Endpoint path, default /feedback/')
    p.add_argument('--dry-run', action='store_true', help='Print payloads instead of posting')
    p.add_argument('--path', default=BASEPATH, help='Folder with review files')
    args = p.parse_args()

    url = args.host.rstrip('/') + '/' + args.endpoint.lstrip('/')
    reviews = read_feedback_files(args.path)
    print(f"Found {len(reviews)} files in {args.path}. Target URL: {url}")
    if args.dry_run:
        for r in reviews:
            print(json.dumps(r, ensure_ascii=False))
    else:
        upload_feedback(reviews, url)
