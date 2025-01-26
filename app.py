from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def create_prompt(user_input):
    return f"<s>[INST] {user_input} [/INST]"

def initialize_model():
    model_name = "/app/Mistral-7B-Instruct-v0.3"
    print("Loading the model...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        return model, tokenizer
    except RuntimeError as e:
        print(f"GPU Error: {e}")
        return None, None
    except OSError as e:
        print(f"Model loading error: {e}")
        return None, None

def generate_response(model, tokenizer, prompt, max_length=512):
    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(
            inputs["input_ids"],
            max_new_tokens=max_length,
            temperature=0.7,
            top_p=0.95,
            do_sample=True
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.split("[/INST]")[-1].strip()
    except Exception as e:
        return f"Error generating response: {e}"

def chatbot():
    print("Initializing chatbot...")
    model, tokenizer = initialize_model()

    if not model or not tokenizer:
        print("Failed to initialize model. Exiting...")
        return

    try:
        print("\nWelcome to the Mistral-7B chatbot!")
        print("Type 'exit' to quit or press CTRL+C")
        print("-" * 50)

        while True:
            try:
                user_input = input("\nYou: ").strip()
                if user_input.lower() == "exit":
                    print("\nGoodbye!")
                    break

                if not user_input:
                    print("Please enter a message.")
                    continue

                prompt = create_prompt(user_input)
                response = generate_response(model, tokenizer, prompt)
                print(f"\nMistral-7B: {response}")

            except KeyboardInterrupt:
                print("\n\nReceived interrupt signal. Shutting down...")
                break
            except Exception as e:
                print(f"\nError during chat: {e}")
                break

    finally:
        print("\nCleaning up resources...")
        if model:
            try:
                del model
                torch.cuda.empty_cache()
                print("GPU memory cleared")
            except Exception as e:
                print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    chatbot()
