from socket import AF_INET,SOCK_STREAM,socket
#AF_INET yerel yerel internet adresini bulmak icin
#SOCK_STREAM ise veri akis icin
from threading import Thread


clients = {}
adresses = {}
# dictionary oluşturduk baglananalrin bilgilerini almak icin
##host =socket.gethostbyname(socket.gethostname()) ip adresi almak icin bu kulanılır dinamik olarak da

HOST ="127.0.0.1"   #'127.0.0.1'#localhost,IP adresi yerel # sadece bu pc kullanabilecek sanirim o yuzden 192 li olan ip almak lazim yani bu 192.168.1.9
#LAN disinda ise public ip yazyoz ama client.py a bu yine bu 
PORT = 23456 #22 ve 80 secme
BUFFERSIZE =1024 #  birim veriyi islemesi icin pc ye verilen sure gibi bir sey
ADDR = (HOST,PORT)# ip adresimizi ve yayım yapacagımız port
SERVER = socket(AF_INET,SOCK_STREAM) #her socket yaparken yaoacagın sey :D socket nesnesi olusturduk
# bu socket baglantilari kabul etmek icin sadece diger socket haberlesme socketi

SERVER.bind(ADDR) #serveri ip adresi ile yayım yapılacak portla esledik



def received_message():
    """gelen mesajlari kontrolunu saglayan fonksiyon"""
    while(True):
        client, client_adress =SERVER.accept()#kabul etme cliemt socket objesi client_adress ise adresi 
        #bu methot surekli doncek ve birisi baglanmaya basladıgı zaman methot istemciyle baglantisi icin socket ve istemcinin adresini dondurcek
        #unutma istemciye baglanmak icin burdan gelen socketi kullanacagiz
        
        print("%s:%s baglandi."%client_adress)# veri mi formatlıyo tam anlamdım part2.1 de var koddunyam socket
        #veriyi byte olarka gonderebiliyoruz utf8 de format
        
        client.send(bytes("wellcome the chat application(powered by otk)/n Please Enter a nickname:","utf8"))
        #client objesini clients listesine atiyoruz
        
        adresses[client] = client_adress
        # aynı anda diger fonksiyonlari da calıstırmak icin 
        
        Thread(target=connect_client, args=(client,)).start()#args connect_client fonksiyonunu calistirmak icin gereken arg virgul olmasi ise birden cok client gelecek ya ondan.




def connect_client(client):
    """client baglantisini saglar"""
    name = client.recv(BUFFERSIZE).decode("utf8")#client in ilk mesaji isim olcak onu da name degiskenine atadik
    wellcome = "wellcome {}! to exit chat application please enter *exit*".format(name)#cikis yapmak icin *exit* yazcak cmd icin ek olarak da hosgeldin mesaji
    client.send(bytes(wellcome,"utf8"))
    #birisi chat a katildiginda herkese ...katıldı mesaji gitsin
    
    msg="{} chat kanalina katildi".format(name)
    #stream_chat fonksiyonunda yayimlayacaz mesaji
    
    stream_chat(bytes(msg,"utf8"))
    clients[client]=name#clients listesine client adini girecek
    while True:
        message = client.recv(BUFFERSIZE)#byte formatinda 
        if message != bytes("*exit*","utf8"):
            stream_chat(message,name + ":")#ahmet : selam gibi message selam name ahmet : ise biz koyduk
        else:
            client.send(bytes("*exit*","utf8"))
            client.close()#socketi kapadik
            del clients[client]#cikan kullaniciyi sildik
            stream_chat(bytes("{} siktirolup gitti..".format(name),"utf8"))
            break


    



def stream_chat(message,person=""):#person argumani koymazsak boş olcak genel mesajlar icin
    for a in clients:# butun clientlara doncek ve butun clientlara mesaji gonderecek
        a.send(bytes(person,"utf8")+message)#message zaten byte formatinda bu yuzden byte a cevirmedik

 #program start


if __name__ == "__main__":#eger bu dosya calisirsa
    SERVER.listen(3)#max 10 kisi dinleyebilir servar a  dinleme komutu 
    #ayrica listen() fonksiyonu accept()methotundan once cagrilmasi lazim
    print("waiting connection...")
    ACCEPT_THREAD =Thread(target=received_message)#received message fonksiyonun calismasini icin thread
    ACCEPT_THREAD.start()#baslatiyoruz
    ACCEPT_THREAD.join()#joine bak 
    SERVER.close()#servari kapatiyoz






