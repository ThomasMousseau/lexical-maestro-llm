#!/usr/bin/env python3
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
import os
import argparse
import time
import sys
from io import StringIO


load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH',8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

from constants import CHROMA_SETTINGS

def main():

    # embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    # db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
    # retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
    # match model_type:
    #     case "LlamaCpp":
    #         llm = LlamaCpp(model_path=model_path, max_tokens=model_n_ctx, n_batch=model_n_batch, verbose=False)
    #     case "GPT4All":
    #         llm = GPT4All(model=model_path, backend='gptj', n_batch=model_n_batch, verbose=False)
    #     case _default:
    #         # raise exception if model_type is not supported
    #         raise Exception(f"Model type {model_type} is not supported. Please choose one of the following: LlamaCpp, GPT4All")
        
    #qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)


    parser = argparse.ArgumentParser(description="A script with command-line arguments.")
    parser.add_argument('formatQA', type=RetrievalQA.BaseRetrievalQA)
    parser.add_argument('prompt', type=str)
    args = parser.parse_args()


    while True:
        prompt = args.prompt#sys.argv[1:]
        prompt = " ".join(prompt)
        if prompt == "exit":
            break
        if prompt.strip() == "":
            continue

        try:
            start = time.time()
            res = args.formatQA(prompt)#qa(prompt)
            answer, docs = res['result'], []
            end = time.time()

            print(f"\n> Answer (took {round(end - start, 2)} s.):")
            print(answer)
            return
        
        except Exception as e:
            continue

    print(answer)
    return
    

if __name__ == "__main__":
    main()