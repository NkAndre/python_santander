condicao = True
def function():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception('Descrição do erro')

try:
    function()
except Exception as e:
    print(f"Erro: {str(e)}")