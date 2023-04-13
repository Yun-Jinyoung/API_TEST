import requests

if __name__ == '__main__':
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    response.text
    print(response.text)
    result = response.json()
    result['userId']
