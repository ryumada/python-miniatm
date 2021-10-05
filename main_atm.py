import random
import datetime
from customer import Customer

# Object Instance
atm = Customer('Rizuki')

# looping checker
while(True):
  print('# ------------------------- <{ Welcome to ryu ATM }> ------------------------- #')
  pin = int(input('Please input your pin: '))
  attempts = 0

  # looping verification
  while(pin != int(atm.checkPin()) and attempts < 3):
    pin = int(input('Your pin is wrong, please try again: '))
    attempts += 1

    # if attempts had reached the limit, show an error message
    if(attempts == 3):
      print('Your account had locked, please take the card and then contact our Customer Service at 170017.')
      exit()
  
  # menu ATM
  while(True):
    print(f'\n------------------- <( Welcome {str(atm.checkId())} )> -------------------')
    print('Menu:\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Change Pin\n5. Exit')
    selected_menu = int(input('Type the number to continue: \n'))
    print('') # kasih jarak

    # ---------------------------- Check Balance menu ---------------------------- #
    if selected_menu == 1:
      print(f'Your Balance: Rp. {str(atm.checkBalance())}')
    
    # ------------------------------ Withdrawal menu ----------------------------- #
    elif selected_menu == 2:
      withdrawal = int(input('How much do you want to withdraw: '))

      verify_withdrawal = input(f'Are you sure want to withdraw Rp. {str(withdrawal)}? (y/n)\n')
      if(verify_withdrawal == 'y'):
        print('Checking your balance...')
      else: 
        print('Okay, got it.')
        break # break while loop to enter pin screen (break menu screen loop)

      if(withdrawal < atm.checkBalance()):
        atm.withdrawBalance(withdrawal)
        print('Withdrawal complete, please take your money.')
      else:
        print('Sorry, your balance is insufficient.')

      print(f'Your Current Balance: {str(atm.checkBalance())}')

    # ------------------------------- deposit menu ------------------------------- #
    elif selected_menu == 3:
      deposit = int(input('How much do you want to deposit: '))
      
      verify_deposit = input(f'Are you sure want to deposit Rp. {str(deposit)}? (y/n)\n')
      if(verify_deposit == 'y'):
        print('Updating your balance...')
      else:
        print('Okay, got it.')
        break # break while loop to enter pin screen (break menu screen loop)

      atm.depositBalance(deposit)
      print(f'Your Current Balance: {str(atm.checkBalance())}')

    # ------------------------------ Change pin menu ----------------------------- #
    elif selected_menu == 4:
      old_pin = int(input('Enter your current pin: '))
      if(old_pin == atm.checkPin()):
        new_pin = int(input('Enter new pin: '))

        verify_new_pin = int(input('Enter your new pin once again: '))
        if(new_pin == verify_new_pin):
          print('Updating your pin to the new one...')
          atm.updatePin(new_pin)

          print('Your pin had changed.')
        else:
          print('The pin you had entered was not the same as the first one.')
      else:
        print('The current pin you have entered was wrong.')      
      
    # --------------------------------- Exit menu -------------------------------- #
    elif selected_menu == 5:
      print('Printing the receipt...')

      print('~~~~~~~~~~~~~~~~~ ryu ATM ~~~~~~~~~~~~~~~\n')
      print(f'Ref: {random.randint(100000, 1000000)}')
      print(f'Date: {datetime.datetime.now()}')
      print(f'Your Current Balance:\n {str(atm.checkBalance())}')
      print('\nThank you for using ryu ATM.')
      print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

      print('Please take your card.')
      print('Thank you :)')
      exit()

    # ------------------ If the number of menu entered was wrong ----------------- #
    else:
      print('The menu you have entered was not valid, please try again.')  
    
    # after this will show the menu screen
    


