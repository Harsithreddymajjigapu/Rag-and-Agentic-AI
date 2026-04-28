- Prompting methods help guide language models to generate accurate and relevant responses. There are different types of prompting methods based on the **amount of guidance** given in the input prompt.
	

| Prompting Type      | Description                                                                                                        | **Example Usage**<br>                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| Zero-Shot Prompting | no context is given to the model as it should get the answer for the parametric knowledge                          | General Q&A, fact-based queries              |
| One-Shot Prompting  | One example is given to guide the model. and that one example is called source knowledge                           | Formatting requests, simple transformations. |
| Few-Shot Prompting  | Multiple examples are provided to define the expected response pattern. those examples are called source knowledge | Text conversion, classification.             |
| Fine-Tuning         | The model is retrained on a new dataset for domain-specific tasks.                                                 | Medical chatbots, legal AI assistants.       |
# prompt Engineering 

Before diving into Langchain’s `PromptTemplate`, we need to better understand prompts and the discipline of prompt engineering.

A prompt is typically composed of multiple parts:

![[Pasted image 20250214121300.png]]

A typical prompt structure.

Not all prompts use these components, but a good prompt often uses two or more. Let’s define them more precisely.

**Instructions** tell the model what to do, how to use external information if provided, what to do with the query, and how to construct the output.

**External information** or _context(s)_ act as an additional source of knowledge for the model. These can be manually inserted into the prompt, retrieved via a vector database (retrieval augmentation), or pulled in via other means (APIs, calculations, etc.).

**User input** or _query_ is typically (but not always) a query input into the system by a human user (the _prompter_).

**Output indicator** marks the _beginning_ of the to-be-generated text. If generating Python code, we may use `import` to indicate to the model that it must begin writing Python code (as most Python scripts begin with `import`).

Each component is usually placed in the prompt in this order. Starting with instructions, external information (where applicable), prompter input, and finally, the output indicator.