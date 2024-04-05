FROM python:3.10-slim

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	&& apt-get install -y git \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces/projeto-integrador-III/

RUN git config --global pull.rebase false
RUN git config --global pull.ff only

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 

# RUN python margm/manage.py migrate

EXPOSE 8000
CMD ["python", "margm/manage.py", "runserver", "0.0.0.0:8000"]
