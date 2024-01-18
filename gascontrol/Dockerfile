FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install  -r requirements.txt

EXPOSE 9000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]


# docker run -p 9000:9000 --privileged -v /dev/gpiomem:/dev/gpiomem -d gascontrol
# docker build -t gascontrol .
