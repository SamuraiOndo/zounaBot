from deep_translator import GoogleTranslator
def handle_response(message: str,username: str):
    message = message.lower()
    if message.startswith("i love you") and "bot" in message:
        return f'I love you too {username}'
    if message.startswith("i hate you") and "bot" in message:
        return f'I hate you too {username}'
    if message.startswith("this bot sucks"):
        return f'kill yourself'
    if message == "thanks bestie":
        return f"You're welcome!"
    if "give me zouna source" in message:
        return "https://cdn.discordapp.com/attachments/888080380752707627/986683930734374922/ZOUNA.rar"