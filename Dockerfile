FROM python:3.6

LABEL maitainer="gas5@cin.ufpe.br"

RUN pip install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements /app/requirements

WORKDIR /app

RUN pip install -r requirements/common.txt

COPY . /app