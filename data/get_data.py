import json
import requests
import os

folder_name = "my_repo"
txt_file = "my_repo"

with open("../api_key.txt") as file:
    text = file.read()
    api_key = text.split(" ")[-1]

def fetch_data(stock_name, api_key=api_key, output_size='full'):
    # download data
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&outputsize={output_size}&apikey={api_key}&datatype=json'
    r = requests.get(url)
    data = r.json()

    # save data
    with open(f'./{folder_name}/{stock_name}.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    print("Get Data")

    with open(f'./{txt_file}.txt', 'r') as file:
        stock_list = [line.strip() for line in file.readlines()]
    print(f"Open {txt_file}.txt")

    # only 25 api requests per day
    counter = 0
    for stock in stock_list:
        if not os.path.exists(f'./{folder_name}/{stock}.json'):
            if counter < 25:
                print(f'get {folder_name}/{stock}.json')
                fetch_data(stock)
                counter+=1
            else:
                print(f'API limit reached')
                break
