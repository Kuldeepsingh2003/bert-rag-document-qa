from fastapi import FastAPI
app=FastAPI(title="ERT RAG Document QA",
            description='Industry-grade Intelligent Document Question Answering System',
             version="1.0.0")

@app.get("/")
def root():
    return {
        "message": "Welcome to BERT-RAG-Document-QA 🚀"
    }
