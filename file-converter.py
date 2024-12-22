import markdown
import sys

command = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

if command == "markdown":
    try:
        with open(input_file, mode='r') as f:
            md_text= f.read()
    except:
        sys.stderr("inputファイルが見つかりません")
        sys.stderr.flush()

    with open(output_file, mode='w') as f:
        html_output = markdown.markdown(md_text, extensions=["toc", "codehilite", "sane_lists", "extra"])
        f.write(html_output)

else:
    sys.stderr("markdownコマンドのみ入力可能です")
    sys.stderr.flush()