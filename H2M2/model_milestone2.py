from transformers import pipeline
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

def img2text(url):
    img_to_text_pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    text = img_to_text_pipe(url)[0]["generated_text"]
    return text

def textGeneration_langChain(msg,type):
    """
    msg is the scenario for the text from the pic (hugging face model output);
    type is the genre of the text- Light, Watering, Humidity, Temperture, Pruning, Propagation
    """
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.2,
        max_tokens=200,
        timeout=None,
        max_retries=2
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert gardener in giving {suggestion_type} plants caring suggestions. Provide detailed gardening advice regarding {suggestion_type}. Use the following pieces of retrieved context to generate {suggestion_type} suggestions based on the plants in the given scenario. Use a simple narrative structure to generate these suggestions. Keep the suggestions to less than 150 words.",
            ),
            (
                "human", 
                "{scenario_lang}"
            ),
        ]
    )

    chain = prompt | llm | StrOutputParser()

    out_message = chain.invoke({
        "suggestion_type" : type,
        "scenario_lang" : msg,
    })

    return out_message

def runModels_langchain(url, type):
    scenario = img2text(url)
    suggestions = textGeneration_langChain(scenario,type)
    return([scenario,suggestions])


def getRetriever(dir):
    """
    dir is the directory of the vector DB
    """
    embeddings_used = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorDB = Chroma(persist_directory=dir,embedding_function=embeddings_used)
    retriever = vectorDB.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    return retriever


def textGeneration_langChain_RAG(msg,type,retrieverDir):
    """
    msg is the scenario for the text from the pic (hugging face model output);
    type is the genre of the text- Light, Watering, Humidity, Temperture, Pruning, Propagation
    retriever is the vector DB with relevant stories from txt version of 
        plants dataset from Hugging face - https://huggingface.co/datasets/jibrand/Plant-dataset
    """
    llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.2,
            max_tokens=200,
            timeout=None,
            max_retries=2
        )

    system_prompt = (
        "You are an expert gardener in giving {suggestion_type} plants caring suggestions." 
        "Provide detailed gardening advice regarding {suggestion_type}."
        "Use the following pieces of retrieved context to generate {suggestion_type} suggestions based on the plants in the given scenario."
        "Use a simple narrative structure to generate these suggestions."
        "keep the suggestions to less than 100 words."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{scenario_lang}"),
        ]
    )

    rag_chain = prompt | llm | StrOutputParser()

    retriever = getRetriever(retrieverDir)

    out_message = rag_chain.invoke({
            "suggestion_type" : type,
            "context":retriever,
            "scenario_lang" : msg,
        })
    
    return out_message

def runModels_langchain_RAG(url, type, retrieverDir):
    scenario = img2text(url)
    suggestions = textGeneration_langChain_RAG(scenario,type,retrieverDir)
    # print(suggestions)
    return([scenario,suggestions])