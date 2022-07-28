FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
ADD app.py /app
RUN pip3 install -r requirements.txt --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
COPY / .
CMD ["python3", "./app.py"]




