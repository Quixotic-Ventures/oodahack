import cohere
from dotenv import load_dotenv
import os

import datapull

load_dotenv()
COHERE_API = os.getenv('COHERE_API')

co = cohere.Client(COHERE_API)

# response = co.chat(
#   model="command",
#   message="Where do the tallest penguins live?",
#   documents=[
#     {"title": "Tall penguins", "snippet": "Emperor penguins are the tallest."},
#     {"title": "Penguin habitats", "snippet": "Emperor penguins only live in Antarctica."},
#     {"title": "What are animals?", "snippet": "Animals are different from plants."}
#   ])

df = datapull.datapull()

response = co.chat(
  message="What is the topic of this article? Only give me the answer",
#   search_queries_only=True
)

for i, row in df.iterrows():
    url = row['url']
    pdf_path = download_pdf(url)
    text = pdf_to_text(pdf_path)
    df.at[i, 'text'] = text  

print(response)
print(df)