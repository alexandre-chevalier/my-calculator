
## fonction qui fait le calcul et retourne le resultat##
def calculator(n1, si, n2):
    if si == "+":
        result = n1 + n2
        return result
    elif si == "-":
        result = n1 - n2
        return result
    elif si == "/":
        result = n1 / n2
        return result
    elif si == "*":
        result = n1 * n2
        return result
    elif si == "%":
        result  = n1 % n2
        return result

## function who display the result ##
def display_result(result):
    print(f"here is your result : {result}")

## function print a message when the wrong sign is enter ##
def error():
        print("you enter the wrong sign, please enter the right sign")
        
## fonction qui retorune les nombre au format int ou float en fonction du coix de l'utilisateur ##
def number(Fl_Int):
    if Fl_Int == "float":
        while True:
            try:
                number1 = float(input("enter the 1st number : "))
                number2 = float(input("enter the 2nd number : "))
                return number1, number2
                break
            except ValueError:
                print("veuillez entrez le bon caractere")
    elif Fl_Int == "int":
        while True:
            try:
                number1 = int(input("enter the 1st number : "))
                number2 = int(input("enter the 2nd number : "))
                return number1, number2
                break
            except ValueError:
                print("enter an integer")


        

## fonction qui gere l'historique des operations ##
def history(hystorique, num1, si, num2, res):
    
    his = f"{num1} {si} {num2} = {res}"
    hystorique.append(his)
    print("here is your calculator history")

    for i in range(len(hystorique)):
        print(i, hystorique[i])
    return hystorique

def remove(histori):
    while True:
        try:
            deleted = int(input(f" your calculator history contain {len(histori)} value, chose the value you want to delete between 0 and {len(histori) - 1} :  " ))
            del histori[deleted]
            print(histori)
            break
        except ValueError:
            print("enter the correct number")
        except IndexError:
            print("enter the correct index number you want to delete )")
       

def reset(history):
    print(f"before clear {history}")
    history.clear()
    print(f"after clear {history}")

 
def main():
    historik = []
    while True:
        fl_int= input("choose between int and float : int/float  ")
        sign = input("enter th sign you want + - / * % : ")
        
        if sign != "+" and sign != "-" and sign != "*" and sign != "/" and sign != "%":
            error()    
        else:
            num = number(fl_int)
            calcul =  calculator(num[0], sign, num[1])
            print(calcul)
            display_result(calcul)
            
            choice1 = input("do you want to see your calculator history ? Y/N : ").upper()
            if choice1 == "Y":
                histori = history(historik, num[0], sign, num[1], calcul)
            
            choice2 = input("do you want to delete an element of your calculator history ? Y/N").upper()
            if choice2 == "Y":
                remove(histori)
            
            choice3 = input("do you want to delete all your calculator history ? Y/N").upper()
            if choice3 == "Y":
                reset(histori)
            
            choice4 = input("do you want to stop the use of your calculator ? Y/N : ").upper()
            if choice4 == "Y":
                break




main()