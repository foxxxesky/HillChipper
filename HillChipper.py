import sympy as sm
import numpy as np 

print('='*15,'TUGAS BESAR ALOGAIRTMA DAN PEMROGRAMAN','='*15)
print('''
                +--------------------------------+
                |    SYARIIF ABDURRAHMAN BATHIK  |
                |           1202194114           |
                |            SI-43-09            |
                +--------------------------------+
''')

class HillCipher(): # Class untuk Hill Chiper
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getKey(self): #Fungsi untuk matrix KEY agar merubah character menjadi angka
        k = 0
        for i in range(3):
            for j in range(3):
                keyMatrix[i][j] = ord(self.y[k]) % 65 # American Standart Code for Information Interchange
                k += 1

    def getInversKey(self): #fungsi untuk menginvers KEY matrix
        self.getKey()
        convertSM = sm.Matrix(keyMatrix)
        minorCoFactorKeyMatrix = convertSM.adjugate() #untuk mencari kofaktor
        determinantKeyMatrix = convertSM.det() #untuk mencari determinan

        inverseKeyMatrix = (determinantKeyMatrix * minorCoFactorKeyMatrix % 26) #invers key matriks harus tetap modulus 26
        inverseKeyMatrix = inverseKeyMatrix.tolist()

        return inverseKeyMatrix
        
        
    def encryptData(self, messageMatrix): #fungsi encrypt data
        for i in range(3):
            for j in range(1):
                cipherMatrix[i][j] = 0
                for x in range(3):
                    cipherMatrix[i][j] += (keyMatrix[i][x] * messageMatrix[x][j])
                    cipherMatrix[i][j] = cipherMatrix[i][j] % 26

        return cipherMatrix


    def decryptData(self, cipherMatrix): #fungsi decrypt data
        inverseKeyMatrix = self.getInversKey() 
        cipherMatrix = self.encryptData(messageMatrix)
        for i in range(3):
            for j in range(1):
                messageMatrix[i][j] = 0
                for x in range(3):
                    messageMatrix[i][j] += (inverseKeyMatrix[i][x] * cipherMatrix[x][j])
                    messageMatrix[i][j] = messageMatrix[i][j] % 26        
        

    def processEncrypt(self):
        self.getKey()
        for i in range(3):
            messageMatrix[i][0] = ord(self.x[i]) % 65 #untuk merubah char ke angka yg merepresentasikannya

        self.encryptData(messageMatrix)

        CipherText = []
        for i in range(3):
            CipherText.append(chr(cipherMatrix[i][0] + 65)) #untuk convert string ke char yang merepresentasikannya
        print("Ciphertext: ", "".join(CipherText)) 

    def processDecrypt(self):
        self.decryptData(cipherMatrix)
        for i in range(3):
            cipherMatrix[i][0] = ord(self.x[i]) % 65

        CipherText = []
        for i in range(3):
            CipherText.append(chr(cipherMatrix[i][0] + 65))
        print("Decrypted Message: ", "".join(CipherText)) 

if __name__ == "__main__":
    Message = input('Input Text To Encrypt :')
    
    keyMatrix = [[0] * 3 for i in range(3)] 
    messageMatrix = [[0] for i in range(3)] 
    cipherMatrix = [[0] for i in range(3)] 
    
    default_Key = "HILLMAGIC"

output = HillCipher(Message, default_Key)
output.processEncrypt()
decrypt = input('Do You Want To Decrypt The Message ? (y/n) :')
if (decrypt == 'Y' or decrypt == 'y'):
    output.processDecrypt()
    print('Ok Thank You :)')
elif (decrypt == 'N' or decrypt == 'n'):
    print('Ok Thank You :)')
else:
    print('Wrong Input !!!')