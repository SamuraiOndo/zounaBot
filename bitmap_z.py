import os
import sys
import subprocess
import requests
import discord
def extract_bitmap(attachment):
    with open(f"D:\\coding\\zouna bot\\{os.path.basename(attachment)}", "wb") as f:
        
        r = requests.get(attachment)
        f.write(r.content)
    pro = subprocess.run(["D:\\Downloads\\noesisv4451\\noesis.exe", "?cmode", os.path.abspath(os.path.basename(attachment)),os.path.dirname(os.path.abspath(os.path.basename(attachment))) + "\\" + os.path.basename(attachment).split(".")[0]+".png"], text=True)
    return [discord.File(os.path.dirname(os.path.abspath(os.path.basename(attachment))) + "\\" + os.path.basename(attachment).split(".")[0]+".png"),os.path.dirname(os.path.abspath(os.path.basename(attachment))) + "\\" + os.path.basename(attachment).split(".")[0]+".png",os.path.abspath(os.path.basename(attachment))]