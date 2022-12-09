from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

projeto = input("Digite o nome do projeto: ")
horas_estimadas = input("Quantas horas serão necessárias: ")
valor_hora = input("Informe o valor da hora trabalhada: ")
prazo = input("Informe o prazo: ")
valor_total = int(horas_estimadas) * int(valor_hora)



pdf.image("template.png", x=0, y=0)
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso")