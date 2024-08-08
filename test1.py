
import os
from langchain_huggingface import ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from brain import network
import warnings

from langchain_core.tools import tool

warnings.filterwarnings("ignore")

parser = StrOutputParser()


llm = network.llm_selection("meta-llama/Meta-Llama-3-8B-Instruct")

model = ChatHuggingFace(llm=llm, verbose=True)


from langchain_core.messages import AIMessage,HumanMessage

history = [HumanMessage(content="hi! I'm bob"),AIMessage(content="Hello bob!")]
while True:
    user_query = input()
    if 'exit' in user_query:
        break

    history.extend([HumanMessage(content=user_query)])
    
    response = model.invoke(history)
    print(response.content)

    history.extend([AIMessage(content=response.content)])
