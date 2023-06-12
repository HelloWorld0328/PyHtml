from PyHtml import PyHtml
Pyhtm=PyHtml()
Pyhtm.SetHtml("ko","Hello")
Pyhtm.SetJavaScript("./script.js")
Pyhtm.SetStyleSheets("./style.css")
Pyhtm.SetPyScript()
Pyhtm.AddTag("a","test",{"herf":"https://www.google.com"})
Pyhtm.CreateHtml("./index.html")