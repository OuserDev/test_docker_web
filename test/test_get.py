import requests

# GET request가 잘 되는가?를 테스트
def test_get():
    url = 'http://localhost:8080/task'
    response = requests.get(url)
    
    assert response.status_code == 204

# - python의 requests 모듈을 사용하여 웹 서버의 task 페이지를 `GET` 요청하였음
# - 웹 서버에 따르면, GET 요청을 수신하여 task 데이터베이스에 있는 모든 task를 조회하여 반환함
# - 데이터베이스를 초기화하였으므로 서버는 204 Non Content 코드를 반환해야 함
# - assert문으로 반환된 코드가 204와 일치하는지 테스트하였음
# - 204가 맞다면 PASS, 그렇지 않다면 FAIL이 출력됨