
import torch
import time
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

model_path = "microsoft/Phi-4-mini-instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    trust_remote_code=True,
)
model.to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_path)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)
generation_args = {
    "max_new_tokens": 200,
    "return_full_text": False,
    "temperature": 0.0,
    "do_sample": False,
}

# หากใช้งาน GPU ให้เรียก synchronize เพื่อรอให้ทุกงานเสร็จสิ้น
if torch.cuda.is_available():
    torch.cuda.synchronize()

def text_generation(prompt):
    messages = [
    {"role": "system", "content": """ยินดีต้อนรับสู่ห้องสมุดแห่งความลับของนิวท์ สคามันเดอร์!
ข้าคือ ศาสตราจารย์ผู้เชี่ยวชาญด้านสัตว์มหัศจรรย์แห่งโลกเวทมนตร์ นักสำรวจสายเลือดมักมายผู้ตามรอยการเดินทางของนิวท์ สคามันเดอร์ และเป็นผู้
เขียนร่วมในฉบับปรับปรุงของตำราสัตว์มหัศจรรย์และถิ่นที่อยู่! """},
    {"role": "user", "content": f"{prompt}"},
]
# เริ่มจับเวลา
    start_time = time.time()

    output = pipe(messages, **generation_args)

    end_time = time.time()
    execution_time = end_time - start_time

    print(output[0]['generated_text'])
    print(f"Execution time: {execution_time:.2f} seconds")
    return output[0]['generated_text']


