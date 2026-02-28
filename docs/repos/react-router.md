# react-router

[View on GitHub](https://github.com/msashish/react-router)

---

# Getting Started with Create React App

    This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

    npx create-react-app react-router
        If errors out then install create-react-app using
            npm install create-react-app

# Setting up project

    yarn add react-router-dom
    yarn start (--> then go to http://localhost:3000/)

# Assignment: Create UserInput and UserOutput components
    Create UserInput to accept name as input text
    Create UserOutput component to display paragraph
    Refer UserInput and UserOutput components in a parent component (say Contact)
    Using state in Contact, bind the userinput to state. 
        So that input entered in UserInput component is available as state variable in parent
    Using props, pass the name in state to UserOutput for display purpose
    Using props, pass the name in state to UserInput for 2 way binding i.e to display it inside input text box


# Following are some interesting components: 
        ListAssignment --> Checking if text is long or short. Displaying its characters and deleting when clicked.
        ListSteps      --> Take a number and tick-mark the circle based on the number. As though step has been completed.