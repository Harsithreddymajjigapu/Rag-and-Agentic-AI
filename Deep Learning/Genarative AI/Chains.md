# What are Chains in LangChain: 
- a **chain** is a sequence of steps that process inputs and generate outputs. Each step can involve:
## How Do Chains Work:
- **Receive an Input** (e.g., a user query)
- **Process the Input** (fetch data, modify the prompt, etc.)
- **Call an LLM or other tools** (generate text, retrieve docs, query databases, etc.)
- **Post-process the output** (extract relevant data, format results, etc.)
- **Return the Final Output
# Types of Chains in LangChain**
###  LCEL Chains (New and Recommended)
- Built using **LangChain Expression Language (LCEL)**
- More **modular, flexible, and optimized**
- Supports **streaming, async execution, batch processing, and better debugging**
- Uses **"runnable"** (smaller, reusable components)
### Legacy Chains (Older but Still Supported)
- Built using **traditional class-based programming**
- Works fine but is **less efficient and harder to customize**
- Will be replaced by LCEL-based chains in the future