import serial
import time
import sys
con = 0
def setup():
    global con
    try:
        con = serial.Serial(port='/dev/ttyACM0',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout = 0)
        #print(con.name)
    except serial.SerialException:
        print "cannot find the multiwii board son"

def read():
        global con
        try:
                #print "read called"
                response = ""
                time.sleep(0.01)
                c = con.inWaiting()
                response = con.read(c)
                return response.encode('hex')
        except Exception:
                print "read failed"
                setup()
                

def write(code):
        global con
        try:
                #print "write called"
                ser_data="$M<"+chr(0)+chr(code)+''+chr(code)
                con.write(ser_data)
        except Exception:
                #print "exception at write"
                print "write failed"
                setup()
    
    
        
def main():
        while True:
                time.sleep(1)
                write(102)
                print read()


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
