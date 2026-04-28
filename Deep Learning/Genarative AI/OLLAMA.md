
# OLLama
## my project-2 base foundation

- **`WebBaseLoader`**: This loader is designed to scrape content from websites.

- **`web_paths`**: This parameter should include URLs or paths to the websites you want to scrape. In this code

- **`bs_kwargs`**: These are arguments passed to the BeautifulSoup4 (bs4) library, which is used for parsing HTML data.

- **`loader.load()`**: This loads the web content scraped by the `WebBaseLoader` into the variable `docs`.

- **`RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)`**: This is used to split the loaded web content into smaller text chunks.

- **`chunk_size=1000`**: Limits the size of each text chunk to 1000 characters.

- **`chunk_overlap=200`**: Ensures there is a 200-character overlap between consecutive chunks for better context preservation.

- **`split_documents(docs)`**: This method applies the splitting logic to the loaded documents, splitting them into smaller chunks, which are stored in `splits`

- The `parse_only` parameter is used with BeautifulSoup to limit the parts of the HTML that are processed. By specifying certain classes, you ensure that BeautifulSoup only looks at the elements that match those criteria.
- - **`SoupStrainers` Class**: `SoupStrainers` is a special class provided by the BeautifulSoup library (bs4) that helps you define which parts of the HTML you want to parse. It acts as a filter, making the parsing process more efficient and focused.**Usage**: When you create a `SoupStrainer`, you specify criteria (like tag names, attributes, or CSS classes) to include or exclude specific elements during the pars
- 
- **`class_=("post-content", "post-title", "post-header")`**: This means you are interested in HTML elements that have one or more of the following classes:

- **`post-content`**: This class likely contains the main body of a blog post or article.
- **`post-title`**: This class likely represents the title or heading of the post.
- **`post-header`**: This class might contain metadata about the post, such as the author, date, or other relevant information.
-

`docs= loader.load()
`text_splitter= RecursiveCharacterTextsplittered(chunk_size=1000,chunk_overlap=200)`
`spilts = text_splitter.spilt_documents(docs)
`embeddings = OllamaEmbeddings(model="llama3.2")
`vectorstore = chrome.from_docments(documents= spilts, embeddings=embeddings
 - **Loading Data**: You load raw text documents from a specified source.
- **Splitting Text**: The loaded documents are split into smaller, manageable chunks while preserving some context through overlapping text.
- **Embedding Generation**: Each text chunk is transformed into a vector representation using a language model designed for embeddings.
- **Vector Store Creation**: The vector representations are stored in a vector store, enabling efficient searches and retrieval based on semantic meaning.




## chunks ?
### HOW DO THEY WORK 
- **Splitting Process**:
- **Chunk 1**: `"Lorem ipsum dolor sit amet, consectetur adipiscing elit, ... [first 1000 characters]"` (characters 0 to 1000)
- **Chunk 2**: Starts at character 800 (overlaps with the last 200 characters of Chunk 1), and continues to character 1800.
- **Chunk 3**: Starts at character 1600 (overlaps with the last 200 characters of Chunk 2), and continues to character 2600.

 ### **Why Use Overlapping Chunks?**
	- In natural language tasks, the meaning of a sentence or a paragraph often depends on the surrounding text. When models process chunks of text independently, they may lose important context if there is no overlap between chunks. By having overlapping sections, models can retain the context from the previous chunk, improving their performance when answering questions or generating text.
## inside 
`response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': formatted_prompt}])`

- **`ollama.chat(...)`**: This line sends a request to the **Ollama Llama3** model to generate a response.

- **`model='llama3'`**: Specifies that the Llama3 model should be used for generating the response.
- **`messages=[{'role': 'user', 'content': formatted_prompt}]`**: The `messages` parameter is an array of message objects. Each message object has two components:
- **`role`**: Here, the role is `'user'`, indicating that the message is coming from the user.
- **`content`**: The actual text (i.e., the formatted prompt with the question and context).
- 