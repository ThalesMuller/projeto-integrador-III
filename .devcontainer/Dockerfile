FROM python:3.10-slim

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	&& apt-get install -y git \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN git config --global pull.rebase false
RUN git config --global pull.ff only

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]