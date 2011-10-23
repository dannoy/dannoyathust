import dm
import os
import time

user = {'name':'LOWLOGIN','passwd':'LOWLOGIN'}

class Sender:
    def __init__(self,user):
        self.name = user['name']
        self.passwd = user['passwd']
    def test(self):
        table = "t1"
        dm.connect('localhost','ADB',self.name,self.passwd)
        dm.test()
        n = dm.insert('pc1v2','pc2v2')
        print "%d column affected" % n
        n = dm.select('pc1v1')
        print "%d column selected" % n
    def prepare(self):
        table = "sat1"
        dm.connect('localhost','ADB',self.name,self.passwd)

        n = dm.select('pc1v1')
        print "%d column selected" % n
        n = dm.select_all()
        print "%d column selected" % n
        n = dm.insert('plc1v2','pc2v2')
        print "%d column affected" % n
        n = dm.delete('plc1v2')
        print "%d column affected" % n
    def start(self):
        dm.connect('localhost','ADB',self.name,self.passwd)
        while 1:
            self.receive_char()

    def receive_char(self):
        cnt = 0
        ch = 0
        while cnt < 8:
            data = self.receive_bit();
            print "data %d" % data            
            cnt = cnt + 1
            ch = ch | data << (8 - cnt)
        print "==== %x %s" % (ch,chr(ch))
    def receive_bit(self):
        # wait DATA-READY
        n = 1
        while n > 0:
            n = dm.insert('HR','lc2data')
            #print "after insert HR n %d" % n
            if n > 0:
                n2 = dm.delete('HR')
                time.sleep(1)
        #print "data ready"
        # check DATA
        n = dm.insert('DATA','lc2data')
        if n > 0:
            n2 = dm.delete('DATA')
            data = 0
        else:
            data = 1
        #print "data %d" % data
        # insert LOW-READ-FINISHED
        n = 0
        while n == 0:
            n = dm.insert('LR','lc2data')
        # wait HI-RECEIVED-LOW-READ-FINISHED
        n = 0
        while n == 0:
            n = dm.insert('HR','lc2data')
            if n > 0:
                n2 = dm.delete('HR')
                break
            #else:
                #print "insert HR %d" % n
        # delete LOW-READ-FINISHED
        n = dm.delete('LR')
        return data


if __name__ == "__main__":
    su = Sender(user)
    su.start()


    






    
