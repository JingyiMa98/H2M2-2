from transformers import pipeline
from openai import OpenAI

def img2text(url):
    img_to_text_pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    text = img_to_text_pipe(url)[0]["generated_text"]
    return text

def textGeneration(msg):
    client = OpenAI()

    msg_list = [
        {
            "role": "system", 
            "content": "You are a renowned poet. Please write a beautiful and emotional poem that includes a title. The title should reflect the theme of the poem. Use vivid imagery, metaphors, and elegant language. The poem can be of any length, but should evoke deep emotions."
        }
    ]
    msg_list.append(msg)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7, 
        max_completion_tokens=300, 
        messages=msg_list
    )
    print(response)
    out_message = response.choices[0].message.content
    return out_message



def runModels(url):
    scenario = img2text(url)
    message = {"role": "user", "content": scenario}
    story = textGeneration(message)
    return([scenario,story])