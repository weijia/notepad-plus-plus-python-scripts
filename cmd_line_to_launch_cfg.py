import json
txt = editor.getText()
v = txt.split(" ")
editor.setText(json.dumps(v))
