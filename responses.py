def handle_response(message: str,username: str):
    message = message.lower()
    if message.startswith("?crc32"):
        import crc32
        return str(crc32.crc32(message[7:].encode("utf-8")))
    if message.startswith("?crc64"):
        import crc64
        return str(crc64.crc64(message[7:].encode("utf-8")))
    if message.startswith("i love you bot"):
        return f'I love you too {username}'
    if message.startswith("i hate you bot"):
        return f'I hate you too {username}'
    if message.startswith("this bot sucks"):
        return f'kill yourself {username}'
    if "sus" in message:
        return "<:zounasus:946987499983613962>"
    if "give me zouna source" in message:
        return "https://cdn.discordapp.com/attachments/888080380752707627/986683930734374922/ZOUNA.rar"
    if message == "thank you":
        return f"You're welcome {username}!"