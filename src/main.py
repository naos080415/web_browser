from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


home_dir = os.getenv("HOME")
import_file_path = home_dir + "/web_browser/sample_html/simple.html"
f = open(import_file_path, 'r')
data = f.read()
f.close()

parser = MyHTMLParser()

print("*** 元のデータ ***")
print(data)
print("*** パース後のデータ ***")
parser.feed(data)
