import mysql.connector
try:
   # Connect to the MySQL server
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="Root@123"
    )

   # Create a cursor object
   mycursor = mydb.cursor()

   # Execute the SQL statement to create the database
   mycursor.execute("CREATE DATABASE Expensetracker")

   # Print a success message
   print("Database created sucessfully")
    
except:
   print("Its Already Exists")

 # to insert data in table
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Root@123",
database = 'Expensetracker'

)

   # Create a cursor object
mycursor = mydb.cursor() 
balance = []
balance.append(1000)
mycursor.execute("INSERT INTO wallet(balance) values(%s)",(balance))
mydb.commit()
# # Close the cursor and database connection
while  True:
   print("1.Add Expenses\n,2.Add wallet Amount\n,3.Display Expenses\n,4.Exit")
   choice = int(input("Enter your choices: ")) 
   if choice==1:
      print("Add Expenses")
      xname = input("Enter the Expense:")
      xamnt = int(input("Enter Expense Amount: "))
      mycursor.execute("SELECT *FROM wallet ")
      list1 = mycursor.fetchall()
      bal = list1[-1][-1]
      mycursor.execute("SELECT *FROM expenses")
      explist = mycursor.fetchall()
      if xamnt<=bal:
          flag = 0
          for i in  explist:
               if i[0]==xname:
                   oldval=i[1]
                   newval = oldval+xamnt
                   mycursor.execute("UPDATE expenses SET amount = %s WHERE expname = %s",(newval,xname))
                   mydb.commit()
                   flag = 1
          if flag==0:
             mycursor.execute("INSERT INTO expenses(expname,amount) VALUES (%s,%s)",(xname,xamnt))
      walletbal = bal- xamnt
      walllist = [] 
      walllist.append(walletbal)
      mycursor.execute("INSERT INTO wallet(balance) VALUES (%s)",(walllist))
      print("Expense Added..")
      mydb.commit()
   elif choice==2:
       print("Add Amount to wallet")
       wallamnt = int(input("Enter the wallet Amount:"))
       mycursor.execute("SELECT *FROM wallet")
       walllist=mycursor.fetchall()
       walbal = walllist[-1][-1]
       newwallet=walbal+wallamnt
       newwalllist = []
       newwalllist.append(newwallet)
       mycursor.execute("INSERT INTO wallet(balance) VALUES (%s)",(newwalllist))
       print("Amount added to wallet..")
       mydb.commit()
   elif choice==3:
       mycursor.execute("SELECT *FROM expenses")
       flistexp=mycursor.fetchall()
       for i in flistexp:
         print(i)
   else:
     exit()  

      




                      







   