from transformers import pipeline

nlp_ner = pipeline(
    "ner",
    model="jplu/tf-xlm-r-ner-40-lang",
    tokenizer=(
        'jplu/tf-xlm-r-ner-40-lang',  
        {"use_fast": False}),
    framework="tf"
)

nlp_ner("서귀포시 강창식 전 국장 등 25명 정년·명예퇴임")
