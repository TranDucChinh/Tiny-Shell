import webbrowser

def search_google(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open_new_tab(url)

search_google("Python programming language")