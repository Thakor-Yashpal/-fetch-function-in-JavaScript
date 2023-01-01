import requests

response = requests.get('https://api.example.com/endpoint')

if response.status_code == 200:
  data = response.json()
  print(data)
else:
  print('An error occurred:', response.status_code)

  
  #o use the Python requests library in a JavaScript file, you can use a library such as pyodide to execute Python code from JavaScript.
  #Alternatively, you can make the HTTP request directly from JavaScript u
  #sing the methods described above.
