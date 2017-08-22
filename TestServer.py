from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep


class ClientChannel(Channel):
    def Network(data):
        print(data)

    def Network_myaction(data):
        print("myaction:", data)


class MyServer(Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print('new connection:', channel)


if __name__ == "__main__":
    myserver = MyServer()
    while True:
        # print("listening...")
        myserver.Pump()
        sleep(0.0001)