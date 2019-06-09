# Multi-Path Story
This is a web application which enables the user to write "multi-path stories." A multi-path story is composed of sentences. 
After each sentence, there are up to four possible next sentences, and after each of those, another four possible next 
sentences, and so on.

## Configuration

**clone the project or unzip the archive in the folder of your choice:**
+ `git clone https://github.com/fergalpowell/multi-path-stories.git`

**create and start a virtual environment:**
+ `virtualenv env --no-site-packages`
+ `source env/bin/activate`

**install the project dependencies:**
+ `pip install -r requirements.txt`
  
**to start the development server**
+ flask run
  
**and open http://127.0.0.1:5000/ on your browser to view the app.**

## Design and Architecture
The web framework that was used to develop this application was the micro python framework Flask. This framework was 
selected over Django as it provides simplicity, flexibility and fine-grained control and Django's all inclusive features
were not going to be needed for this lightweight web app.

On the client side the user interface was kept as simple and as intuitive as possible while using a Material Design approach.
The client can communicate with the back-end of the web app through two URLs: 
  * **/story/story_id**: This URL takes the id of a story as a parameter and searches for the story in the story dictionary using that 
  id. Once the story is found it is returned to the client with all current data for that story. The app initialy redirects to 
  `/story/story1` and the Back To Home button also uses to this URL. This URL is also used with the corresponding path id 
  each time the user clicks on a path link.
  * **/create_story**: This URL is used when the user submits a new path to a story. A form is submitted on the client-side
  that contains the current story id, the path position and the sentence. This data is used to create a new entry in the 
  story dictionary and updates the current story to contain the new path id. Once completed the current story id is used 
  to redirect to the `/story/story_id` URL to show the new path in the story. There is very simple user input validation 
  through the use of the `required` attribute in the form inputs.
  
## Challenges and Learning outcomes
The challenge that proved most difficult for me in this project was designing the format of the data structure that would hold
the stories in memory. The speed when retrieving when getting/creating stories was a priority, a database was not used and
the stories are not stored persistently. Python offers many data structures that could have been used but as mentioned 
previously, a dictionaty was used to store the stories as order of the stories being stored did not matter and it provided
an easy and fast method of searching through the use of keys. 

I began storing the stories in a nested format however I found that this method required recursivly searching through each 
story and it's paths and their paths etc...so I decided that a better method would be to keep each story in an object on the 
same level in the dictionary and then holding a reference to each of the story's paths in the object.

This project exercised my ability to create a well-structured client-server web app using only the basics. The nature of the 
Multi-Path Story involves a lot of repitation so it was important to manage the code in the back-end in a way that would 
accomodate that through code re-useability, i.e. creating functions to be used repeatedly. 
