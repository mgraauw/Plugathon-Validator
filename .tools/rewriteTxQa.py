if __name__ == "__main__":
    with open("output/qa-tx.html", "r") as f:
        content = f.readlines()
    
    output = """
<!DOCTYPE HTML>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <script defer src="assets/script/pretty-json-custom-element/index.js"></script>
</head>
<body>
"""

    for line in content:
        line = line.replace("&quot;", '"')
        if line.startswith('{"resourceType":"Parameters"') or line.startswith('{"resourceType" : "Parameters"'):
            output += "\n</pre>\n"
            output += "<pretty-json expand='3'>\n"
            output += line
            output += "\n</pretty-json>\n"
        if line.startswith('{'):
            output += "\n</pre>\n"
            output += "<pretty-json>\n"
            output += line
            output += "\n</pretty-json>\n"
        elif line.startswith("</pre>"):
            pass
        else:
            output += line

    output += "\n</body>\n</html>"
    with open("output/qa-tx.html", "w") as f:
        f.write(output)