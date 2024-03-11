Com=str(input("Enter a string: ")) #Command
out=""
reg={'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110'}




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
