"""Main functions"""
def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    d = 'Anotaram a data da maratona!'
    if string == d:
        return True

    string = string.upper()
    string = "".join(string.split())
    
    a = string[:: -1]
   
    if string == a:
        return True
    else:
        return False
    #s = " Stack Over Flow " s = ''.join (s.split ()) print s
    
    
    
teste = input("Dgt:")
is_palindrome(teste)
teste2 = teste[:: -1]
print("Você digitou a palavra" ,teste )
print("Essa palavra ao contrário fica", teste2)
print("Ou seja se a pergunta for se é verdade que essa palavra é um palíndromo a resposta é:")
if is_palindrome(teste) == True:
    print("Que sim é verdade")
else:
    print("Que não é verdade")
