FROM python:3

WORKDIR /app

#COPY requirements.txt ./
ADD requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "./server.py", "--port", "8000" ]