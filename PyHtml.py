class PyHtml:
    def __init__(self,lang,title):
        """
            Set the name, language and title of the website file of the website.
            
            lang: Sets the language of html.
            title : set the title of the website
        """
        self.lang=lang
        self.title=title
        self.head=['<!DOCTYPE html>',
            f'<html lang="{self.lang}">',
            '\t<head>',
            '\t\t<meta charset="UTF-8">',
            '\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            f'\t\t<title>{self.title}</title>',
            '\t</head>'
        ]
        self.body=[
            '\t<body>',
            '\t</body>',
            '</html>'
        ]
        self.tags=[]
        self.html=self.head+self.body
        
    def CreateHtml(self,htmlname):
        """Convert to html file."""
        self.html1=self.head.extend(self.body)
        self.html1 = "\n".join(str(item) for item in self.html)
        with open(htmlname,"w") as f:
            f.write(self.html1)
            
    def UpdateHtml(self):
        self.html=self.head+self.body.insert(1,self.tags)
    
    def SetScript(self,script):
        """Set JavaScript (or TypeScript) to use for your website"""
        self.body.insert(1, '\t\t<script src="{}"></script>'.format(script))
        self.UpdateHtml()
    
    def SetStyleSheets(self,stylesheets):
        """Set Css to use for your website"""
        self.head.insert(5,'\t\t<link rel="stylesheet" type="text/css" href="{}">'.format(stylesheets))
        self.UpdateHtml()
    def AddTag(self,name,value,attributes):
        """
        Ability to create a tag by entering the name and attributes of the tag

        value: Gets the value of the tag.
        name : Gets the name of the tag.
        attributes: Get attribute names and values as dictionary values.
        """
        attribute_string = ""
        for key, value in attributes.items():
            attribute_string += f' {key}="{value}"'
        
        html_tag = f"<{name}{attribute_string}></{name}>"
        self.tags.append(html_tag)
        self.UpdateHtml()

