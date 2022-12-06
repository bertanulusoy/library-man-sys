FROM python:3.10

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app
EXPOSE 8000

ENTRYPOINT [ "python", "pipeline"]

#ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
# CMD python -m uvicorn main:app --host 127.0.0.1 --port 8000


