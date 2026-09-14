import sys, pathlib
root = pathlib.Path(__file__).parent
tokens = (root/'tokens.css').read_text()
head = '''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Fraunces:ital,opsz,wght@0,9..144,300..500;1,9..144,300..500&family=DM+Mono:wght@400;500&display=swap">
<style>
%s
</style>
</helmet>
'''
tail = '''
</x-dc>
</body>
</html>
'''
for frag in sorted(root.glob('*.frag.html')):
    out = root/(frag.name.replace('.frag.html','.dc.html'))
    out.write_text((head % tokens) + frag.read_text() + tail)
    print('built', out.name)
