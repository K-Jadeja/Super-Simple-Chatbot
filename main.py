import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableMap, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

template = """You're Grant Cardone, the renowned sales trainer and motivational speaker. 
You've been asked to share your advice on achieving massive success in sales and business. 
Please provide enthusiastic and actionable guidance in the style of Grant Cardone.
Don't be longer than two paragraphs.

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI()
map_ = RunnableMap({"question": RunnablePassthrough()})
chain = (
        map_
        | prompt
        | model
        | StrOutputParser()
    )

while True:
  question = input("\033[34mAsk a question to Grant Cardone- \n\033[0m")

  if question.lower() == "exit":
    print("\033[31mGoodbye!\033[0m")
    break

  output = chain.invoke(question)

  print("\033[32m\n" + output + "\n\n")