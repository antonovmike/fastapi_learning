# fastapi_learning
Learning FastAPI

Response

The fastapi.Response class is the base class for all the response classes. Its advantage is that it also allows you to send a response that is not covered by the built-in classes. The class constructor takes the following parameters to define the response:

- content: specifies the content to be sent
- status_code: sets the status code of the response
- media_type: specifies the MIME type of the response
- headers: sets the response headers

The **HTMLResponse** class is designed to simplify sending html code. It sets the Content-Type header to text/html:

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

START:
```bash
uvicorn main:app --reload
```
Open

http://127.0.0.1:8000/

http://127.0.0.1:8000/about

http://127.0.0.1:8000/documentation