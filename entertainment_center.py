import movie
import fresh_tomatoes

def create_movies():
	
	good_will_hunting = movie.Movie("Good Will Hunting","http://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Good_Will_Hunting_theatrical_poster.jpg/220px-Good_Will_Hunting_theatrical_poster.jpg",
	"www.youtube.com/watch?v=WDcMUCpppVs", 
	"Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.", 
	5)

	the_dark_knight = movie.Movie("The Dark Knight", "http://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
	"https://www.youtube.com/watch?v=EXeTwQWrcwY",
	"When the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.", 5)

	tinker_tailor = movie.Movie("Tinker, Tailor, Soldier, Spy",	
	"http://upload.wikimedia.org/wikipedia/en/thumb/3/38/Tinker%2C_Tailor%2C_Soldier%2C_Spy_Poster.jpg/220px-Tinker%2C_Tailor%2C_Soldier%2C_Spy_Poster.jpg",
	"https://www.youtube.com/watch?v=LPKhWXhiMSw",
	"In the bleak days of the Cold War, espionage veteran George Smiley is forced from semi-retirement to uncover a Soviet agent within MI6.",
	4)

	fraizer = movie.TVShow("Fraizer: Goodnight, Seattle Pt 1-2", "http://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Frasier_Logo.JPG/220px-Frasier_Logo.JPG",
	"www.youtube.com/watch?v=mNJlNJ6XfGA", "Dr. Frasier Crane moves back to his hometown of Seattle where he lives with his father and works as a radio psychiatrist.",
	5, "Season 11", "May 13, 2014")

	friends = movie.TVShow("Friends: The Last One Part Pt 1-2", "http://upload.wikimedia.org/wikipedia/en/thumb/8/86/Friends_titles.jpg/260px-Friends_titles.jpg",
	"https://www.youtube.com/watch?v=bvEnlf9g4co", "When Monica's high school friend (Rachel) re-enters her life, she sets off on a series of humorous and entertaining events involving Monica's brother (Ross), her ex-roommate (Phoebe), and her next door neighbors (Chandler & Joey)",
	5, "Season 10", "May 6, 2004")

	last_man = movie.TVShow("Last Man Standing:  Shoveling Snow", "http://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Last_Man_Standing_intertitle.jpg/250px-Last_Man_Standing_intertitle.jpg",
	"https://www.youtube.com/watch?v=FslQpa4wXZE", "A married father of three tries to maintain his manliness in a world increasingly dominated by women.",
	3.5, "Season 2", "Nov 8, 213")

	movie_list = [good_will_hunting, the_dark_knight, tinker_tailor, fraizer, friends, last_man]
	#print tinker_tailor.video_title 
	#print tinker_tailor.video_poster 
	#print tinker_tailor.video_clip_link
	#print tinker_tailor.movie_story
	#print tinker_tailor.movie_rating
	#print isinstance(last_man, movie.TVShow)
	#print type(tinker_tailor)
	fresh_tomatoes.open_movies_page(movie_list)
	
	

create_movies()

