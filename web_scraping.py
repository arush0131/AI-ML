# https://www.langchain.com/langgraph


# https://www.langchain.com/careers

# https://langchain-ai.github.io/langgraph/concepts/why-langgraph/


import threading
import requests

from bs4 import BeautifulSoup

urls=[
    'https://www.langchain.com/langgraph',
    'https://www.langchain.com/careers',
    'https://langchain-ai.github.io/langgraph/concepts/why-langgraph/'
]

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Title for  {len(soup.text)}")


threads=[]

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished execution.")