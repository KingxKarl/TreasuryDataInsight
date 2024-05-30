import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from tenacity import retry, stop_after_attempt, wait_fixed
import pymongo
from datetime import datetime

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def fetch_initial_data(endpoint_details, start_date=None):
    url = f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service{endpoint_details['endpoint']}"
    params = endpoint_details['params']
    if start_date:
        params['filter'] = f"record_date:gte:{start_date}"

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data['data'], data['meta']

def fetch_page_data(url, params, page):
    params['page[number]'] = page
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['data']

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def fetch_data_with_pagination(endpoint_details, start_date=None):
    url = f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service{endpoint_details['endpoint']}"
    params = endpoint_details['params']
    if start_date:
        params['filter'] = f"record_date:gte:{start_date}"

    response = requests.get(url, params=params)
    response.raise_for_status()
    initial_data = response.json()
    all_data = initial_data['data']
    total_pages = initial_data['meta']['total-pages']

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_page = {executor.submit(fetch_page_data, url, params.copy(), page): page for page in range(2, total_pages + 1)}

        for future in tqdm(as_completed(future_to_page), total=total_pages - 1, desc='Fetching data', unit='page'):
            page_data = future.result()
            all_data.extend(page_data)

    return all_data

def get_most_recent_record_date(collection):
    most_recent_record = collection.find_one(sort=[("record_date", pymongo.DESCENDING)])
    if most_recent_record:
        most_recent_date = most_recent_record['record_date']
        if isinstance(most_recent_date, str):
            most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%dT%H:%M:%S.%f%z')
        return most_recent_date
    return None