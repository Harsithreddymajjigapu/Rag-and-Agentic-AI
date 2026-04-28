	AGENDA - 1.API
			2. how do we use openAI API


# Open-AI API?
-  this Open AI API has been deigned to provide developers with seamless access to state of art, pre trained, artificial intelligence models like gpt-3 gpt-4 dall e whisper, embeddings etc. so by using this openai ape you can integrate cutting edge ai capabilities into your applications regardless the programming language.
So, the conclusion is by using this Open AI API you can unlock the advance functionalities and you can enhance the intelligence and performance of your application.

# Complete chat 
**openai.Completion.create()**: This method is used to generate completions or responses. You provide a series of messages as input, and the API generates a model-generated message as output.
**openai.ChatCompletion.create() :** Similar to Completion.create(), but specifically designed for chat-based language models. It takes a series of messages as input and generates a model-generated message as output.

# function calling
-**function calling in LLM** means asking the chatbot to do specific tasks that need extra help from other tools or services


## Direct Function Call

A **direct function call** is when you use the model's API directly to get a response. You send a question or prompt, and the model gives you an answer right away.

## Indirect Function Call

An **indirect function call** is when you have a middle layer or another function that decides which model or service to use based on what you ask. Instead of calling the model directly, you go through this middle step.
- we just have a middle layer like a data that train the rag its like an api


## Summary

- **Direct Function Call**: You ask the model something, and it answers directly.
- **Indirect Function Call**: There’s another layer that decides how to answer your question, which might involve checking different services before getting a response.