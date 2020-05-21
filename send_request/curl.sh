
#!/bin/bash


echo "http://localhost:5001/test1"

curl -X POST \
  http://localhost:5001/test1 \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 66704144-6003-41ad-b4cb-9e97cd353c32' \
  -H 'cache-control: no-cache' \
  -d '{
	"email" : "ilyes@ensi.tn"
}'