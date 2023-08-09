#program
#Author : Harindu Adhikari
#Date : 12/3/2022
isRetry ="Y"
while isRetry == "Y":

    code_breaker_name = input("What is your name:") #This is my varibale for player name
    txt = "Hi " + code_breaker_name + " Welcome to GameInt"
    print(txt.center(75))
    print(f"{'Number to Guess- X X X X' : <40}{'Color Mapping:': >20}")
    print(f"{'':<52}{'1-White 2-Blue 3-Red':>15}")
    print(f"{'':<52}{'4-Yellow 5-Green 6-Purple':>15}")
    print("-"*100)
    print("INSTRUCTIONS\n Enter a 4 digit code within 1 to 6 number range. \n e.g. If you enter 7890, that number is invalid. But 6251 is a valid number.\n Enter 0000 to end the game")
    print("We wil give you 8 attempts to guess and win")
    print("-"*75)
    txt1 = '\u0332'.join('Attempts ')
    txt2 = '\u0332'.join('Guess ')
    txt3 = '\u0332'.join('Result ')
    print(f"{txt1:<20}{txt2:^30}{txt3:>10}")

#My variable section------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    attempts = 1
    smallerpeg1 ="-"
    smallerpeg2 ="-"
    smallerpeg3 ="-"
    smallerpeg4 ="-"
    is_won = 0
    is_exit = 0
#My gameint code_maker random number area -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    import random    #import module called random to genarate random number
    code_maker_random_no  = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
        #Reason for above line is to generate individual letters within 1 to 6.

    code_maker_random_number_list = []
    for letter in  code_maker_random_no:
        code_maker_random_number_list.append(letter)
        

#End of my gameint code_maker random number area -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#My gameint code_breaker / player guess area for 8 times -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    while attempts <=8:
      code_breaker_attempt_no = input(f'{attempts:<21}')

      if (code_breaker_attempt_no =="0000"):
          attempts=9
          is_exit=1
          print("Thank you. :) for your participate")
      else:
          player_number_list = [] 
          for letter in  code_breaker_attempt_no:
              player_number_list.append(letter)

          #print(code_maker_random_number_list[0])
          #print(player_number_list[0])
              
#End of my gameint code_breaker / player guess area for 8 times ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Check--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          if(int(code_maker_random_number_list[0]) ==int( player_number_list[0])):
              smallerpeg1 = 1
          else:
              if(int(code_maker_random_number_list[1]) ==int( player_number_list[0]) or int(code_maker_random_number_list[2]) ==int( player_number_list[0]) or int(code_maker_random_number_list[3]) ==int( player_number_list[0])):
                  smallerpeg1 = 0
              else:
                  smallerpeg1 ="-"
              
          if(int(code_maker_random_number_list[1]) ==int( player_number_list[1])):
              smallerpeg2 = 1
          else:
              if(int(code_maker_random_number_list[0]) ==int( player_number_list[1]) or int(code_maker_random_number_list[2]) ==int( player_number_list[1]) or int(code_maker_random_number_list[3]) ==int( player_number_list[1])):
                  smallerpeg2 = 0
              else:
                  smallerpeg2 = "-"

          if(int(code_maker_random_number_list[2]) ==int( player_number_list[2])):
              smallerpeg3 = 1
          else:
              if(int(code_maker_random_number_list[0]) ==int( player_number_list[2]) or int(code_maker_random_number_list[1]) ==int( player_number_list[2]) or int(code_maker_random_number_list[3]) ==int( player_number_list[2])):
                  smallerpeg3 = 0
              else:
                  smallerpeg3 = "-"

          if(int(code_maker_random_number_list[3]) ==int( player_number_list[3])):
              smallerpeg4 = 1
          else:
              if(int(code_maker_random_number_list[0]) ==int( player_number_list[3]) or int(code_maker_random_number_list[1]) ==int( player_number_list[3]) or int(code_maker_random_number_list[2]) ==int( player_number_list[3])):
                  smallerpeg4 = 0
              else:
                  smallerpeg4 = "-"
              
         # print(f'{attempts:<20}', f'{code_breaker_attempt_no:<20}', smallerpeg1,smallerpeg2)
          print(f"{smallerpeg1:>39}", smallerpeg2 )
          print(f"{smallerpeg3:>39}", smallerpeg4 )

          
          attempts += 1
          print("-"*75)
          
          if (smallerpeg1 != '-' and smallerpeg2 != '-' and smallerpeg3 != '-' and smallerpeg4 != '-'):
             if(int(smallerpeg1)==1 and int(smallerpeg2)==1 and int(smallerpeg3)==1 and int(smallerpeg4)==1):
               is_won=1
            
          if(is_won == 1):
             print("Congratulations!! You won the game")
             attempts= 9

    print("The Secret Code is:",code_maker_random_number_list)
    if (attempts > 8 and is_exit == 0):
        print(" Ooh !, Your chances are finished :(")
    isRetry = input("Do you want to try again? Y-Yes N-No:")
    print("Thank you:) for your participation.")
