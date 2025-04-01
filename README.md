
# Documentation

## Requirements
In order to run the application you would need:
1. Ollma running locally with the "nomic-embed-text" model
2. Pinecone account and api key
- the index should be dense and have 768 dimensions
3. Anthropic account and api key

> **_NOTE:_** You might also need to install any missing python packages.

## How to run the code?
1. Clone the bazel-docs repo as it's used by the documentation search tool
2. Fill in the missing config options in the config.py file
3. Clone the bazel-docs repo
4. Generate embeddings
- create a dense index with 768 dimensions
- generating embeddings is one-time operation
- as the embeddings are 1,424, the generation takes a significant time
5. run the chatbot, i.e
```
python main.py
```
6. Enjoy!

## Tips & Tricks
- use "exit" to stop the chatbot
- use "debug" to see messages in the chatbot

> **_NOTE:_** In its current version the chatbot doesn't persist chats and all messages in a program run are treated to be part of the same chat. It's better to rerun the chatbot when a new conversation is needed.





