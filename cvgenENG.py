from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Empty header
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

# Create PDF
pdf = PDF()
pdf.add_page()

# Name
pdf.set_font("Arial", 'B', 18)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, "Fabio H. B. Lopes", ln=True)
pdf.set_font("Arial", '', 12)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 6, "São Paulo - SP", ln=True)
pdf.cell(0, 6, "Email: fabiohblopes3@gmail.com | Tel: (11) 96319-0942", ln=True)
pdf.cell(0, 6, "GitHub: github.com/binexe1113 | LinkedIn: linkedin.com/in/fabio-henrique-baptista-lopes", ln=True)

y = pdf.get_y() + 2
pdf.set_line_width(0.25)
pdf.line(10, y, 200, y)
pdf.ln(4)

# Education
pdf.section_title("Education")
pdf.section_content("Bachelor in Computer Engineering - Federal Institute of São Paulo (IFSP) (02/2024 - 12/2028)(Expected)")

# Technical Skills
pdf.section_title("Technical Skills")
pdf.section_content(
    "- Languages: Rust, Go, C, C++, Node.js, Python\n"
    "- Web Development: APIs, HTTP servers, Node.js, Express, Fullstack\n"
    "- Databases: MySQL, SQL Server, PostgreSQL\n"
    "- Tools & Systems: Git/GitHub, Linux (Arch), VSCode, Docker basics, VisualStudio"
)

# Relevant Projects
pdf.section_title("Relevant Projects")
pdf.section_content(
    "HTTP 1.1 Server in Rust:\n"
    "- Development of a web server from scratch implementing HTTP 1.1\n"
    "- Focus on performance, sockets, multithreading, and persistent connections\n"
    "- Demonstrates deep knowledge of network protocols and low-level systems\n\n"

    "Password Manager - Passman (Python):\n"
    "- CLI application for generating and storing passwords using encryption\n"
    "- Uses CSV and cryptography libraries for secure manipulation and retrieval of credentials\n\n"

    "CLI in Go:\n"
    "- Created a command-line tool for task automation\n"
    "- Demonstrates concurrency, flags, and file manipulation\n\n"

    "Web Scraper in Node.js:\n"
    "- Developed a scraper to collect information from websites\n"
    "- Uses request/axios and cheerio for HTML parsing and data extraction\n\n"
)

# Objective
pdf.section_title("Objective")
pdf.section_content(
    "Work as a Software Development Intern, applying knowledge in Rust, Go, C/C++, and Node.js, "
    "with interest in back-end, distributed systems, and data analysis."
)

# Languages
pdf.section_title("Languages")
pdf.section_content("Portuguese (Native)\nEnglish (Fluent)")

# Save PDF
pdf.output("Fabio Henrique Baptista Lopes - ENG.pdf")
