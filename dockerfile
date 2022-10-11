FROM python:3.10-alpine
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ['/bin/bash']