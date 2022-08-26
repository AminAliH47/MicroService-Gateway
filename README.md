<div align="center">

# MicroService Project
### _Gateway service_

<hr>
</div>

In this service, you can Create, Retrieve, Update, and Delete users
by using the Rest Full API request to the service.

**Gateway service** connect to **Users service** with **gRPC**,
It receives the data from the user service.

## ⚠ Important ⚠
To send and get users datas, the Users service must be active.

[Users Service](https://github.com/AminAliH47/MicroService-Users)

<hr>

## 🏁 Run the service
**Gateway service is dockerized.** 
This means that the running of the project is very simple.

⚠ Naturally, Docker must be installed on your system. [Install docker](https://docs.docker.com/get-docker/)

<br>

⚠ If you haven't already run the Users service, run this command in your terminal.
to create and config _users_network_ in Docker.
```commandline
$ docker network create users_network -d bridge --gateway 10.5.0.1 --subnet 10.5.0.0/16
```

Then run this command in the main root of project:

linux/macOS:
```commandline
$ docker-compose up --build -d
```

after that you can open [10.5.0.1:8041](http://10.5.0.1:8041/) URL 
and use the Gateway service.

also you can test APIs with **Swagger UI** docs in [10.5.0.1:8041/docs/](http://10.5.0.1:8041/docs/) URL

<hr>

## ✅ Use the project
Now you can use and test Gateway service. 
But don't forget to Run [Users Service](https://github.com/AminAliH47/MicroService-Users) 
to be able to send and get users data.

- You can use [Postman collection](https://www.getpostman.com/collections/ea8ae73cd9243409b825) 
to test and use gateway service endpoints.
- You can use [Swagger UI docs](http://10.5.0.1:8041/docs/) to test gateway service endpoints.

<div align="center">
<br>

###### Licensed By Huma

</div>