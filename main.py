from PyHtml import PyHtml
Pyhtml=PyHtml("ko","test")
Pyhtml.SetScript("./script.js")
Pyhtml.SetStyleSheets("./style.css")
PyHtml.AddTag("a","구글",{"herf":"https://google.com"})
PyHtml.CreateHtml()