# Fiberr

## Inspiration
This app was inspired by how confusing it is to make healthy, sustainable choices when it comes to purchasing groceries and snacks. We aim to promote a sustainable lifestyle and educate our users on the available alternatives to their favorite (yet unhealthy) foods . 

## What it does
This project takes our user's dietary priorities into account and uses them to suggest better alternatives. After selecting their preferences, users can scan any barcode, and the app will recognize the product, analyze its nutritional content with respect to user preferences, and suggest better alternatives if they are available. 

## How we built it
We used OpenCV to scan barcodes using the camera to get the UPC value. We then used python to query the specific UPC into openFoodData API to get relevant data on the scanned product. On the frontend, a simple React app views the webcam and is meant to display the JSON query below (work in progress). To provide better suggestions, arguments had to be passed into the API and the results were sorted based on user preference.

## Challenges we ran into
To start, our team struggled finding the best APIs since most popular options only work for US products.
It was difficult to quanitify the metrics for what makes food nutritious, since there are a lot of different ways to measure the quality of food that vary between food groups, such as Nutriscore. We also had difficulties with integrating the React frontend, and Python backend. On the front end, we had difficulties using the router to navigate through the app, and NPM would occasionally refuse to install necessary packages. Thus, the group was divided into two teams - backend and fronted, and at the end both faced difficulties integrating their solutions.

## Accomplishments that we're proud of
We're proud of being able to select the right API that fit our criteria, and recieve meaningful queries from it. Additionally, we came up with a clean and attractive prototype design which would have kept the app really clean and intuitive. Our team spent a lot of time coming up with a meaningful idea which helped set us up for a good process and an enjoyable time working together. Interfacing OpenCV with an API was a first for all of us and we're satisfied with the results despite not having any background. Lastly, this experience helped accelerate our knowledge of fullstack development immensely, and everything we accomplished this weekend was built from scratch. 

## What we learned
We learned how to use and test APIs and how to incorporate them into our code. We learned how to parse JSON files, basics of building frontends with React and JS, working with data structures and image processing in Python, as well as the importance of reaching out for help when we need it. 

## What's next for Fiberr
As we further develop our app, we would like to incorporate more health preferences to make a more personalized experience for our users. We would also like to use our users data and link it with Apple/Google Health for a better overall experience. Another future objective for our application would be to provide recipes using the alternative healthier options to interest our user in buying the healthiest option by tapping into their location and serving up data from the API of retail store closets to them.

