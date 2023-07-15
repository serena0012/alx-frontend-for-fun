import sys
import os.path

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    sys.stderr.write("Missing " + input_file + "\n")
    sys.exit(1)

# Process the Markdown file and convert it to HTML

sys.exit(0)
