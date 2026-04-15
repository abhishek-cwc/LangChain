from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional

load_dotenv()

class Review(BaseModel):
    name: Optional[str] = Field(description="Write the name of reviewer")
    sentiment:Literal["Positive", "Negative"] = Field(description="Return sentiment of review either Positive or Negative")


model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

structured_model_output = model.with_structured_output(Review)

# result = structured_model_output.invoke(""" Phone is very good and its battery power is too long
#                                  By Abhishek
#                                  """)
# print(result)

###### With Chain ######
prompt = PromptTemplate(
    template="Analyze this review and extract structured info:\n{review}",
    input_variables=['review']
    )

chain = prompt | structured_model_output

result = chain.invoke({
    'review': "Phone is very good and battery lasts long. By Abhishek"
})

print(result)

