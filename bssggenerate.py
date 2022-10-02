from functools import cache
import markdown
import glob
import os
import re

pages = []

class Page:
    title: str      # Title of the page
    content: str    # Markdown file name in content/ folder for page content.
    file: str       # File to save the generated HTML to in the generated-site/ folder.
    template: str   # File containing page template.
    
    def __init__(self, title, content, file, template):
        self.title = title
        self.content = content
        self.file = file
        self.template = template


@cache
def file_compile_markdown(file_name):
    f = open(file_name, 'r')
    contents = f.read()
    f.close()
    return markdown.markdown(contents)

def change_setting(page, setting, new_value):
    page_num = pages.index(page)
    if setting == "title":
        page.title = new_value
    elif setting == "template":
        page.template = new_value
    pages[page_num] = page

def make_missing_dirs(file_name: str):
    file_path_l = file_name.split("/")
    if len(file_path_l) <= 1: return
    file_path_l.pop()
    file_path = "/".join(file_path_l)
    if os.path.exists("generated-site/" + file_path): return
    os.makedirs("generated-site/" + file_path)

@cache
def generate_page(page):
    page_num = pages.index(page)
    make_missing_dirs(page.file)
    f = open("generated-site/" + page.file, 'w')
    page_content_f = open(page.content, 'r')
    page_content = page_content_f.read()
    page_content_f.close()

    # set options
    curly_braces = re.findall(r'\{.*?\}', page_content)
    for inst in curly_braces:
        data: str = inst
        data = data.strip('{}')
        if data.startswith("option:"):
            data = data[7:]
            data = data.split('=')
            change_setting(page, data[0], data[1])
            page_content = page_content.replace(inst, '', 1)
        elif data.startswith("option!"):
            page_content = page_content.replace(inst, inst.replace("!", ":"), 1)
    
    page_content = markdown.markdown(page_content)
    
    # reload page data
    page = pages[page_num]

    template = open("templates/" + page.template + ".html", 'r')
    contents = template.read()

    # substitutions
    curly_braces = re.findall(r'\{.*?\}', contents)
    for inst in curly_braces:
        data: str = inst
        data = data.strip('{}')
        if data.startswith("subst:"):
            data = data[6:]
            if data == "title":
                contents = contents.replace(inst, page.title, 1)
            elif data == "content":
                contents = contents.replace(inst, page_content, 1)
            else:
                contents = contents.replace(inst, file_compile_markdown("content/" + data + ".md"), 1)
    
    # no subst
    curly_braces = re.findall(r'\{subst!.*?\}', contents)
    for inst in curly_braces:
        contents = contents.replace(inst, inst.replace("!", ":"), 1)

    f.write(contents)
    f.close()
    template.close()

def auto_page_title(file_name):
    page_name = os.path.splitext(file_name)[0]
    page_name = page_name.split("/")[-1]
    page_name = page_name.split("\\")[-1]
    page_name = page_name.replace("_", ' ')
    page_name = page_name.title()
    return page_name


def auto_file_name(input_file_name):
    file_name: str = os.path.splitext(input_file_name)[0]
    file_name = file_name.replace("\\", "/")
    file_name = file_name.split("/")
    file_name_list = list(reversed(file_name))
    file_name: list = []
    i = 0
    while True:
        if file_name_list[i] == "content":
            break
        file_name.append(file_name_list[i])
        i += 1
    file_name = list(reversed(file_name))
    file_name: str = "/".join(file_name)
    return file_name + ".html"


def main():
    if not os.path.isdir("./generated-site"): os.mkdir('./generated-site')
    if not os.path.isdir("./templates"): os.mkdir('./templates')
    if not os.path.isdir("./content"): os.mkdir('./content')

    markdown_files = glob.glob('content/**/*.md', recursive=True)
    
    for md in markdown_files:
        page_name = auto_page_title(md)
        file_name = auto_file_name(md)
        if file_name[0] == "_":
            continue    # Special reserved _ file name. will not render
        pages.append(Page(title=page_name, content=md, file=file_name, template='template'))

    for page in pages:
        generate_page(page)

if __name__ == "__main__":
    main()
