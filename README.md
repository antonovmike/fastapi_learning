# fastapi_learning
Learning FastAPI

Path parameter

Browser sends the request to http://127.0.0.1:8000/users/315, i.e. the request path in this case is users/315. The FastAPI framework sees that this path corresponds to the "/users/{id}" pattern, so this request will be handled by the users function.

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

START:
```bash
uvicorn main:app --reload
```
Open

http://127.0.0.1:8000/users/Your_Name/Your_Age

http://127.0.0.1:8000/users_2/12345678912