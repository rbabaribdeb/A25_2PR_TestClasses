from text_generation import Client

client = Client("http://localhost:8000")  # si tu as lancé le serveur local
response = client.generate("Bonjour, explique la relativité générale simplement.", max_new_tokens=200)
print(response.text)