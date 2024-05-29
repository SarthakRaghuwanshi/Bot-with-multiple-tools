import random
from bs4 import BeautifulSoup
import requests
import colorama
import pyfiglet
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

comp_wins = 0
player_wins = 0

def weather():
    print("enter the city name")
    city=input("Enter the city name: ")
    city=city+" weather"
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching in google......\n")
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(Fore.BLUE +location)
    print(Fore.BLUE +time)
    print(Fore.BLUE +info)
    print(Fore.BLUE +weather+"°C")

def Playgame(player_wins,comp_wins):
 while True:
    
    user_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")
    
    if user_choice == "r":
        if comp_choice == "r":
            print(Fore.RED + 'You chose rock. The computer chose rock. You tied.')
        
        elif comp_choice == "p":
            print(Fore.RED + 'You chose rock. The computer chose paper. You lose.')
            comp_wins += 1
            
        elif comp_choice == "s":
            print(Fore.RED + 'You chose rock. The computer chose scissors. You win.')
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print(Fore.RED + 'You chose paper. The computer chose rock. You win.')
            player_wins += 1
        
        elif comp_choice == "p":
            print(Fore.RED + 'You chose paper. The computer chose paper. You tied.')
            
            
        elif comp_choice == "s":
            print(Fore.RED + 'You chose paper. The computer chose scissors. You lose.')
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print(Fore.RED + 'You chose scissors. The computer chose rock. You lose.')
            comp_wins += 1
        
        elif comp_choice == "p":
            print(Fore.RED + 'You chose scissors. The computer chose paper. You win.')
            player_wins += 1
            
        elif comp_choice == "s":
            print(Fore.RED + 'You chose scissors. The computer chose scissors. You tied.')

    print("")
    print(Fore.RED + 'Player wins: ' + str(player_wins))
    print(Fore.RED + 'Computer wins: ' + str(comp_wins))
    print("")
    
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

def chatMe(user_name):
 var_1=['hi','hello']
 var_2=['how are you',Fore.LIGHTMAGENTA_EX + 'how are you doing',Fore.LIGHTMAGENTA_EX + 'how is your health']
 var_3=[Fore.LIGHTMAGENTA_EX +'what is your name',Fore.LIGHTMAGENTA_EX + 'how do i call you',Fore.LIGHTMAGENTA_EX + 'name']
 var_4=[Fore.LIGHTMAGENTA_EX +'programming language',Fore.LIGHTMAGENTA_EX + 'what should i learn']
 var_5=[Fore.LIGHTMAGENTA_EX +'what are your hobbies',Fore.LIGHTMAGENTA_EX + 'hobbies',Fore.LIGHTMAGENTA_EX + 'what do you do in your free time']
 var_6=['your introduction','introduction','introduce yourself bot']
 var_7=['hobbies','Hobbies']
 var_8=['world cup football']
 var_9=['world cup cricket']
 var_10=['explain the project']
 var_11=['how are you in hindi']
 var_12=['jokes']
 var_13=['quotes']
 print("\nHello",user_name,"talk with me!!")

 print("\n\t Type exit to Exit chat:\n")
 while True:
     
    
    user_input=input('talk to bot : ')

    if(user_input=="exit"):
            return "Chat  exit..."
    
    elif user_input.lower() in var_1: 
        bot_1=['hello','hi']
        print(Fore.GREEN + ' Bot replied: '+random.choice(bot_1)+'\n')

    elif user_input.lower() in var_2:
        bot_2=['I am good', 'I am doing great','I am fine']
        print(Fore.GREEN + ' Bot replied: ' +random.choice (bot_2)+'\n')

    elif user_input.lower() in var_3:
        bot_3=['My name is ChatterBot', 'call me Chatterbot','chatterbot']
        print(Fore.GREEN + 'Bot replied: '+random.choice(bot_3)+'\n')

    elif user_input.lower() in var_4: 
        bot_4=['python', 'python programming language'] 
        print(Fore.GREEN + ' Bot replied: '+random.choice (bot_4)+'\n')

    elif user_input.lower() in var_5:
        bot_5=['learning a programming language', 'learning a programming language', 'learning a programming language']
        print(Fore.GREEN + ' Bot replied: '+random.choice(bot_5)+'\n')
    elif user_input.lower() in var_6:
        bot_6=[Fore.GREEN + 'HELLO SIR\Maam! I am a Bot hope you liked the above features of me before having a chat I was created using python lang.Thanks for coming','HELLO SIR\Maam! I am a Bot hope you liked the above features of me  before having a chat! I was created using python lang.Thanks for coming' ]
        print(Fore.GREEN + ' Bot replied: '+random.choice(bot_6)+'\n')
    elif user_input.lower() in var_7: 
        bot_7=[Fore.GREEN + 'i like to chat with humans and playing quiz',Fore.GREEN + 'i like to chat with humans and playing quiz'] 
        print(Fore.GREEN + ' Bot replied: '+random.choice (bot_7)+'\n')
    elif user_input.lower() in var_8: 
        bot_8=[Fore.GREEN + '2022-ARGENTINA 2018-FRANCE 2014-GERMANY 2010-SPAIN 2006-ITALY 2002-BRAZIL 1998-FRANCE',Fore.GREEN + '2022-ARGENTINA 2018-FRANCE 2014-GERMANY 2010-SPAIN 2006-ITALY 2002-BRAZIL 1998-FRANCE'] 
        print(Fore.GREEN + ' Bot replied: '+random.choice (bot_8)+'\n')
    elif user_input.lower() in var_9:
        bot_9=[Fore.GREEN + '2007-INDIA 2009-PAKISTAN 2010-ENGLAND 2012-WEST INDIES 2014-SHRILANKA 2016-WEST INDIES 2022-ENGLAND',Fore.GREEN + '2007-INDIA 2009-PAKISTAN 2010-ENGLAND 2012-WEST INDIES 2014-SHRILANKA 2016-WEST INDIES 2022-ENGLAND']
        print(Fore.GREEN + ' Bot replied: '+random.choice(bot_9)+'\n')
    elif user_input.lower() in var_10:
        bot_10=[Fore.GREEN +'FIRST I IMPORTED THREE MODULES -1bs4 2BeautifulSoup 3Requests 4Random then i used dictionaries and a mozilla firefox link for the weather feature then if elif else if conditions dictionaries concatetaion as well as random.choice etc etc for other three the rock paper scissor game the quiz and the bot',Fore.GREEN + 'FIRST I IMPORTED THREE MODULES -1bs4 2BeautifulSoup 3Requests 4Random then i used dictionaries and a mozilla firefox link for the weather feature then if elif else if conditions dictionaries concatetaion as well as random choice etc etc for other three the rock paper scissor game the quiz and the bot']
        print(Fore.GREEN + ' Bot replied: '+random.choice(bot_10)+'\n')
    elif user_input.lower() in var_11: 
        bot_11=[Fore.GREEN + 'नमस्ते मैं ठीक हूं पूछने के लिए धन्यवाद','नमस्ते मैं ठीक हूं पूछने के लिए धन्यवाद'] 
        print(Fore.GREEN + ' Bot replied: '+random.choice (bot_11)+'\n')
    elif user_input.lower() in var_12: 
        bot_12=[Fore.GREEN + 'DID YOU HEARD ABOU THE ACTOR WHO FELL THROUGH THE FLOOR BOARDS?--HE WAS JUST GOING THROUGH THE STAGE',Fore.GREEN + 'DID YOU HEARD ABOU THE ACTOR WHO FELL THROUGH THE FLOOR BOARDS?--HE WAS JUST GOING THROUGH THE STAGE'] 
        print(Fore.GREEN + ' Bot replied: '+random.choice (bot_12)+'\n')
    elif user_input.lower() in var_13: 
        bot_13=[Fore.GREEN + 'Opportunities dont happen, you create them',Fore.GREEN + 'It is never too late to be what you might have been'] 
        print(Fore.GREEN + ' Bot replied: '+random.choice (bot_13)+'\n')
    else:
        print(' Bot replied - Sorry what are you asking,I am not getting that !')

def Playquiz():
    #Answers=["A","D","B","c"]
    print("\n***************************************")
    print(Fore.YELLOW + 'How do you create a variable with the numeric value 5?')
    print("***************************************")
    print("A.b and c are correct\n""B.x = 5\n""C.x = int(5)\n""D.5")
    guess=input("\nOption: ")
    if(guess=="A"or guess=="a"):
        print("\n$$ Bravo!You got it correct $$ ")
    else:
        print("\n$$ Incorrect $$")
    print(Fore.YELLOW + 'What is the correct file extension for Python files?')
    print("***************************************")
    print("A.pp\n""B.pa\n""C.pc\n""D.py")
    guess=input("\nOption: ")
    if(guess=="D"or guess=="d"):
        print("\n$$ Bravo!You got it correct $$ ")
    else:
        print("\n$$ Incorrect $$") 
    print(Fore.YELLOW + 'What is a correct syntax to output Hello World in Python?')
    print("***************************************")
    print("A.print(Hello World)\n""B.p(Hello World)\n""C.echo Hello World\n""D.echo(Hello World);")
    guess=input("\nOption: ")
    if(guess=="A"or guess=="a"):
        print("\n$$ Bravo!You got it correct $$ ")
    else:
        print("\n$$ Incorrect $$")  
    print(Fore.YELLOW + 'How do you insert COMMENTS in Python code??')
    print("***************************************")
    print("A./*This is a comment*/\n""B.//This is a comment\n""C.#This is a comment  \n""D.7")
    guess=input("\nOption: ")
    if(guess=="c"or guess=="C"):
        print("\n$$ Bravo!You got it correct $$ ")
    else:
        print("\n$$ Incorrect $$")  
    print(Fore.YELLOW + 'Which one is NOT a legal variable name?')
    print("***************************************")
    print("A.my_var\n""B.my-var\n""C.Myvar\n""D._myvar")
    guess=input("\nOption: ")
    if(guess=="B"or guess=="b"):
        print("\n$$ Bravo!You got it correct $$ ")
    else:
        print("\n$$ Incorrect $$")
    print(Fore.YELLOW + 'What is the correct syntax to output the type of a variable or object in Python?')
    print("***************************************")
    print("A.print(typeof x)\n""B.print(typeof(x))\n""C.print(type(x))\n""D.print(typeOf(x))")
    guess=input("\nOption: ")
    if(guess=="C"or guess=="c"):
        print("\n$$ Bravo!You got it correct $$ ")
    else:
        print("\n$$ Incorrect $$")       
    print("\nDo you want to play again (y/n)") 
    response=input() 
    if(response=="y") :
        Playquiz()
    else:
        exit    




print("Hello sir!")
print("")
print("What should i call you?")
user_name=input()
print("")
print(Fore.BLUE + '******************************************')
print("Hello",user_name,"Welcome! to the ChatBot")
print(Fore.BLUE + '******************************************')
print("")

print("These are my some Awesome! Features:")
print("")
print(Fore.RED + Back.GREEN + "******************************************")
text = pyfiglet.figlet_format( "1.WEATHER")
print(text)
tex=pyfiglet.figlet_format("2.Play Rock Paper scissor game with me")
print(tex)
te=pyfiglet.figlet_format("3.Chat With Me ")
print(te)
t=pyfiglet.figlet_format("4.PYTHON QY")
print(t)
print(Fore.RED + Back.GREEN + "******************************************")
print("Enter corresponding numbers with features displayed to do so...")

check=True

while True:
 number=int(input())   
 if(number==1):
    weather()

 elif(number==2):
    Playgame(0,0)

 elif(number==3):
   msg= chatMe(user_name)  
   print(msg)

 elif(number==4):
    Playquiz()      

 else:
    print("Please enter correct number:")   
