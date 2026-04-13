from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please give me beutifull lines on "{input_topic}" with following specification
length : {length}
style : {style}
""",
input_variables=['input_topic','length','style'],
validate_template=True
)

template.save('template.json')