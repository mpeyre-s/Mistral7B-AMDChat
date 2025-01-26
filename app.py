from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "mistral-7b-instruct"
print("Loading the model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Model loaded with success!")

def chatbot():
    print("Welcome to the chatbot! Press 'exit' to exit.")
    while True:
        user_input = input("You : ")
        if user_input.lower() == "exit":
            print("See you soon!")
            break
        inputs = tokenizer(user_input, return_tensors="pt").to("cuda")
        outputs = model.generate(inputs["input_ids"], max_new_tokens=50)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Mistral7B : {response}")

if __name__ == "__main__":
    chatbot()
