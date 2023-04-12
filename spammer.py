print("""
                                                                                                 
                    Webhook Spammer by VCode Dev                        
                    Stworzono przez VCode Developer
                    Github: VCode Dev
""")

from dhooks import Webhook
import time

message = input("Co bys chcial wyslac: ")
webhookurl = Webhook(input("Wklej URL webhooka: "))
delay = int(input("Wskaz czas wysylania wiadomosci: "))

while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Wyslano...")
