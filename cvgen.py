from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Cabeçalho vazio
        pass

    def section_title(self, title):
        self.set_font("Arial", 'B', 14)
        self.set_text_color(0, 0, 80)
        self.cell(0, 8, title, ln=True)
        self.ln(2)

    def section_content(self, text):
        self.set_font("Arial", '', 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(4)

# Criar PDF
pdf = PDF()
pdf.add_page()

# Nome
pdf.set_font("Arial", 'B', 18)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, "Fabio H. B. Lopes", ln=True)
pdf.set_font("Arial", '', 12)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 6, "São Paulo - SP", ln=True)
pdf.cell(0, 6, "Email: fabiohblopes3@gmail.com | Tel: (11) 96319-0942", ln=True)
pdf.cell(0, 6, "GitHub: github.com/binexe1113 | LinkedIn: linkedin.com/in/fabio-henrique-baptista-lopes", ln=True)
#pdf.ln(8)

y = pdf.get_y() + 2
pdf.set_line_width(0.25)
pdf.line(10, y, 200, y)
pdf.ln(4)

# Formação Acadêmica
pdf.section_title("Formação Acadêmica")
pdf.section_content("Bacharelado em Engenharia de Computação - Instituto Federal de São Paulo (IFSP) (02/2024 - 12/2028)(Previsão)")


# Habilidades Técnicas
pdf.section_title("Habilidades Técnicas")
pdf.section_content(
    "- Linguagens: Rust, Go, C, C++, Node.js, Python\n"
    "- Desenvolvimento Web: APIs, servidores HTTP, Node.js, Express, Fullstack\n"
    "- Banco de Dados: MySQL, SQL Server, PostgreSQL\n"
    "- Ferramentas e Sistemas: Git/GitHub, Linux (Arch), VSCode, Docker básico,VisualStudio"
)

# Projetos Relevantes
pdf.section_title("Projetos Relevantes")
pdf.section_content(
    "Servidor HTTP 1.1 em Rust:\n"
    "- Desenvolvimento de um servidor web do zero implementando HTTP 1.1\n"
    "- Foco em performance, sockets, multithreading e conexões persistentes\n"
    "- Demonstra conhecimento profundo de protocolos de rede e sistemas de baixo nível\n\n"

    "Gerenciador de Senhas - Passman (Python):\n"
    "- Aplicação CLI com geração e armazenamento de senhas utilizando criptografia\n"
    "- Uso de CSV e bibliotecas criptográficas para manipulação e recuperação segura de credenciais\n\n"

    "CLI em Go:\n"
    "- Criação de uma ferramenta de linha de comando para automação de tarefas\n"
    "- Demonstração de concorrência, flags e manipulação de arquivos\n\n"

    "Web Scraper em Node.js:\n"
    "- Desenvolvimento de um scraper para coletar informações de sites\n"
    "- Uso de request/axios e cheerio para parsing de HTML e extração de dados\n\n"

)

# Objetivo
pdf.section_title("Objetivo")
pdf.section_content(
    "Atuar como Estagiário em Desenvolvimento de Software, aplicando conhecimentos em Rust, Go, C/C++ e Node.js, "
    "com interesse em back-end, sistemas distribuídos e análise de dados."
)

# Idiomas
pdf.section_title("Idiomas")
pdf.section_content("Português (Nativo)\nInglês (FLuente)")

# Salvar PDF
pdf.output("Fabio Henrique Baptista Lopes.pdf")