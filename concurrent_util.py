from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os
import asyncio
import aiohttp

def read_file(file_path) -> int:
    with open(file_path, 'r', encoding="utf-8", errors="replace") as file:
        return len(file.read())

def read_files_concurrently(file_paths) -> list[int]:
    with ThreadPoolExecutor() as executor:
        return list(executor.map(read_file, file_paths))


def read_files_with_process_pool(file_paths) -> list[int]:
    with ProcessPoolExecutor() as executor:
        return list(executor.map(read_file, file_paths))
    
def read_files_sequentially(file_paths) -> list[int]:
    return [read_file(fp) for fp in file_paths]
    

def get_files_in_directory(directory_path) -> list[str]:
    return [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def fetch_urls_concurrently(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for url, content in zip(urls, results):
            print(f"Fetched {len(content)} characters from {url}")

def fetch_url_sequential(url):
    import requests
    response = requests.get(url)
    return response.text

def fetch_urls_sequentially(urls):
    for url in urls:
        content = fetch_url_sequential(url)
        print(f"Fetched {len(content)} characters from {url}")

def main_compare(files_to_read):
    start = time.time()
    lengths = read_files_concurrently(files_to_read)
    print("File lengths:", lengths)
    print("Time taken:", time.time() - start)
    print("-" * 40)

    start = time.time()
    lengths = read_files_with_process_pool(files_to_read)
    print("File lengths with process pool:", lengths)
    print("Time taken with process pool:", time.time() - start)
    print("-" * 40)

    start = time.time()
    lengths = read_files_sequentially(files_to_read)
    print("File lengths with sequentially:", lengths)
    print("Time taken with sequentially:", time.time() - start)
    print("-" * 40)

    start = time.time()
    urls = ["https://mohisttech.com/en/dws/M600", "https://www.python.org", "https://www.github.com"]
    asyncio.run(fetch_urls_concurrently(urls))
    print("Time taken for async URL fetch:", time.time() - start)
    print("-" * 40)

    start = time.time()
    fetch_urls_sequentially(urls)
    print("Time taken for sequential URL fetch:", time.time() - start)
    print("-" * 40)