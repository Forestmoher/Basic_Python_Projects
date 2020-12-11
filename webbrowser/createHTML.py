import webbrowser as wb

webpage = open("index.html","x")
webpage.write("""<html> 
                     <body> 
                        <h1>
                          Stay tuned for our amazing summer sale! 
                       </h1>
                     </body> 
                </html> """)
webpage.close()


wb.open("index.html")
