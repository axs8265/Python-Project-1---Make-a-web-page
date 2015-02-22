Movie trailer project consists of following modules:

1. movie.py – this file consists the of following class definitions :
	a. Video – Parent class for types inhibiting a video behavior
	b. Movie – Child of Video class. Contains structure for a movie type data
	c. TVShow – Child of Video class. Contains structure for a TV show type data

2. fresh_tomatoes – this is module dynamically generates html file based on the video data provided in form of a list. The main function to generate the html file is 
	fresh_tomatoes.open_movies_page

3. entertainment_center.py – this module imports movie and instantiates objects of Movie and TVShow and passes them in a list to fresh_tomatoes module to create the html page containing information about videos of your pick

How to Run Movie Trailer:

  - Make sure you have Pyhon 2.7 installed on your mahcine
  - Simply double click file entertainment_center.py to generate and open HTML page

Want to Create your own movie list:

  -Import movie and fresh_tomatoes to your Python program
  -Take a look at entertainment_center.py to create your own movies and tv shows and how to use them to generate your very own movie list.
