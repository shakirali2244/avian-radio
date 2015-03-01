import serial
import time
import sys
con = 0
def setup():
        global con
        con = serial.Serial(port='/dev/ttyACM0',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout = 0)
        print(con.name)
        

def read(ser):
        try:
                print "read called"
                response = ""
                time.sleep(0.01)
                c = ser.inWaiting()
                response = ser.read(c)
                return response.encode('hex')
        except Exception:
                setup():
                print "Exception at read"
                

def write(con,code):
        try:
                print "write called"
                ser_data="$M<"+chr(0)+chr(code)+''+chr(code)
                con.write(ser_data)
        except Exception:
                print "exception at write"
    
    
	
def main():
        while True:
                time.sleep(1)
                write(global con,102)
                print read(global con)


if __name__ == "__main__":
        main()



#ser.flush()
#while True:
#    data = data+ser.read(1)
#    time.sleep(1)
#    ava = ser.inWaiting()
#    if(ava):
#        data = data + ser.read(ava)
#    else:
#        print(data)

#print sys.argv[1]
