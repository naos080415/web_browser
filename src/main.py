import os
home_dir = os.getenv("HOME")
import_file_path = home_dir + "/web_browser/sample_html/simple.html"
f = open(import_file_path, 'r')
data = f.read()
f.close()

print(data)
