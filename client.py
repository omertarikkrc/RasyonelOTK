from socket import AF_INET,SOCK_STREAM,socket
#AF_INET yerel yerel internet adresini bulmak icin
#SOCK_STREAM ise veri akis icin
from threading import Thread

from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from chadgptgui import ChatWindow



##socket seyisileri

HOST = '127.0.0.1'  #'127.0.0.1'# local host
PORT = 23456
BUFFERSİZE = 1024
ADRES = (HOST,PORT)
client_socket =socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADRES)


class Abee_Chat(QtWidgets.QMainWindow):
    def __init__(self):
        super(Abee_Chat,self).__init__()## allah askına ogren bi gun
        self.ui = ChatWindow() #chadgptgui dosyasina bak nasil calistigini anlamak icin
        self.ui.initUI()#calıstırmak icin chatgui e bak
        ## baglama isleri burada olacak 
        print("init")
        self.ui.kullanici_input.returnPressed.connect(self.message_send)# entera basinca send_message fonksiyonu calıstıyor

        Thread(target=Abee_Chat.receivedcmsg,args=(self,)).start()
        



## anlasılmayan yer message_send fonksiyonu parametre olarak sadece self alıyor
## ama icinde kullanici_input gibi degiskenler var onlar da self in altinda ondan sanırım


    def message_send(self):
        
        #client_socket.send(self.ui.kullanici_input.text().encode("utf8"))# ya da client_socket.send(bytes(self.ui.kullanic_input.text(),"utf8"))
        client_socket.send(bytes(self.ui.kullanici_input.text(),"utf8"))
        print("message_send fonksiyonu")

        self.ui.kullanici_input.setText("")# her mesaj gondermede input labelini temizliyor ne ise yaradigini anlamak icin bu satiri komple yorum satiri yap 


    def receivedcmsg(self):
        print("receivedmsg fonksiyonu")
        while True:
            self.ui.temp_text = str(client_socket.recv(1024).decode("utf8"))
            self.ui.sohbet.append(self.ui.temp_text)

            



            
            

            
          
            

        

        


       







    


def status_exit():
    pass


























def app(): 
    application= QtWidgets.QApplication(sys.argv)
    pencere = Abee_Chat()   
    pencere.show()
    sys.exit(application.exec_())# carpiya basinca kapanmasini saglar
app()
