with open(r"D:\vsCode\CO project\new.txt","r") as file:
    data = file.readlines()
par= ""
for i in range (0,len(data)):
    par += data[i]
lines = par.split('\n')
n = len(lines) 

reg={'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}

def decimal_to_twos_complement(decimal_num, num_bits):  #Parth (with the help of internet)
    if decimal_num < 0:
        positive_binary_str = bin(abs(decimal_num))[2:].zfill(num_bits)
        
        flipped_bits = ''.join(['1' if bit == '0' else '0' for bit in positive_binary_str])
        binary_str = bin(int(flipped_bits, 2) + 1)[2:].zfill(num_bits)
    else:
        binary_str = bin(decimal_num)[2:].zfill(num_bits)
        
    return binary_str


def RType(I):
    out=""
    rs2= I[10]+I[11]
    rs1= I[7]+I[8]
    rd= I[4]+I[5]
    if (I[0]=='a' and I[1]=='d' and I[2]=='d'):
        out+="0000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="000"
        out+=reg[rd]
        out+="0110011"
        return out
    def RType(I):
    out=""
    rs2= I[10]+I[11]
    rs1= I[7]+I[8]
    rd= I[4]+I[5]
    if (I[0]=='a' and I[1]=='d' and I[2]=='d'):
        out+="0000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="000"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='s' and I[1]=='u' and I[2]=='b' and I[7]!='z'):
        out+="0100000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="000"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='s' and I[1]=='u' and I[2]=='b' and I[7]=='z'):
        rs2= I[12]+I[13]
        rs1= I[7]+I[8]+I[9]+I[10]
        rd= I[4]+I[5]
        out+="0100000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="000"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='s' and I[1]=='l' and I[2]=='l'):
        out+="000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="001"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='s' and I[1]=='l' and I[2]=='t' and I[3]!='u'):
        out+="000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="010"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='s' and I[1]=='l' and I[2]=='t' and I[3]=='u'):
        rs2= I[11] + I[12]
        rs1= I[8]  + I[9]
        rd= I[5] + I[6]
        out+="000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="011"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='x' and I[1]=='o' and I[2]=='r'):
        out+="000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="100"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='s' and I[1]=='r' and I[2]=='l'):
        out+="000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="101"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='o' and I[1]=='r'):
        rs2= I[9] + I[10]
        rs1= I[6]  + I[7]
        rd= I[3] + I[4]
        out+="000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="110"
        out+=reg[rd]
        out+="0110011"
        return out
    if (I[0]=='a' and I[1]=='n' and I[2]=='d'):
        out+="000000"
        out+=reg[rs2]
        out+=reg[rs1]
        out+="111"
        out+=reg[rd]
        out+="0110011"
        return out


def Stype(I):
    if (I[0]=='s' and I[1]=='w'):
        out=""
        list1=I.split(" ")
        temp1=list1[-1].split(",")
        temp=temp1[1].split("(")


        Num=decimal_to_twos_complement(int(temp[0]),12)

        for i in range(0,7):
            out+=Num[i]
        rs2= temp1[0]
        rs1= temp[1][0]+temp[1][1]
        out+=reg[rs2]
        out+=reg[rs1]
        out+="010"
        for n in range(7,12):
            out+=Num[n]
        out+="0100011"
        return out


def IType(I) :  #Parth
    out=""
    if (I[0]=='l' and I[1]=='w'):
        list1=I.split(" ")
        temp1=list1[-1].split(",")
        temp=temp1[1].split("(")

        out= decimal_to_twos_complement(int(temp[0]),12)
        
        rs1= temp[1][0] + temp[1][1]
        rd= temp1[0]
        out+= reg[rs1]
        out+= "010"
        out+= reg[rd]
        out+= "0000011"
        return out
    if (I[0]=='a' and I[1]=='d' and I[2]=='d' and I[3]=='i'):
        out=""
        temp= I.split()[1].split(",")
        out= decimal_to_twos_complement(int(temp[2]),12)
        rs1= temp[1]
        rd= temp[0]
        out+= reg[rs1]
        out+= "000"
        out+= reg[rd]
        out+= "0010011"
        return out
    if (I[0]=='s' and I[1]=='l' and I[2]=='t' and I[3]=='i' and I[4]=='u'):
        out=""
        temp= I.split()[1].split(",")
        out= decimal_to_twos_complement(int(temp[2]),12)
        rs1= temp[1]
        rd= temp[0]
        out+= reg[rs1]
        out+= "011"
        out+= reg[rd]
        out+= "0010011"
        return out
    if (I[0]=='j' and I[1]=='a' and I[2]=='l' and I[3]=='r'):
        out=""
        temp= I.split()[1].split(",")
        out= decimal_to_twos_complement(int(temp[2]),12)
        rs1= temp[1]
        rd= temp[0]
        out+= reg[rs1]
        out+= "000"
        out+= reg[rd]
        out+= "1100111"
        return out


