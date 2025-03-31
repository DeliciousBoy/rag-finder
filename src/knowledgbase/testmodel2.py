# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-4-mini-instruct", trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-4-mini-instruct", trust_remote_code=True)

import torch
import time
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

model_path = "microsoft/Phi-4-mini-instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    trust_remote_code=True,
)
model.to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_path)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"},
    {"role": "assistant", "content": "Sure! Here are some ways to eat bananas and dragonfruits together: 1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits together with some milk and honey. 2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits together with some lemon juice and honey."},
    {"role": "user", "content": "What about solving an 2x + 3 = 7 equation?"},
]

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.0,
    "do_sample": False,
}

# หากใช้งาน GPU ให้เรียก synchronize เพื่อรอให้ทุกงานเสร็จสิ้น
if torch.cuda.is_available():
    torch.cuda.synchronize()

# เริ่มจับเวลา
start_time = time.time()

output = pipe(messages, **generation_args)

# ถ้าใช้งาน GPU ควรซิงโครไนซ์เพื่อรอให้ทุกอย่างประมวลผลเสร็จ
if torch.cuda.is_available():
    torch.cuda.synchronize()

end_time = time.time()
execution_time = end_time - start_time

print(output[0]['generated_text'])
print(f"Execution time: {execution_time:.2f} seconds")

