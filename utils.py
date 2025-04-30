# utils.py
import json

def save_request_to_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_request_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_example_request():
    return {
        "url": "https://httpbin.org/post",
        "method": "POST",
        "headers": '{\n  "Content-Type": "application/json"\n}',
        "body": '{\n  "name": "Tester",\n  "message": "Hello from PyQt6!"\n}'
    }

def get_example_by_method(method: str) -> dict:
    examples = {
        "GET": {
            "url": "https://jsonplaceholder.typicode.com/posts/1",
            "method": "GET",
            "headers": "",
            "body": ""
        },
        "POST": {
            "url": "https://httpbin.org/post",
            "method": "POST",
            "headers": '{\n  "Content-Type": "application/json"\n}',
            "body": '{\n  "username": "tester",\n  "email": "test@example.com"\n}'
        },
        "PUT": {
            "url": "https://httpbin.org/put",
            "method": "PUT",
            "headers": '{\n  "Content-Type": "application/json"\n}',
            "body": '{\n  "status": "active"\n}'
        },
        "DELETE": {
            "url": "https://httpbin.org/delete",
            "method": "DELETE",
            "headers": '{\n  "Authorization": "Bearer token123"\n}',
            "body": ""
        }
    }
    return examples.get(method.upper(), get_example_request())
