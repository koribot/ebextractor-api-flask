import requests
import concurrent.futures
import time


def send_request(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            status = f"Success (Status Code: {response.status_code})"
        else:
            status = f"Failure (Status Code: {response.status_code})"

        print(
            f"Request: {url}, Status: {status}, Time Taken: {elapsed_time:.2f} seconds")
    except Exception as e:
        print(
            f"Request: {url}, Status: Error - {str(e)}, Time Taken: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000/api/extract/using_keyword?q=shoes"

    # Number of concurrent requests
    num_requests = 20

    # Create a list of URLs for concurrent requests
    urls = [base_url for _ in range(num_requests)]

    # Send concurrent requests
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(send_request, urls)
