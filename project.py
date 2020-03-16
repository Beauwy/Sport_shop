import array as ars

item_shirt_nikie = ["","Nike Sportswear","Nike Wild Run","Nike Polo"]
price_shirt_nikie = ars.array('i',[0,2900,3100,2000])
stock_shirt_nikie = ars.array('i',[0,10,10,10])

item_shirt_adidas = ["","Adidas Run Tee","Adidas Supernova","Adidas Jacket"]
price_shirt_adidas = ars.array('i',[0,800,1200,2259])
stock_shirt_adidas = ars.array('i',[0,10,10,10])

item_pant_nikie = ["","Nike Air Max","Nike Air Force","Nike Jordan",]
price_pant_nikie = ars.array('i',[0,4600,4400,4200])
stock_pant_nikie = ars.array('i',[0,10,10,10])

item_pant_adidas = ["","Ultra boast","Superstar","Stan Smith",]
price_pant_adidas = ars.array('i',[0,7300,4000,3500])
stock_pant_adidas = ars.array('i',[0,10,10,10])

item_shoe_nikie = ["","Nike Sportswear","Nike Pri-Fit","Nike Wild Run",]
price_shoe_nikie = ars.array('i',[0,3100,1400,3100])
stock_shoe_nikie = ars.array('i',[0,10,10,10])

item_shoe_adidas = ["","Adidas Black Shorts","Adidas 3 Striped Shorts","Afidas Running Stripetights",]
price_shoe_adidas = ars.array('i',[0,856,1673,1000])
stock_shoe_adidas = ars.array('i',[0,10,10,10])

total_price=[0]

id = 'login'
password = '1234'

#/////////////////////////////MAIN/////////////////////////////
def main():
    m_login=login()

    if m_login=="true":
        n_select = select()

        if n_select == 1:
            shop()
        elif n_select == 2:
            check_stock()
        
#/////////////////////////////LOG IN/////////////////////////////
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
             print ("Fail login. Please login again!")
             count+=1

        if count >= 3 :
             print ("Fail login. Try login later!!!!")
             login="false"
             break   

    return login  

#/////////////////////////////SELECT/////////////////////////////
def select():
    re_select = 0

    while True:
          print ("-"*30)
          select_1 = int(input("Select Menu  \n 1.Shop \n 2.Check Stock  \n>>>>> "))

          if select_1 >= 1 and select_1 <= 2:
             re_select = select_1
             break

          else:
              print ("Fail Select Again!")

    return re_select

#/////////////////////////////SHOP/////////////////////////////
def shop():
    print ("-"*30)
    print ("Shop Menu")
    print ("-"*30)
    while True:
          select1 = int(input('Do you want to menu? \n 1.Shirts \n 2.Pants \n 3.Shoes \n>>>>> '))

          if select1 == 1:
             shirt()

          elif select1 == 2:
             pant()

          elif select1 == 3:
             shoe()

#/////////////////////////////SHIRT/////////////////////////////  
def shirt():
    print ('-'*30)
    first_select = int(input('What Do you want? \n 1.Nike \n 2.Adidas \n>>>>> '))
    print ('-'*30)

    count = 1
  
    if first_select == 1:

        while count >= 0 and count <= 3:
              print (count," : ",item_shirt_nikie[count], "price", price_shirt_nikie[count])
              count += 1
              
        print ('-'*30)
        select_item = int(input("Select item : "))
        select_reques = int(input("How many item? :"))
        print ('-'*30)

        if select_reques > stock_shirt_nikie[select_item]:
            print ("Not enough product")
            ques = input("Do you want to select another item? (y/n) : ")

            if ques == 'y':
               shop()

            else:
                bill()

        else:
            total_price[0] += price_shirt_nikie[select_item]*select_reques
            stock_shirt_nikie[select_item]-=select_reques
            print (total_price[0])
            ques = input("Do you want to selcet another item? (y/n) : ")

            if ques == 'y':
               shop()

            else:
                bill()

    elif first_select == 2:
         count = 1

         while count >= 0 and count <= 3:
               print (count," : ",item_shirt_adidas[count], "price", price_shirt_adidas[count])
               count += 1

         select_item = int(input("Select item : "))
         select_reques = int(input("How many item? :"))

         if select_reques > stock_shirt_adidas[select_item]:
            print ("Not enough produt")
            ques = input("Do you want to selcet another item? (y/n) : ")

            if ques == 'y':
               shop()

            else:
                bill()

         else:
             total_price[0] += price_shirt_adidas[select_item]*select_reques
             stock_shirt_adidas[select_item]-=select_reques

             print (total_price[0])
             ques = input("Do you want to selcet another item? (y/n) : ")

             if ques == 'y':
                shop()

             else:
                 bill()

#/////////////////////////////PANT/////////////////////////////
def pant():
    print ('-'*30)
    second_select = int(input('What Do you want? \n 1.Nike \n 2.Adidas \n>>>>> '))
    print ('-'*30)

    if second_select == 1:
       count = 1

       while count >= 0 and count <= 3:
             print (count," : ",item_pant_nikie[count], "price", price_pant_nikie[count])
             count += 1

       select_item = int(input("Select item : "))
       select_reques = int(input("How many item? :"))

       if select_reques > stock_pant_nikie[select_item]:
          print ("Not enough produt")
          ques = input("Do you want to selcet another item? (y/n) : ")

          if ques == 'y':
             shop()

          else :
                 bill()

       else:
            total_price[0] += price_pant_nikie[select_item]*select_reques
            stock_pant_nikie[select_item]-=select_reques
            print (total_price[0])
            ques = input("Do you want to selcet another item? (y/n) : ")

            if ques == 'y':
               shop()

            else :
                 bill()

    elif second_select == 2:
         count = 1

         while count >= 0 and count <= 3:
               print (count," : ",item_pant_adidas[count], "price", price_pant_adidas[count])
               count += 1

         select_item = int(input("Select item : "))
         select_reques = int(input("How many item? :"))

         if select_reques > stock_pant_nikie[select_item]:
            print ("Not enough produt")
            ques = input("Do you want to selcet another item? (y/n) : ")
            
            if ques == 'y':
               shop()

            else:
                 bill()

         else:
             total_price[0] += price_pant_adidas[select_item]*select_reques
             stock_shirt_adidas[select_item]-=select_reques
             print (total_price[0])
             ques = input("Do you want to selcet another item? (y/n) : ")

             if ques == 'y':
                shop()

             else:
                  bill()

#/////////////////////////////SHOE/////////////////////////////
def shoe():
    print ('-'*30)
    third_select = int(input('What Do you want? \n 1.Nike \n 2.Adidas \n>>>>> '))
    print ('-'*30)

    if third_select == 1:
       count = 1

       while count >= 0 and count <= 3:
             print (count," : ",item_shoe_nikie[count], "price", price_shoe_nikie[count])
             count += 1

       select_item = int(input("Select item : "))
       select_reques = int(input("How many item? :"))

       if select_reques > stock_shoe_nikie[select_item]:
          print ("Not enough produt")
          ques = input("Do you want to selcet another item? (y/n) : ")

          if ques == 'y':
             shop()

          else:
               bill()

       else:
            total_price[0] += price_shoe_nikie[select_item]*select_reques
            stock_shoe_nikie[select_item]-=select_reques
            print (total_price[0])
            ques = input("Do you want to selcet another item? (y/n) : ")

            if ques == 'y':
               shop()

            else:
                 bill()

    elif third_select == 2:
         count = 1

         while count >= 0 and count <= 3:
               print (count," : ",item_shoe_adidas[count], "price", price_shoe_adidas[count])
               count += 1

         select_item = int(input("Select item : "))
         select_reques = int(input("How many item? :"))

         if select_reques > stock_shoe_nikie[select_item]:
            print ("Not enough produt")
            ques = input("Do you want to selcet another item? (y/n) : ")

            if ques == 'y':
               shop()

            else:
                 bill()

         else:
             total_price[0] += price_shoe_adidas[select_item]*select_reques
             stock_shoe_adidas[select_item]-=select_reques
             print (total_price[0])
             ques = input("Do you want to selcet another item? (y/n) : ")

             if ques == 'y':
                shop()

             else:
                 bill()

#/////////////////////////////CHECK STOCK/////////////////////////////
def check_stock():
    print ("-"*30)
    print ("Check Stock")
    print ("-"*30)
    select = int(input("Selct to check item : \n 1.Shirt \n 2.Pant \n 3.Shoe \n>>>>> "))
    if select == 1:
       choose = int(input("Seleck to check brand : \n 1.Nike \n 2.Adidas \n>>>>> "))
       check_select(select,choose)
    elif select == 2:
         choose = int(input("Seleck to check brand \n 1.Nike \n 2.Adidas \n>>>>> "))
         check_select(select,choose)
    elif select == 3:
         choose = int(input("Seleck to check brand \n 1.Nike \n 2.Adidas \n>>>>> "))
         check_select(select,choose)

def check_select(select,choose):
    if select == 1 and choose == 1:
       count = 1

       while count <= 3:
             print (count,":",item_shirt_nikie[count],"----",stock_shirt_nikie[count])
             count += 1

       add = input("Do you want to add item stock (y/n) : ")

       if add == 'y':
          add_item = int(input("Select to add item stock : "))
          hm_item = int(input("How many item : "))
          stock_shirt_nikie[add_item] += hm_item
          print ("Add item Success!!")
          print (item_shirt_nikie[add_item],"----",stock_shirt_nikie[add_item])
          wh = input("Do you want to add another item? (y/n) : ")

          if wh == 'y':
             check_stock()

          else:
              main()

       else:
           main()

    elif select == 1 and choose == 2:
         count = 1

         while count <= 3:
               print (count,":",item_shirt_adidas[count],"----",stock_shirt_adidas[count])
               count += 1

         add = input("Do you want to add item stock (y/n) : ")

         if add == 'y':
             add_item = int(input("Select to add item stock : "))
             hm_item = int(input("How many item : "))
             stock_shirt_adidas[add_item] += hm_item
             print ("Add item Success!!")
             print (item_shirt_adidas[add_item],"----",stock_shirt_adidas[add_item])
             wh = input("Do you want to add another item? (y/n) : ")

             if wh == 'y':
                 check_stock()
             else:
                  main()

         else:
             main()

    elif select == 2 and choose == 1:
         count = 1

         while count <= 3:
            print (count,":",item_pant_nikie[count],"----",stock_pant_nikie[count])
            count += 1

         add = input("Do you want to add item stock (y/n) : ")

         if add == 'y':
             add_item = int(input("Select to add item stock : "))
             hm_item = int(input("How many item : "))
             stock_pant_nikie[add_item] += hm_item
             print ("Add item Success!!")
             print (item_pant_nikie[add_item],"----",stock_pant_nikie[add_item])
             wh = input("Do you want to add another item? (y/n) : ")

             if wh == 'y':
                 check_stock()

             else:
                 main()

         else:
             main()

    elif select == 2 and choose == 2:
         count = 1

         while count <=3:
               print (count,":",item_pant_adidas[count],"----",stock_pant_adidas[count])
               count += 1

         add = input("Do you want to add item stock (y/n) : ")

         if add == 'y':
             add_item = int(input("Select to add item stock : "))
             hm_item = int(input("How many item : "))
             stock_pant_adidas[add_item] += hm_item
             print ("Add item Success!!")
             print (item_pant_adidas[add_item],"----",stock_pant_adidas[add_item])
             wh = input("Do you want to add another item? (y/n) : ")

             if wh == 'y':
                 check_stock()
          
             else:
                  main()

         else:
             main()

    elif select == 3 and choose == 1:
         count = 1

         while count <= 3:
               print (count,":",item_shoe_nikie[count],"----",stock_shoe_nikie[count])
               count += 1

         add = input("Do you want to add item stock (y/n) : ")

         if add == 'y':
             add_item = int(input("Select to add item stock : "))
             hm_item = int(input("How many item : "))
             stock_shoe_nikie[add_item] += hm_item
             print ("Add item Success!!")
             print (item_shoe_nikie[add_item],"----",stock_shoe_nikie[add_item])
             wh = input("Do you want to add another item? (y/n) : ")
          
             if wh == 'y':
                 check_stock()
             
             else:
                 main()

         else:
             main()

    elif select == 3 and choose == 2:
         count = 1

         while count <= 3:
               print (count,":",item_shoe_adidas[count],"----",stock_shoe_adidas[count])
               count += 1

         add = input("Do you want to add item stock (y/n) : ")

         if add == 'y':
             add_item = int(input("Select to add item stock : "))
             hm_item = int(input("How many item : "))
             stock_shoe_adidas[add_item] += hm_item
             print ("Add item Success!!")
             print (item_shoe_adidas[add_item],"----",stock_shoe_adidas[add_item])
             wh = input("Do you want to add another item? (y/n) : ")

             if wh == 'y':
                 check_stock()
             else:
                 main()

         else:
             main()

#/////////////////////////////BILL/////////////////////////////
def bill():
    print ("-"*30)
    if total_price[0] != 0:
       print ("Total price : ",total_price[0])

       while True:
             money = int(input("Enter your money : "))

             if money < total_price[0]:
                print ("Not enough money!!")

             else:
                 change = money-total_price[0]
                 print ("Total : ",total_price[0])
                 print ("Your money : ",money)
                 print ("Your change : ",change)
                 total_price[0] = 0
                 print ('x'*30)
                 main()
                 break

    else:
        print ("No item in cart!!")
        main()

#/////////////////////////////CALL MAIN/////////////////////////////
main()