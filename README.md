# fastapi_learning
Learning FastAPI

Query string parameters: 
parameters_name=parameters_value

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

START:
```bash
uvicorn main:app --reload
```
Open

http://127.0.0.1:8000/users?name=mike&age=39