import os
import json
import subprocess
import requests

# Header
print(f"---")
print(f"layout: archive")
print(f"permalink: /blog/")
print(f"title: \"Blog Posts\"")
print(f"author_profile: true")
print(f"redirect_from:")
print(f"---")
print()
print(f"{{% include base_path %}}")
print()

# Essays
print(f"<h2>Essays</h2>")
print(f"<ol>")
print(f"<li><a href='../pages/Games and Computational Complexity 0d8fa9beb82948efb8aa325720525ddd.html' target='_blank'><span class='centered'>Games and Computational Complexity</a></li>")
print(f"<li><a href='../files/Ten_Commandments.pdf' target='_blank'><span class='centered'>Ten Commandments: Impossible Operations in Quantum Mechanics</a></li>")
print(f"<li><a href='../files/PIR_Intro.pdf' target='_blank'><span class='centered'>Introductory Survery for Quantum Private Information Retrieval</a></li>")
print(f"<li><a href='../files/Query_Complexity.pdf' target='_blank'><span class='centered'>Query Complexity</a></li>")
print(f"<li><a href='../files/Entanglement_and_non_Markovianity_of_Quantum_Evolutions.pdf' target='_blank'><span class='centered'>Entanglement and Quantum non-Markovianity</a></li>")
print(f"</ol>")
print()

def extract_time(json):
    try:
        return (json['created_time'])
    except KeyError:
        return 0

def get_data(url):
    payload = {"page_size": 100}
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer secret_F5x49bLQ1bDLgN9EhihvNJrx8WsKoGo4DR9cKcD6vJG"
    }

    data = requests.request("POST", url, json=payload, headers=headers)
    data = data.json()
    data = data["results"]

    data.sort(key=extract_time)
    return data


# Mathematics
print(f"<h2>Mathematics</h2>")
print(f"<ol>")
data = get_data(
    "https://api.notion.com/v1/databases/fde4d184234e4374a15402e48d9c41ce/query")
for i in data:
    url = i["url"].replace("www.notion.so", "banrovegrie.notion.site")
    name = i["properties"]["Name"]["title"][0]["plain_text"]
    print(f"<li><a href={url} target='_blank' target='_blank'><span class='centered'>{name}</a></li>")
print(f"</ol>")
print()

# Computation and Information
print(f"<h2>Computation and Information</h2>")
print(f"<ol>")
data = get_data(
    "https://api.notion.com/v1/databases/a2456a6ca26c492c9bda36ea66bf8153/query")
for i in data:
    url = i["url"].replace("www.notion.so", "banrovegrie.notion.site")
    name = i["properties"]["Name"]["title"][0]["plain_text"]
    print(f"<li><a href={url} target='_blank'><span class='centered'>{name}</a></li>")
print(f"</ol>")
print()

# Algorithms and Machine Learning
print(f"<h2>Algorithms and Machine Learning</h2>")
print(f"<ol>")
data = get_data(
    "https://api.notion.com/v1/databases/1105bec026cb4f6a950d785d42efebef/query")
for i in data:
    url = i["url"].replace("www.notion.so", "banrovegrie.notion.site")
    name = i["properties"]["Name"]["title"][0]["plain_text"]
    print(f"<li><a href={url} target='_blank'><span class='centered'>{name}</a></li>")
print(f"</ol>")
print()

# Systems
print(f"<h2>Systems</h2>")
print(f"<ol>")
data = get_data(
    "https://api.notion.com/v1/databases/a7e66f76f8a144c58017f37955029288/query")
for i in data:
    url = i["url"].replace("www.notion.so", "banrovegrie.notion.site")
    name = i["properties"]["Name"]["title"][0]["plain_text"]
    print(f"<li><a href={url} target='_blank'><span class='centered'>{name}</a></li>")
print(f"</ol>")
print()

print(f"<br>")
print(f"<p> Also, here is <a href='/random' target='_blank'>link</a> to some random shit. </p>")