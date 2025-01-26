FROM rocm/pytorch:latest

RUN apt-get update && apt-get install -y \
    git wget python3 python3-pip && \
    pip3 install --upgrade pip

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY your_huggingface_key.txt .

RUN python3 -c "\
import os;\
from huggingface_hub import HfApi;\
with open('your_huggingface_key.txt', 'r') as f:\
    hf_token = f.read().strip();\
api = HfApi();\
api.set_access_token(hf_token);\
api.download_repo(repo_id='your_model_id', repo_type='model', revision='main', local_dir='/app/model');\
"

COPY app.py .

CMD ["python3", "app.py"]
