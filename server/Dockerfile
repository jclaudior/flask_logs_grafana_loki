FROM python:3.10
COPY . /server
WORKDIR /server

EXPOSE 7007

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt