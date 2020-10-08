# Twitter Toplinks
Twitter Toplinks is a project in which a twitter user can login and see stats of their timeline.

# Tech Stack
![](images/django.png) ![](images/next.png)
![](images/lambda.png) ![](images/docker-1.png)
![](images/heroku.png)
* Next.js - for a cool frontend built on top of React
* Django - for a robust backend
* AWS Lambda and API gateway - To deploy the backend API (Django)
* Heroku - To deploy the frontend (Next.js)
* Docker - to make the application scalable and production ready

# Architecture
![](images/architecture.png)

### The architecture is designed in a way that it gives best and fast experience to the user and saves cost too. The main purpose of using Lambda was to save the cost of servers running in the background unnecessarily, which has nowadays become a new norm for organizations to save cost and increase performance. MongoDB Atlas M10 cluster is used for performance and less throughput. The Next.js app is dockerized to make it platform independent and scalable in any environment. 

