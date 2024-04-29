FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	&& apt-get install -y git build-essential pkg-config python3-dev default-libmysqlclient-dev libxslt-dev \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces/projeto-integrador-III/

RUN git config --global pull.rebase false
RUN git config --global pull.ff only

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 

EXPOSE 8000