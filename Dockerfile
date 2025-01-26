FROM rocm/pytorch:latest

RUN apt-get update && apt-get install -y \
    git wget python3 python3-pip && \
    pip3 install --upgrade pip

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["python3", "app.py"]
