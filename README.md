# Mistral 7B AMD Chatbot with Docker

This repository hosts a high-performance chatbot built on the open-source Mistral-7B model, optimized for local deployment in a Docker container. Designed to leverage the power of an AMD GPU.

## Step 1: Prerequisites

### Hardware
- An AMD GPU with ROCm support for GPU computations.

### Software
- **Docker**: Ensure Docker is installed on your machine.
- **ROCm**: Properly configure ROCm to use your GPU with Docker. You can follow the [tuto here](https://github.com/mpeyre-s/Mistral7B-AMDChat/blob/main/rocom_installation.md). You can verify your installation by running:
  ```bash
  /opt/rocm/bin/rocminfo
  ```

## Step 2: Clone the Project
Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/mpeyre-s/Mistral7B-AMDChat.git
cd Mistral7B-AMDChat
```

## Step 3: Get and set your Hugging Face API KEY
Get your access token from your Hugging Face account and paste it into
``` your_huggingface_key.txt ```

## Step 3: Build the Docker Image
Build the Docker image using the provided Dockerfile:
```bash
docker build -t mistral-chatbot .
```

## Step 4: Run the Docker Container
Run the container, attaching the GPU to enable computations:
```bash
docker run --rm --gpus all -it mistral-chatbot
```

## Step 5: Interact with the Chatbot
Once the container is running, you can interact with the chatbot directly in the console. Type your queries, and the chatbot will respond.

---

### Notes
- Ensure your system meets the hardware and software requirements before proceeding.
- If you encounter any issues, verify your ROCm setup and Docker GPU configuration.
- For additional help, refer to the [ROCm Documentation](https://rocm.docs.amd.com/) or the Docker [GPU support guide](https://docs.docker.com/config/containers/resource_constraints/#gpu).

---

### Acknowledgements
Special thanks to the Mistral team and their CEO for continuing to make everything open source.

