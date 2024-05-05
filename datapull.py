import pandas as pd
# from data_download import download_pdf, pdf_to_text


from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()




client = OpenAI()
openai.api_key = os.getenv("OPENAI_API")

def datapull():
    df = pd.read_csv('data.csv')
    df['text'] = None 
    df['title'] = None

    for i, row in df.iterrows():
        url = row['url']
        pdf_path = download_pdf(url)
        text = pdf_to_text(pdf_path)
        df.at[i, 'text'] = text  

        response = co.chat(
        message="What is the title? Only give me the answer only. \n\n\n\n\n" + text,
        #   search_queries_only=True
        )
        df.at[i, 'title'] = response.text  

    return df

def threatpull():
    df = pd.read_csv('data_with_title.csv')
    df['threats'] = None

    for i, row in df.iterrows():
        text = row['text']
        response = openai.Completion.create(
            model="gpt-4-turbo", 
            messages=[{"role": "system", 
                        "content": "Give me the list of " + text}],
            max_tokens=500  # Adjust based on how long you want the response to be
            )
        
    return response.choices[0].message.content

if __name__ == '__main__':
    # df = datapull()
    # print(df)
    print(threatpull())
    # df.to_csv('data_with_threats.csv', index=False)

    # df = pd.read_csv('data_with_title.csv')
    # print(df['text'][0])