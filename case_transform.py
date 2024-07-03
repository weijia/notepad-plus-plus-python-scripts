txt = editor.getText()
if txt.isupper():
    editor.setText(txt.lower())
else:
    editor.setText(txt.upper())
