import os

print("""
\x1b[38;2;155;20;134m╭━━━┳━━━┳━╮╱╭┳━━┳━━━╮
\x1b[38;2;155;20;134m┃╭━╮┃╭━╮┃┃╰╮┃┣┫┣┫╭━╮┃
\x1b[38;2;155;20;134m┃╰━━┫┃╱┃┃╭╮╰╯┃┃┃┃┃╱╰╯
\x1b[38;2;155;20;134m╰━━╮┃┃╱┃┃┃╰╮┃┃┃┃┃┃╱╭╮
\x1b[38;2;155;20;134m┃╰━╯┃╰━╯┃┃╱┃┃┣┫┣┫╰━╯┃
\x1b[38;2;155;20;134m╰━━━┻━━━┻╯╱╰━┻━━┻━━━╯\x1b[38;2;0;500;58m <~~@MrMarko
""") 

print("""[1] pip\n[2] pip3\nChoose which one to install with.""")

c = input("~|~: ")
if c == "1":
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install pysocks")
    os.system("pip install colorama")
    os.system("pip install undetected_chromedriver")
    os.system("pip install httpx")

elif c == "2":
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip3 install pysocks")
    os.system("pip3 install colorama")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Done.")