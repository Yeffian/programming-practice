def validate_hello(greetings):
    hallos = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    
    for hallo in hallos:
        if hallo in greetings.lower():
            return True
    
    return False