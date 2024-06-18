# puter-plugins
 plugins for puter that runs on your computer

 each plugin is a nodejs http local server that runs on your computer on localhost:3000
 It allow communication between your computer and puter




for each plugin  :

```sh
npm install
node server.js
```




## Python plugin

runs python script on your computer with http and return the result: 

```sh
curl -X POST http://localhost:3000/run-python -H "Content-Type: application/json" -d '{"code": "print(\"Hello, World!\")"}'
```


## ssh plugin

runs ssh command on your computer and return the result:

```sh
curl -X POST http://localhost:3000/run-command -H "Content-Type: application/json" -d '{"command": "ls"}'
```

## OpenAiProxy Plugin

a simple proxy for open ai chat streamining
need export your OPENAI_API_KEY

```sh
curl -X POST http://localhost:3000/stream \                                                                                                                      ─╯
-H "Content-Type: application/json" \
-d '{
  "chatOptions": {
    "model": "gpt-4o",
    "messages": [
      { "role": "system", "content": "You are a helpful assistant" },
      { "role": "user", "content": "Hello!" }
    ],
    "stream": true
  }
}'

```

every functionalities will be added


## AnthropicProxy Plugin

a simple proxy for anthropic chat streamining
need export your ANTHROPIC_API_KEY


## Local File Server Plugin

a simple readDir and readFile http server




## Todos

[ ] add bearer auth
[ ] puter-app samples
[ ] add security and blacklist
[ ] add more functionalities to existing plugins
[ ] make more plugins






 
