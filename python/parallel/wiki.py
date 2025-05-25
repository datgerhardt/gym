import time
import requests
import concurrent.futures

def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknow"
    if response.status_code == 200:
        page_status = "exist"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status 

# wiki_pages_urls = [
#    "https://en.wikipedia.org/wiki/Ocean",
#    "https://en.wikipedia.org/wiki/Island",
#    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
#    "https://en.wikipedia.org/wiki/Shark",
#]

wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]

print("Running with threads:")
with_threads_start = time.time()
#
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(
            executor.submit(
                get_wiki_page_existence, wiki_page_url=url, 
            )
        )
    for future in concurrent.futures.as_completed(futures):
        try:
           print(future.result()) 
        except requests.ConnectTimeout:
            print("Connection Timeout")
print("With threads time:", time.time() - with_threads_start)


#wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]

#print("Running without threads:")
#without_threads_start = time.time()
#for url in wiki_page_urls:
#    print(get_wiki_page_existence(wiki_page_url=url))
#print("Without threads time:", time.time() - without_threads_start)

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Ocean"
#    print(get_wiki_page_existence(wiki_page_url=url))
