from app import *
import pytest
import requests

docs = [
    ('876234', 'passport','Петя Петров', '3'),
    ('33213', 'passport','Коля Иванов', '2')
]

@pytest.mark.parametrize('doc, result', [('11-2', True), ('2207 876234', True), ("123", False)])
def test_check_document_existance(doc, result):
    assert check_document_existance(doc) == result

@pytest.mark.parametrize('doc, owner', [('11-2', 'Геннадий Покемонов'), ('2207 876234', 'Василий Гупкин'), ("123", None)])
def test_get_doc_owner_name(doc, owner):
    assert get_doc_owner_name(doc) == owner


@pytest.mark.parametrize('doc, shelf', [('11-2', '1'), ('2207 876234', '1'), ("123", None)])
def test_get_doc_shelf(doc, shelf):
    assert get_doc_shelf(doc) == shelf

def test_remove_doc_from_shelf():
    check_user_doc = get_doc_shelf('11-2')
    assert check_user_doc == '1'
    remove_doc_from_shelf('11-2')
    check_user_doc2 = get_doc_shelf('11-2')
    assert check_user_doc2 == None

@pytest.mark.parametrize('number, type, name, shelf',docs)
def test_add_new_doc(number, type, name, shelf):
    add_new_doc(number, type, name, shelf)
    assert check_document_existance(number) == True
    assert get_doc_shelf(number) == shelf
    delete_doc(number)

@pytest.mark.parametrize('folder_name', ['111', '222', '333'])
def test_create_folder_ya(folder_name):
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'OAuth ..........'}
    url = 'https://cloud-api.yandex.net/v1/disk/resources/?path=' + folder_name
    res = requests.put(url, headers=headers)
    assert res.status_code == 201
    res = requests.get(url, headers=headers)
    assert res.status_code == 200
    res = requests.delete(url, headers=headers)


