import os
from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain. embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

api_key="Your-api-key"

llm=GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)


instructor_embedding=HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")

vectordb_filepath="faiss_index"

def create_vector_db():

    loader=CSVLoader(file_path='codebasics_faqs.csv', source_column="prompt",encoding="latin-1")
    
    data=loader.load()

    vectordb=FAISS.from_documents(documents=data,embedding=instructor_embedding)

    vectordb.save_local(vectordb_filepath)

def get_qa_chain():

    vectordb = FAISS.load_local(vectordb_filepath, instructor_embedding)

    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs=chain_type_kwargs)
    return chain

if __name__=="__main__":
    create_vector_db()
    chain = get_qa_chain()
    print(chain("Do you have javascript course?"))