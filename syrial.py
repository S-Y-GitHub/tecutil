import sys
import serial
import serial.tools.list_ports
import threading

VID = 1027
PID = 24577


def getPort():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if p.vid == VID and p.pid == PID:
            return p
    print("tecが接続されていません")
    sys.exit(1)


try:
    f = open(sys.argv[1], "rb")
except FileNotFoundError:
    print("binファイルが見つかりません")
    sys.exit(1)

b = b"\033TWRITE\r\n"

data = f.read()
if len(data) == 0:
    print("binファイルが空です")
    sys.exit(1)

print("bin : "+data.hex())
b += data

comport = serial.Serial(getPort().device)
comport.write(b)
comport.flush()

EXIT = "~."

print("書き込み成功\t終了するには \""+EXIT+"\" を入力してください\n")


def send():
    while True:
        s = input()
        if s == EXIT:
            print("終了します")
            sys.exit(0)
        comport.write((s+"\n").encode("UTF-8"))
        comport.flush()


def receive():
    while True:
        if(comport.in_waiting > 0):
            bs = comport.read_all()
            while True:
                try:
                    print(bs.decode("UTF-8"), end="", flush=True)
                    break
                except UnicodeDecodeError:
                    # もし中途半端なところまでしか読めてなかったら読み足す
                    bs += comport.read_all()
                    continue


threading.Thread(target=send).start()

# receiveスレッドだけデーモン化する(sys.exitで終了するため)
receiveTh = threading.Thread(target=receive)
receiveTh.setDaemon(True)
receiveTh.start()
