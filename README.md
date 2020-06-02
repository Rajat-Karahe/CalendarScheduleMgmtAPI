# CalendarScheduleMgmtAPI

## Link:- https://schedulemgmt.herokuapp.com/

It's a Web APP along with REST API views

This is a Calendar Schedule management Web Application for Users

Following are the features provided:
1. Users can register themselves with a unique username and emailId along with strong password
2. Users can create their own schedules by providing event date and title
3. There is a authentication machanism so that a user can be able to see his own scheduled events only.
4. A user can Login, Logout, Create, Update and Delete scheduled events in the calendar.
```
Flow of Links for Web App :-
    Web App:
    
    baseUrl = https://schedulemgmt.herokuapp.com/
    
    Home Page = baseUrl (links to login / register in the navbar)
    Login = baseUrl/login
    Logout = baseUrl/logout
    List Created Events = baseUrl/events (login required)
    Add Events = baseUrl/event/new
    Detail of an Event = baseUrl/event/<event_id>
    Update an Event = baseUrl/event/<event_id>/update
    Delete an Event = baseUrl/event/<event_id>/delete
    
```    


```
Flow of Links for API :-
    Web App:
    
    baseUrl = https://schedulemgmt.herokuapp.com/api
    
    List of Events = baseUrl (Login Required)
    Login = baseUrl/users/login
    Logout = baseUrl/users/logout
    Add Events = baseUrl/event/new
    Detail of an Event = baseUrl/event/<event_id>  (Authentication required)
    Update an Event = baseUrl/event/<event_id>/update (Authentication required)
    Delete an Event = baseUrl/event/<event_id>/delete (Authentication required)
    
``` 
```
 Code Structure :-
    
    baseUrl = https://schedulemgmt.herokuapp.com/api
    
    List of Events = baseUrl (Login Required)
    Login = baseUrl/users/login
    Logout = baseUrl/users/logout
    Add Events = baseUrl/event/new
    Detail of an Event = baseUrl/event/<event_id>  (Authentication required)
    Update an Event = baseUrl/event/<event_id>/update (Authentication required)
    Delete an Event = baseUrl/event/<event_id>/delete (Authentication required)
    
``` 

Instructions to access API's

>1. GET ALL YOUR EVENTS:

https://schedulemgmt.herokuapp.com/api is the base url to access all your created events, to access this events a user must Login.
  Request should be GET type with login credentials: 
  
>2. CREATE AN ACCOUNT:

https://schedulemgmt.herokuapp.com/api/users/register :- To create a new user account, it accepts a POST type request in following formate
```
{
  "username" :
  "email" :
  "password" :
}
```

to regiter you must provide unique username and email id to register as a unique user, it will raise a validation error if username or email is already taken. It accepts Password of minimum 8 characters(Otherwise validation error)

>3. LOGIN:

https://schedulemgmt.herokuapp.com/api/users/login :- Users can login using this URL it accepts a POST type request in following formate,

```
{
  "username" :
  "password" :
}

```

>4. LOGOUT:

https://schedulemgmt.herokuapp.com/api/users/logout :- To logout


>5. DETAILED VIEW OF AN EVENT:

https://schedulemgmt.herokuapp.com/api/event/<id>/ :- In order to access detailed view of any of your Events send a GET request to this url by putting id of your event just after event (A user will only be able to access events created by him/her, for other's events you will get "detail not found exception")
  
>6. CREATE EVENT:

 https://schedulemgmt.herokuapp.com/api/event/<id>/update :- If request is GET user will get detailed view of his/her Event if request id POST it will update given event details:
Input JSON form:
  ```
  {
    "title" :
    "event_date" :
  }
  ```
  
>7. DELETE EVENT:

https://schedulemgmt.herokuapp.com/api/event/<id>/delete :- It will delete and event, A user will only be able to delete his/her own post for all other case will get a "detail not found error"
