Com=str(input("Enter a string: ")) #Command
out=""
reg={'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}




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

