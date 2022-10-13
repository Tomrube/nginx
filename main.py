from flask import Flask

app = Flask(__name__)




@app.route('/')
@app.route('/hello')
@app.route('/hi')
def main():
    """Return an HTML-formatted string and an optional response status code"""
    return """
      <!DOCTYPE html>
      <html>
      <head>
      <style>
      Body {
      background-color: linen;
      }
      h1{
      color: maroon;
      text-align: center;
      text-size: 90px;
      }
      h2 {
      color: black;
      text-align-last: right;
      text-size: 90px;
      }
      
      </style> 
      
      <title>Hello</title></head>
      <body><h1>Hello World!</h1>
      <h2 id="displayDateTime"></h2>
      <script type="text/javascript">
      var today = new Date();
      var day = today.getDay();
      var daylist = ["Sunday","Monday","Tuesday","Wednesday ","Thursday","Friday","Saturday"];
      var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
      var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
      var dateTime = date+' '+time;
       
      document.getElementById("displayDateTime").innerHTML = dateTime + ' <br> Day :- ' + daylist[day];
     
      </script>
   
      </body>
      </html>
      """
