# App Name

Material UI, while it looks nice and gives you some stuff out of the box that saves time, it does seem to require you to import a lot of varied stuff to make it work, and if you need to overwrite some of their stylings it get complicated
It also gets complicated when handling submits


<img src="https://github.com/jennikate/remember-your-meds/blob/development/readme-images/splash.png?raw=true">


by [JenniKate Wallace](https://github.com/jennikate), [Jonny Farmer](https://github.com/jonnysfarmer)

## The product

[View the app](http://take-your-medicine.herokuapp.com/#/)

[View the code](url)

_gif goes here_

### Overview

Don't forget your meds! is an app where you can:

- store your medicine information including dosage and renewal dates
- choose to get reminders to take your meds at a specific time of day
- choose to get SMS and/or email reminders for each type

----

## The brief


----

## Technologies used

#### Backend : technologies used to create our Schema's and API


**Additional Libraries**


#### Frontend : technologies used to create our interface and interactions

**Additional Libraries**

#### Integrations : 3rd party products and APIs

- NHS API for data
- Twilio for SMS
- EmailJS for email


#### Management : tools used for planning and delivery management

- Trello : for task management
- Figma : for wireframing
- LucidChart : for dataflows / dbstructure

----

## The planning

### Management

<img src="https://github.com/jennikate/remember-your-meds/blob/development/readme-images/trello-board.png?raw=true" width="200px">


### Flows

<img src="https://github.com/jennikate/remember-your-meds/blob/development/readme-images/flow-overview.png?raw=true" width="200px"><img src="https://github.com/jennikate/remember-your-meds/blob/development/readme-images/flow-create.png?raw=true" width="200px"><img src="https://github.com/jennikate/remember-your-meds/blob/development/readme-images/flow-remind.png?raw=true" width="200px">


### Entity Relationship Diagram
<img src="https://github.com/jennikate/remember-your-meds/blob/development/readme-images/erd.png?raw=true" width="200px">

----


## The development

----

## Hurdles Overcome & Problems to Solve

----

## Future

### Go Native

We would ideally turn this into a native app for android and iphone and offer notifications as preferable to sms's for reminders. 

### Schedule Reminders

These are features we built as much as we could for, but some aspects were outside our scope

**Remdiner scheduling**
The idea of this app is to send you reminders, either on a date or at a time, so you remember to take medicine, or order it, or make a doctors appointment to review.

We spent some time investigating how to trigger these reminders at the specific time or date. And decided it had to be a CRON job, or even better, using a proper scheduler like RabbitMQ. This was outside our capabilities currently and as this was a week long project we decided we did not have enough time to learn how to set these up, and therefore have not built the actual scheduling of sends.

**Send email reminders**
We implemented Yagmail to send email reminders and can trigger a successful send from our backend.

**Send SMS reminders**
We implemented Twilio to send sms reminders and could trigger a successful send from our backend, though we've removed this functionality for deployment as it can't be run from live app and contains secure information that we didn't want to have to deal with for this project deploy.

### Feature Ideas

These were considered in our architecture but were deprioritised due to time constraints

- Link to/details of my GP

These are other ideas that we deprioritised before we began design

- Link to/details of my pharmacy 
- Search conditions to get NHS information

### Bugs

 - can't work out how to remove the underline on menu links (text-decoration: none is not clearing them!)
 - on edit prescription, if you change amounts but do not reenter(orchange) the prescription name, it errors with 'not a valid string'
 - empty fields on add prescription are not showing errors
 - page loads after form submits are not always loading full info now we're on heroku with `too many connections`, works locally so needs investigating
 - time input fields not working on iOS (safari or chrome), discovered they are unsupported only after we'd pushed to heroku and tested on phones

If you find any other bugs let us know!


----
