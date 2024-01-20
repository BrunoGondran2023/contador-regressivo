# Programa para disparar um alarme.

status_porta = "aberta"
status_janela = "aberta"

# status = porta_fechada + janela_fechada

if status_porta == "fechada" and status_janela == "fechada":
    print("Casa segura, porta e janela fechadas!")
elif status_porta == "aberta" and status_janela == "aberta":
    print("Porta e janela abertas, alarme disparado!")
elif status_porta == "aberta":
    print("Porta aberta, alarme disparado!")
    print("Janela fechada.")
elif status_janela == "aberta":
    print("Janela aberta, alarme disparado!")
    print("Porta fechada!")
else:
    print("Situação não prevista. Verifique o sistema de alarme.")
