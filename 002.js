fetch('https://api.example.com/endpoint')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error))

To make an HTTP request from Python, you can use the requests library. Here is an example of how to use requests to make a GET request:
