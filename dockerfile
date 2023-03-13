FROM python:3.9
 
WORKDIR /code

RUN pip install fastapi uvicorn

COPY api.py ./

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8081"]