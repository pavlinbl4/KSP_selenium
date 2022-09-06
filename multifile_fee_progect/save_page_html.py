from pathlib import Path

report_folder = f'{Path.home()}/Documents/Kommersant/My_report_from_0107'

def save_html_page(report_html):
    with open(f'{report_folder}/source_page.html', 'w') as file:
        file.write(report_html)