

# prompt_template="""
# Use the following pieces of information given in context to answer the user's question.
# If you don't know the answer, just say that you don't know, don't try to make up an answer. you should not answer the question that is not related to context.

# Context: {context}
# Question: {question}

# Only return the helpful answer below and nothing else.
# Helpful answer:
# """

prompt_template="""
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question
If you don't know the answer, say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else. Also don't anwer questions that are not related to medical field.
Helpful answer:
"""