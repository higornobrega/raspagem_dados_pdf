# importa as bibliotecas necessárias
import PyPDF2
import re

# Abre o arquivo pdf 
# lembre-se que para o windows você deve usar essa barra -> / 
# lembre-se também que você precisa colocar o caminho absoluto
pdf_file = open('PATH_TO_YOUR_FILE/holerite1.pdf', 'rb')

#Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# pega o numero de páginas
number_of_pages = read_pdf.getNumPages()

#lê a primeira página completa
page = read_pdf.getPage(0)

#extrai apenas o texto
page_content = page.extractText()

# faz a junção das linhas 
parsed = ''.join(page_content)

print("Sem eliminar as quebras")
print(parsed)

# remove as quebras de linha
parsed = parsed.rstrip('\n')
print("Após eliminar as quebras")
print(parsed)

print("nPegando apenas as 20 primeiras posições")
novastring = parsed[0:20]
print(novastring)