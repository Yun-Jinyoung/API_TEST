import requests

if __name__ == '__main__':
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    response.text
    print(response.text)
    result = response.json()
    result['userId']

# 오늘은 Github 다른 소스 분석을 합니다. 내일 소스 업데이트 예정