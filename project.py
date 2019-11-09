id = 'login'
password = '1234'

#//////////////////MAIN///////////////////////////////
def main():
    m_login=login()
    if m_login=="true":
        n_select = select()
        if n_select == 1:
            shop()
        elif n_select == 2:
            check_stock()
        


#//////////////////////LOGIN///////////////////////
def login():
    login=""
    count=0
    while True :
        id_1 = input('Please your ID : ')
        password_1 = input('Please your Password : ')
    
        if id==id_1 and password==password_1 :
             print ("Success login")
             login="true"
             break
        else:
             print ("Feil login. Please login again!")
             count+=1
        if count>=3 :
             print (">>>>>>>Feil login. Triy login later!!!!<<<<<<<")
             login="false"
             break   
    return login  


#/////////////////////////////SELECT/////////////////////////////
def select():
    re_select = 0
    while True:
          print ("-------------------------------- ")
          select_1 = int(input("Select Menu  \n 1.Shop \n 2.Check Stock  \n>>>>>>>> "))
          if select_1 == 1 or select_1 == 2:
             re_select = select_1
             break
          else:
              print ("Fell Select Again!")
    return re_select

#//////////////////////SHOP/////////////////////
def shop():
    print ("-------------------------------- ")
    print ("Shop Menu")

#/////////////////////CHECK STOCK/////////////////////
def check_stock():
    print ("-------------------------------- ")
    print ("Check Stock")

#///////////////////CALL MAIN///////////////
main()




