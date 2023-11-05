
trabalho_laboratorio = float(
    input("Digite a nota do trabalho de laboratório: "))
avaliacao_semestral = float(input("Digite a nota da avaliação semestral: "))
exame_final = float(input("Digite a nota do exame final: "))

media = ((trabalho_laboratorio * 2) +
         (avaliacao_semestral * 3) + (exame_final * 5)) / 10

if 0 > trabalho_laboratorio > 10 or 0 > avaliacao_semestral > 10 or 0 > exame_final > 10:
    print("Alguma nota foi digitada incorretamente. Por favor, reveja as notas informadas.")

if 0 <= media = > 2.9:
    print(f"Você foi reprovado. Sua média foi {media:.2f}.")
elif 3 <= media = > 4.9:
    print(f"Você está de recuperação. Sua média foi {media:.2f}.")
elif 5 <= media = > 10:
    print(f"Você foi aprovado. Sua média foi {media:.2f}.")
