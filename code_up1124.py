text=input()
where_h=text.index("H")
c_amount=text[1:where_h]
y_amount=text[where_h+1:]
print(int(c_amount)*12+int(y_amount))