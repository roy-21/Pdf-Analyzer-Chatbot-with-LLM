from langchain import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings


# Global variables
llm = None
llm_embeddings = None


# Function to initialize the language model and its embeddings
def init_llm():
    global llm, llm_embeddings

    api_key = "YOUR API KEY"

    # Initialize the language model with the OpenAI API key
    llm = OpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key
    )

    # Initialize the embeddings for the language model
    llm_embeddings = OpenAIEmbeddings(
        openai_api_key=api_key
    )