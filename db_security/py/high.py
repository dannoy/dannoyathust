import dm
import os

user = {'name':'HILOGIN','passwd':'HILOGIN'}

class Sender:
    def __init__(self,user):
        self.name = user['name']
        self.passwd = user['passwd']
        self.seq = 1
    def test(self):
        table = "t1"
        dm.connect('localhost','ADB',self.name,self.passwd)
        dm.test()
        n = dm.insert('pc1v2','pc2v2')
        print "%d column affected" % n
        n = dm.select('pc1v1')
        print "%d column selected" % n
    def prepare(self):
        global user
        self.data = []
        for key in ['name','passwd']:
            self.data = self.data + [c for c in user[key]]
            self.data = self.data + [0]

        print self.data
        
    def start(self):
        dm.connect('localhost','ADB',self.name,self.passwd)
        for ch in self.data:
            self.send_char(ch)

    def send_char(self,ch):
        print ch
        
        if type(ch) != int:
            data = ord(ch)
        else:
            data = ch
        data = bin(data)
        data = data[2:]
        print data
        i = 7
        length = len(data)
# print "length %d" % length 
        while i > -1:
            if i > length-1:
                self.send_bit('0')                
            else:
                self.send_bit(data[length - i - 1])
            i = i - 1
    def send_bit(self,bit):
        print bit
        # send DATA
        if bit == '1':
            n = dm.insert('DATA','hc2data')
            if n != 1:
                #print "insert DATA error"
                os.abort()
        # insert DATA-READY
        n = 0
        while n == 0:
            n = dm.insert('HR','hc2data')
            #if n == 0:
                #print "insert HR error"
            
        # wait LOW-READ-FINISHED
        n = 0
        while n == 0:
            n = dm.select('LR')
            #print "select n %d" % n
        #  delete DATA
        n = dm.delete('DATA')
        n = dm.delete('HR')
        # wait LOW-READ-FINISHED-DELETED
        n = 1
        while n > 0:
            n = dm.select('LR')       
        

if __name__ == "__main__":
    su = Sender(user)
    '''su.start()'''
    su.prepare()
    su.start()


    






    
