import requests
import pytest


@pytest.fixture(scope="session")
def base_url():
    return ' https://automationexercise.com/api'

def test_get(base_url):
    
    response = requests.get(
    
    base_url + '/productsList',
    
    )
    
    # чтобы извлечь что-то из response применяем json
    products = response.json()
    
    # получили словарь в котором все данные и достаём что-то конкретное
    print(products['products'][0]['id'])

    # проверяем что статус код 200
    assert response.status_code == 200
    
    # проверяем что количество товаров в products больше 0
    assert len(products) > 0 


def test_post(base_url):
    
    response = requests.post(
        
        base_url + '/productsList'
        # тоже самое но с ф строкой
        # f'{base_url}/productsList'
        
    )

    print(response.json())  
    
    # достаём данные из респонса
    message = response.json()
    
    # статус код достаём из message и сравниваем   
    assert message['responseCode'] == 405
    
    assert message['message'] == 'This request method is not supported.'
    

def test_search_products(base_url):
    
    
    
    body = {
        
        'search_product':'jean'
        
    }
    response = requests.post(
        
        base_url + '/searchProduct',
        data=body
         
    )
    
    print(response.json())
    assert response.status_code == 200 
    
    list = response.json()['products']
    
    for product in list :
        assert 'jean' in product['name'].lower()
        
        

def test_search_product_without_parameter(base_url):
    
    response = requests.post(
        
        base_url + '/searchProduct'
    )
    
    data = response.json()
    
    assert data['responseCode'] == 400
    
    assert data["message"] == "Bad request, search_product parameter is missing in POST request."
    
    
def test_login_valid(base_url):
    
    
    login = {
        
        'email' : 'mzatovka@gmail.com',
        'password': 'maksim'
        
    }
    
    response = requests.post(
        
        base_url + '/verifyLogin',
        data=login
        
    )
    
    message = response.json()
    
    assert message['message'] == "User exists!"
    assert response.status_code == 200
    
def test_login_invalid(base_url):
    
    
    login = {
        
        'email' : 'mzovka@gmail.com',
        'password': 'maksim'
        
    }
    
    
    response = requests.post(
        
        base_url + '/verifyLogin',
        data = login
        
    )
    
    message = response.json()
    
    assert message['message'] == 'User not found!'
    assert message['responseCode'] == 404


def test_create_user(base_url):
    
    info_about_user={
        
        'name':'max',
        'email':'maxzatoovka@gmail.com',
        'password':'maksim',
        'title ':'mr',
        'birth_date':'04',
        'birth_month':'06',
        'birth_year':'1996',
        'firstname':'maksim',
        'lastname':'zatouka',
        'company':'azot',
        'address1':'grodno',
        'address2':'grodno_sity',
        'country':'belarus',
        'zipcode':'230026',
        'state':'belarus',
        'city':'grodno',
        'mobile_number':'37533584956'
        
        
    }
    
    response = requests.post(
        
        base_url + '/createAccount',
        data= info_about_user
        
    )
    
    info =  response.json()
    assert info['responseCode'] == 201
    