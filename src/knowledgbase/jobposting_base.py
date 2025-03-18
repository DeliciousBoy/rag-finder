# knowledgebase/jobposting_base.py

import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

data = None  # ตัวแปรเก็บข้อมูลที่โหลดไว้

def get_data():
    global data
    if data is None:  # โหลดข้อมูล
        data_path = r"D:\GraduationProject\skill_mapping\knowledgbase\developers_programmers_jobposting_corpus_skill.json"
        with open(data_path, encoding="utf-8") as f:
            data = json.load(f)
    return data

def get_skill_corpus():
    vectorizer = TfidfVectorizer()
    data = get_data()
    skill_corpus = [] 
    for item in data:  
        item_skill_list = json.loads(item['combine_skill_corpus'])
        X = vectorizer.fit_transform(item_skill_list)

        skill_corpus.append(vectorizer.get_feature_names_out().tolist())
    return skill_corpus 


skill_corpus = get_skill_corpus()
print("Skill corpus size:", len(skill_corpus))
print(json.dumps(skill_corpus[20],indent=4))