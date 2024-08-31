import nbformat
import os 
import pypandoc
import re
import subprocess
import yaml 


def extract_exercises(exercise_folders, output_file, Ex_name):
    # Initialize a list to store extracted cells
    extracted_cells = []
    
    extracted_cells.append(f"# Exercise {Ex_name.replace('Ex','')}")
    extracted_cells.append(f'Student:  Firstname Lastname    Sciper: 000000')
    extracted_cells.append(""":::{admonition} Please use this template to submit your answers. \n
If you had to modify code from the notebook, please include the modified code in your submission either as screenshot or in a \n
```
\\begin{lstlisting}[language=Python]
\\end{lstlisting}
```\n\n
environment. \n
You only need to include the code cells that you modified.\n
Note, that references to other parts of the documents aren't resolved in this template and will show as `??`. Check the text of the exercises on website for the reference

:::""")
    # Get a list of notebook files in the directory
    notebook_files = exercise_folders
    
    for notebook_file in notebook_files:
        with open(os.path.join("iesm", notebook_file), 'r') as f:
            notebook_content = nbformat.read(f, as_version=4)
            
            # Iterate through cells in the notebook
            for cell in notebook_content.cells:
                if cell.cell_type == 'markdown':
                    source = cell['source']
                    if ':::{admonition} Exercise' in source:
                        if 'solution' not in cell.metadata.get('tags', []):
                            # Strip out content outside of the admonition
                            admonition_start = source.index(':::{admonition} Exercise')
                            admonition_end = source.rindex(':::')
                            extracted_cells.append(source[admonition_start:admonition_end+4])
                            extracted_cells.append('Your answer here')
                    if '```{admonition} Exercise' in source:
                        if 'solution' not in cell.metadata.get('tags', []):
                            # Strip out content outside of the admonition
                            admonition_start = source.index('```{admonition} Exercise')
                            admonition_end = source.rindex('```')
                            extracted_cells.append(source[admonition_start:admonition_end+4])
                            extracted_cells.append('Your answer here')
       

    # Write the extracted cells to the output file
    with open(output_file, 'w') as f:
        f.write('\n\n'.join(extracted_cells))
    

    subprocess.call(["myst", "build", output_file,"--tex"])
    tex_file = output_file.replace("_","-").replace('.md', '.tex').lower()
    text_file_noending = tex_file.replace("_","-").replace('.tex', '_tex').lower()
    os.system(f"cp _build/exports/{text_file_noending}/{tex_file} {tex_file}")

    # read in exercise template
    with open(tex_file, 'r') as f:
        exercise_template = f.read()
    #replace everythin before \maketitle with replace text
    replace_text = """\\documentclass{article}
\\usepackage{xcolor}
\\usepackage{amsmath}
\\usepackage{mdframed}
\\usepackage{listings}
\\usepackage{graphicx}
\\usepackage{hyperref}
\\definecolor{codegreen}{rgb}{0,0.6,0}
\\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\\definecolor{codepurple}{rgb}{0.58,0,0.82}
\\definecolor{backcolour}{rgb}{0.95,0.95,0.92}
\\lstdefinestyle{mystyle}{
    backgroundcolor=\\color{backcolour},   
    commentstyle=\\color{codegreen},
    keywordstyle=\\color{magenta},
    numberstyle=\\tiny\\color{codegray},
    stringstyle=\\color{codepurple},
    basicstyle=\\ttfamily\\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}
\\lstset{style=mystyle}
\\title{Exercise """ + Ex_name + """}
\\begin{document}
\\maketitle"""


    exercise_template = exercise_template.replace(exercise_template[:exercise_template.index('\maketitle')], replace_text)

    # replace all occurences of \begin{framed} or \end{framed} with \begin{mdframed} or \end{mdframed}
    exercise_template = exercise_template.replace('\\begin{framed}', '\\begin{mdframed}')
    exercise_template = exercise_template.replace('\\end{framed}', '\\end{mdframed}')


    # remove \printglossaries and \bibliography
    exercise_template = exercise_template.replace('\\printglossaries', '')
    exercise_template = exercise_template.replace('\\bibliography{main.bib}', '')

    # write new exercise template to file
    with open(tex_file, 'w') as f:
        f.write(exercise_template)

    #convert tex to docx
    docx_file = tex_file.replace('.tex', '.docx')
    pypandoc.convert_file(tex_file, 'docx', outputfile=docx_file)
    return output_file, docx_file, tex_file


# Example usage:
# dirs = [ f.path for f in os.scandir("iesm/Exercises") if f.is_dir() ]

# extract notebook files from _toc.yml

# Parse the YAML string
with open('iesm/_toc.yml', 'r') as file:
    parsed_yaml = yaml.safe_load(file)

# Navigate through the parsed YAML structure to extract the file paths
file_paths = {}
for part in parsed_yaml['parts']:
    for chapter in part['chapters']:
        
        if 'sections' not in chapter.keys():
            continue
        key = chapter['file'].split('/')[1]
        file_paths[key] = []
        for section in chapter['sections']:
            if section['file'].endswith(".ipynb"):
                file_paths[key].append(section['file'])

print(file_paths)

output_files = []

for key in file_paths.keys():
    exercise_folders = file_paths[key]
    output_files.extend(extract_exercises(exercise_folders, f'exercise_template_{key}.md', key))

# move outputfiles to template dir
os.system("mkdir -p templates")

for output_file in output_files:
    os.system(f"mv {output_file} templates/")



