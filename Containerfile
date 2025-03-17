FROM python:3.13

WORKDIR /testing-template

COPY . /testing-template

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "pytest --env=dev"]