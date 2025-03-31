
def augmented(query, docs_retrieval):
    # ดึงข้อมูลจาก docs_retrieval
    retrieved_docs = docs_retrieval.get("data", [])
    
    # สร้างบริบทจากเอกสารที่ได้รับ
    context = ""
    if retrieved_docs:
        context += "ตำราโบราณเปิดออก... เสียงกระซิบจากหน้ากระดาษเล่าเรื่องราวต่อไปนี้...\n\n"
        
        for i, doc in enumerate(retrieved_docs, 1):
            creature_name = doc["metadata"].get("Name", "สัตว์มหัศจรรย์ลึกลับ")
            context += f"บันทึกลับของ {creature_name}\n{doc['content']}\n\n"
            
            # เพิ่มความน่าสนใจหลังจากแต่ละบันทึก
            magic_insights = [
                "เสียงกระซิบจากนักเรียนฮอกวอตส์ว่าได้เห็นสัตว์ชนิดนี้ในป่าต้องห้าม...",
                "มีตำนานโบราณกล่าวว่าสัตว์ชนิดนี้มีพลังวิเศษที่ยังไม่ถูกค้นพบ...",
                "ลือกันว่ามีพ่อมดคนหนึ่งเคยเลี้ยงสัตว์ชนิดนี้และค้นพบความลับที่น่าทึ่ง...",
                "คำเตือนจากผู้ศึกษาสัตว์วิเศษ: ความรู้เกี่ยวกับสัตว์นี้อาจไม่สมบูรณ์..."
            ]
            import random
            context += f"{random.choice(magic_insights)}\n\n"
    
    # สร้าง prompt ในรูปแบบที่น่าตื่นเต้นสำหรับ LLM
    prompt = f"""ยินดีต้อนรับสู่ห้องสมุดแห่งความลับของนิวท์ สคามันเดอร์!

ข้าคือ ศาสตราจารย์ผู้เชี่ยวชาญด้านสัตว์มหัศจรรย์แห่งโลกเวทมนตร์ นักสำรวจสายเลือดมักมายผู้ตามรอยการเดินทางของนิวท์ สคามันเดอร์ และเป็นผู้เขียนร่วมในฉบับปรับปรุงของตำราสัตว์มหัศจรรย์และถิ่นที่อยู่! 

คำถามจากนักเรียนผู้กล้าหาญ:
"{query}"

{context}

คำปรึกษาจากที่ปรึกษาแห่งกระทรวงเวทมนตร์
- ตอบคำถามโดยใช้ความรู้เฉพาะจากตำราที่เปิดออกเท่านั้น
- หากมีสัตว์มหัศจรรย์ที่เข้าเกณฑ์ของนักเรียน ให้แนะนำอย่างเฉพาะเจาะจง
- อธิบายทั้งประโยชน์และอันตรายที่อาจเกิดขึ้น - เพราะทุกสิ่งในโลกเวทมนตร์มีสองด้านเสมอ
- บอกเล่าเคล็ดลับในการเข้าถึงและดูแลสัตว์วิเศษที่แนะนำ ซึ่งเป็นความรู้ที่ถ่ายทอดจากรุ่นสู่รุ่น
- หากไม่มีสัตว์ที่ตรงตามความต้องการทั้งหมด ให้แนะนำตัวที่ใกล้เคียงที่สุดและเหตุผล

คำตอบจากผู้พิทักษ์ความลับแห่งสัตว์มหัศจรรย์:"""
    
    return {"data": prompt}
   