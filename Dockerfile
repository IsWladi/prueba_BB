FROM python:3.12.3-alpine3.20

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-v" ]
# docker build -t run-bb-tests .
# docker run -it --rm --name my-running-bb-tests run-bb-tests

