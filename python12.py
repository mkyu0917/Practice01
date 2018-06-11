
for i in range(1,101):
        if str(i).count("3")+ str(i).count("6") + str(i).count("9")==1:
           print(str(i) +"짝")

        if str(i).count("3")+str(i).count("6") + str(i).count("9")== 2:
            print(str(i) +"짝짝")



        #1f i%30==3>1and i/30>=1 or i%30==6>1and i/30>=1 or i%30==9 and i/30>=1:
        #    print(str(i)+"짝짝")

        #if i/30 ==1 or 2 or 3 and i%30 ==3 or 6 or 9:
        #   print(str(i) + "짝짝" )
