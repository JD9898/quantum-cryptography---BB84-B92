##usage

All responses will have the form

```json
{
	"data": "Mixed type holding the content of the response",
	"mesage": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the 'data field'

###list all containers

**Definition**

`GET /containers`

**Response**

- '200 OK' on success
```json
[
	{
		"indentifier": "container_1",
		"name": "Container",
		"object_type": "check",
		"controller_gateway": "100.000.0.0"
	},
	{
		"indentifier": "container_2",
		"name": "Container",
		"object_type": "check",
		"controller_gateway": "100.000.0.1"
	},
]
```

### Registering a new container

**Definition**

`POST/ containers`

**Arguments**

- `"indentifier":string` a globally unique identifier for this container
- `"name":string` a friendly name for this container
- `"object_type":string` the type of the containers as understood by the client
- `"controller_gateway":string`the IP address of the container's controller

If a container with the given identifier exists, the existing container will be overwritten. 

**Response**

- `201 Created` on success

```json
{
	"indentifier": "container_1",
	"name": "Container",
	"object_type": "check",
	"controller_gateway": "100.000.0.0"
}
```

### Looking up container details

`GET /container/<identifier>`

**Response**

- `404 Not Found` if the container does not exist
- `200 OK` on success

```json
{
	"indentifier": "container_1",
	"name": "Container",
	"object_type": "check",
	"controller_gateway": "100.000.0.0"
}
```
## Delete a container

**Definition**

`DELETE /container/<identifier>

- `404 Not Found` if the container does not exist
- `204 No content` on success

