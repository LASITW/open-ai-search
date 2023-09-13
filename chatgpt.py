import os
import sys
import time

from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader, Docx2txtLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = "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"

query = None

loader = DirectoryLoader(".",glob="**/*.txt", loader_cls=TextLoader)

index = VectorstoreIndexCreator().from_loaders([loader])

if not query:
  #This is where the question you asked in "Enter Question" 
  # is passed to query
  query = input("Prompt: ")
if query in ['quit', 'q', 'exit']:
  sys.exit()
# The result is generated and send to result, whicdh needs
# to be shown in the Response section
result = index.query(query)
print(" ")
print(result)
print(" ")
#print("Hope, that was helpful. Have a nice day :)")
print(" ")