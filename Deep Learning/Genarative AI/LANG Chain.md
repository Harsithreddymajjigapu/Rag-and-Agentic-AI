	how to use the langnchain
	promt templating 
	chains
	agents
	memory
	document loader
	hugging face api
- lang chain is a rapper on any api 
- we can use any api mot only open ai
# limitation of open-ai
- its not free we cant use it as an open source 
- its trained till a time data 
- present or daily thing cant be stored
## open ai playground
- this means how a chatbot should behave 
# what is the use of lang chain
- we can use it for different LLMS by using different API
- we can access private data 
- we can also access third party 
- we can also create different prompt template 
# prompt template
- **Prompt templating** is a way to create flexible and reusable prompts for language models (like GPT). Instead of writing a new prompt every time, you make a general template with empty spaces (called **placeholders**) that you can fill in with different words or information. This saves time and helps you easily adjust what you're asking the model.
- we are going to make the it remember i think
# agent 
- we use agent to get real time data
- we are going to use serp API 
- we install google search key
-    we can install Wikipedia and more 
# chain
In Lang-Chain, a "chain" is a series of steps that work together to complete a task. Each step does something different, like changing information or finding data.
- connecting two or more thing that process the data is called chain
- if we want to combine multiple chain and set a sequence for that we use simple sequential chain
# document loader 
- https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/

# Memory
- it remembers the conversions we built a conversation chains 
- we can make it only remember some prompts like last 5 or the last 10  

## Temperature
- in 0 temperature the model becomes more like a robot but when it comes to creative and different we need to increase the temperature as it will 

- when the temperature increases it will increase the randomness it will give you more diverse and creative responses

- If you always set the temperature to 0, you limit the model's ability to explore its knowledge. It will always choose the "safest" answers, which might not be the most helpful or engaging in every context. like when it comes to creative 

## conversation Buffer Window Memory
- it will only remember the last 5 to7 conversation which make the chatbot more faster and efficient instead of remembering the whole conversation 
- we will pass a key so that it remembers the number of prompts it should remember 
### Example of How It Works:
Suppose the conversation buffer window is set to 3 turns. If the conversation progresses like this:
    
1. User: "Tell me about climate change."
2. Bot: "Climate change refers to..."
3. User: "What about its effects on sea levels?"
4. Bot: "Sea levels are rising due to..."
5. User: "How does this affect coastal cities?"
    
In this case, the memory will only store turns 3, 4, and 5, forgetting the earlier ones (1 and 2).

# Different conversation chain 

|                | **Conversation Chain**                            | **Conversation Buffer Chain**               | **Conversation Buffer Window Memory**:                                                                                  |
| -------------- | ------------------------------------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| What it does   | It do not   even remember the last prompt we gave | Assistants that remember full chat          | Short-term memory for recent context like                                                                               |
| How it work    | Simple bots with no memory.                       | the whole memory of the chat will be saved  | You can decide how many messages the chatbot should remember, like 3 or 5. It will keep only that many recent messages. |
| Examples usage | FAQ bots, search engines, command bots            | Virtual assistants, therapy bots, AI tutors | E-commerce bots, live support, game NPCs                                                                                |

# what is a vector database
- it is a database where we store high dimensional vector values 
- it can store the embeddings of words and the image 
### vector
- the magnitude and the direction on the 2d or any dimensional  plane 
- if you have 2 numbers in a vector that a 2d vector and n numbers that a n dimensional vector
## how
-  sparse matrix 
1. here you cant preserve the context its meaning less
- embedding = its to represent the text in the vector form 
- its word 2 vec method
- when it comes to our ai this is a high dimensional like it will have at least 300 dimensions 
-  
- we use vector data base for faster retrieval and similarity search to long 
#  Use of vector data base
- long-trem memory for LLMs 
- sematic search 
- similarity search 
	