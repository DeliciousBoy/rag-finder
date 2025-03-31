import json
from .vector_store import get_vector_store

def retrieval(query, top_k):
   vector_store = get_vector_store()
   docs = vector_store.similarity_search_with_score(query, top_k)
   uuids = list(vector_store.index_to_docstore_id.values())
   print("UUIDs: ", len(uuids))
   print(json.dumps(uuids, indent=1))
   results = []
   for res, score in docs:
      results.append(
         {
            "score": f"{score:3f}",
            "content": res.page_content,
            "metadata": res.metadata,  
         } 
      ) 
   return {"data": results}
   
   