from retrieval import retrieval
from augmented import augmented

def rag_pipeline(query, top_k):


   docs_retrieval = retrieval(query, top_k)
   prompt = augmented(query, docs_retrieval)
   
   test = prompt
   return test


query = "ฉันอยากเสี่ยงสัตววิเศษที่ ที่เป็นมิตร ต่อพ่อมด อาศัยอยู่ในนํ้า ชอบกินผักขม มีตัวอะไรเเนะนำบ้าง?"
test = rag_pipeline(query, 3)
print(test.get("data", []))