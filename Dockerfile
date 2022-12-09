FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app
EXPOSE 8000

#ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
#CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000

# ENTRYPOINT [ "bash"]


