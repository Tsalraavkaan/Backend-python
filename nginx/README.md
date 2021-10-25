# Nginx web server

## Setting up server
### Download nginx

`$ sudo apt install nginx`

### Copy server.conf
Before this in location /static/ change path to public on yours
`
$ cp server.conf /etc/nginx/conf.d/server.conf
`

## Run server

### Start nginx
`sudo /etc/init.d/nginx start`

### Open static files in folder via browser or console
`127.0.0.1:8088/static/index.html/`

### Activate virtual environment and install requirements
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Start gunicorn
`$ gunicorn --workers 4 app:app`

### Send request via browser or console
`127.0.0.1:8000/aaa/bb?c=11&d=17`

### Test server
'ab -c 4 -n 5000 http://127.0.0.1:8000/api/aaaa'