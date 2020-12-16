a=12
b=90
c=a+b
print("Content-type:text/html\r\n\r\n")
print(f"""<!DOCTYPE html>
<!--html5 declaration-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h2>Sum of {a} amd {b} = {a+b}</h2>
</body>
</html>""")