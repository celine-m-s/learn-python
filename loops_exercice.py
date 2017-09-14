################
# Exercice sur les boucles et listes
################
#
# 1) Completez la fonction fib() pour qu'elle retourne les 25 premiers nombres de la suite de fibonacci avec "while"
#
# 2) Completez la fonction fib() pour qu'elle retourne les 25 premiers nombres de la suite de fibonacci avec "for"
#
# 3) Completez la fonction search_dic() afin qu'elle recherche l'index de la valeur 17711 par dichotomie


# With loop "while" :
def fib():
    i = 0
    list = [0, 1]
    # remplacez moi ! :)
    return list


# With loop "for" :
def fib2():
    list = [0, 1]
    # remplacez moi ! :)
    return list


# Fonction dichotomous research
def search_dic(numb, short_list):
    start = 0
    end = len(short_list) - 1
    middle = (start + end) / 2
    # remplacez moi ! :)
    return start


# Fibonacci List with loop "while" :
fibonacciList = fib()
# Fibonacci List with loop "for" :
fibonacciList2 = fib2()


# Displaying the top 25 values :
print("List of 25 first Fibonacci Number with loop while :")
print(fibonacciList)
print("List of 25 first Fibonacci Number with loop for :")
print(fibonacciList2)

# Displaying the index of the number 17711 :
index = search_dic(17711, fibonacciList)
print("Index of 17711 Number:", (index + 1))


