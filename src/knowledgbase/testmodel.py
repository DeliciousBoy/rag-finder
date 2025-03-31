# Use a pipeline as a high-level helper
# from transformers import pipeline

# messages = [
#     {"role": "user", "content": "1+1 ได้เท่าไร"},
# ]
# pipe = pipeline("text-generation", model="microsoft/Phi-4-mini-instruct", trust_remote_code=True)
# print(messages)
# print(pipe(messages))
# print(messages)

# import tensorflow as tf
# print(tf.config.list_physical_devices('GPU'))

# import os
# print(os.environ.get("CUDA_VISIBLE_DEVICES"))
# import torch

# print(torch.cuda.is_available())
import torch

if torch.cuda.is_available():
    # จำนวน GPU
    num_gpus = torch.cuda.device_count()
    print(f"จำนวน GPU ทั้งหมดในเครื่อง: {num_gpus}")
    
    # วนลูปแสดงข้อมูลของทุก GPU
    for i in range(num_gpus):
        device_name = torch.cuda.get_device_name(i)
        capability = torch.cuda.get_device_capability(i)
        props = torch.cuda.get_device_properties(i)
        
        print(f"\nGPU #{i}:")
        print(f"  ชื่ออุปกรณ์ (device name): {device_name}")
        print(f"  Capability: {capability}")
        print(f"  หน่วยความจำ (Bytes): {props.total_memory}")
        
        # ตัวอย่างการเช็คหน่วยความจำที่ใช้ไปแล้ว (allocated) และหน่วยความจำที่จองไว้ (reserved)
        # ทั้งนี้ต้องใช้บน GPU device ที่เรากำหนด active ก่อน
        torch.cuda.set_device(i)
        allocated = torch.cuda.memory_allocated(i)
        reserved = torch.cuda.memory_reserved(i)
        print(f"  หน่วยความจำที่ใช้ไปแล้ว (allocated): {allocated}")
        print(f"  หน่วยความจำที่จองไว้ (reserved): {reserved}")
else:
    print("ไม่พบ GPU หรือไม่สามารถใช้งาน GPU ได้")
