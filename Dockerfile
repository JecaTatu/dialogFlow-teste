FROM python:3.6

LABEL maitainer="gas5@cin.ufpe.br"

RUN pip install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements /app/requirements

WORKDIR /app
RUN apt-get update
RUN apt-get install gdal-bin python-gdal python3-gdal -y
RUN apt-get install libgdal-dev -y
RUN pip install -r requirements/common.txt

COPY . /app