import re

def format_markdown(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    formatted_lines = []
    for line in lines:
        # Add ### before titles like 4.2, 4.3
        if re.match(r'^\d+\.\d+\s', line):
            formatted_lines.append(f"### {line.strip()}\n")
        # Add #### before subtitles like Depth of Coverage, Practical Exercises, Additional Resources
        elif re.match(r'^Depth of Coverage:|Practical Exercises:|Additional Resources:', line):
            formatted_lines.append(f"#### {line.strip()}\n")
        # Add - before list items under subtitles
        elif not line.startswith('###') and not line.startswith('####') and line.strip():
            formatted_lines.append(f"- {line.strip()}\n")
        else:
            formatted_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(formatted_lines)

# Replace 'path_to_your_markdown_file.md' with the actual path to your Markdown file
format_markdown('advanced-syllabus.md')