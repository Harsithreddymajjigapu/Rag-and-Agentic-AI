# basic terms
- **Prompt template** they are the  external template for the prompts 
- **agents** are those which does the external work that are not done by the llm but it needs llm for knowing what action it should be performed 
- **Memory**: for short term we can do it in variable or dict if its long term we use the vector database 
	- Different conversation chain 
	
		| \|**Feature**     | **Conversation Chain**                                | **Conversation Buffer Chain**                           | **Conversation Buffer Window Memory**                                          |
		| ----------------- | ----------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------ |
		| **What it does**  | Does not remember any previous prompt.                | Remembers the full conversation history.                | Remembers only a fixed number of recent messages.                              |
		| **How it works**  | Works without memory, treating each input separately. | Stores and passes the entire chat history to the model. | Keeps only the last **N** messages (e.g., last 3 or 5), forgetting older ones. |
		| **Example Usage** | FAQ bots, search engines, command bots.               | Virtual assistants, therapy bots, AI tutors             | E-commerce bots, live support, game NPCs.                                      |

- **parameters **:
1. model
	- Specifies which **language model** to use (e.g., `"gpt-3.5-turbo"`, `"gpt-4"`, `"Llama-3"`).
2. temperature=0
	- Controls the **randomness** of responses. so it represent the creativity of the answer should be like if it is more the creativity of the answer will ore creative 
3. max_tokens=None
	- Limits the **number of tokens** (words/characters) in the response.
4. timeout=None
	- defines the **maximum time (in seconds)** to wait for a response before failing.
5. max_retries=2
	- Specifies how many times to **retry** the request if it **fails** due to network issues or API errors.
6. `input_variable` 
	- **Defines the variable(s) the model expects as input** in a LangChain prompt template.
	- ```input_variables=["question"], template=
	  "What is the answer to {question}?"
	  output:`What is the answer to What is AI? ````
	- this output will be taken by the LLM 
7. we use `.run()` if we have one query if more `.genarate()` with the dictionary of questions we have 
- **parametric knowledge** : the knowledge has been learned during model training and is stored within the model weights
- **source knowledge**: the knowledge is provided within model input at inference time, i.e.  via the prompt. 
- `LenghtBasedexampleselector()` this function will take only a particular length of the examples 
- `similarity eample selectors`  this will choose the similar examples 

# chains:
A **chain** in Lang-Chain is a way to **connect multiple components** (like prompts, LLMs, and memory) to create structured workflows for AI interactions.
## Types of chains:
### **Generic Chain**: **Generic Chain** 
- in Lang-Chain is like creating a **custom pipeline** for your prompt. (**manual workflow** for handling prompts efficiently)
	- **You control the flow**:
		- How input is processed
		- How it’s sent to the LLM
		- How the output is handled
### **Combined Document Chain** 
- (CombineDocsChain) is used when you have **multiple documents** and want to merge them into a **single input** before passing it to the LLM.
	- Useful for **retrieval-augmented generation (RAG)** setups.
	**How It Works?**
		- **Loads multiple documents** (e.g., PDFs, articles, notes).  
		- **Combines them** into one structured prompt.  
		- **Sends the merged text** to the LLM for processing.### **Utility Chains in LangChain**
### **Utility Chains**
**pre-built helper chains** that handle specific tasks like **summarization, question-answering, or text transformation** without needing a complex setup.
1. Utility Chains: chains that are usually used to extract a specific answer from a llm with a very narrow purpose and are ready to be used out of the box.
	
## Runnables 
- Runnable is something that can take input process it and give us output by we can just connects them with LLM 
- We can **combine multiple runnables** to create **complex chains**.
- use when building custom chains with complex logic
## LCEL (LangChain Expression Language):
- No need to manually route inputs or connect multiple Runnables.
	- **How LCEL Works**
	LCEL relies on **functional programming concepts**:
	1. **`RunnableLambda(func)`** → Wraps a Python function to make it a **Runnable**.
	2. **`RunnableBranch(*conditions, default)`** → Routes input to the correct Runnable **based on conditions**.
