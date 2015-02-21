import webbrowser

class Video:
	'''Parent class for all Videos'''
	
	#Constructor for parent class
	def __init__(self, video_title, video_poster, video_clip_link):
		#Title of the video
		self.video_title = video_title
		#Poster image of the video
		self.video_poster = video_poster
		#Youtube link to play the video
		self.video_clip_link = video_clip_link



class Movie(Video):
	'''Movie Class inheriting from Video'''

	#Constructor for child Movie class
	def __init__(self, movie_title, movie_poster, movie_trailer_link, movie_story, movie_rating):
		Video.__init__(self, movie_title, movie_poster, movie_trailer_link)

		#Store additional information relevant to the Movie class
		self.movie_story = movie_story
		self.movie_rating = movie_rating


class TVShow(Video):
	'''TVShow class inheriting from Video class. This subclass shows eposide level details of a TV show'''
	#Constructor for child TVshows class
	def __init__(self, show_eposide_title, show_poster, show_trailer_link, show_story, show_rating, show_season, show_broadcast_details):
		Video.__init__(self, show_eposide_title, show_poster, show_trailer_link)

		#Store additional information relevant to the TVShow class
		self.show_story = show_story
		self.show_rating = show_rating
		self.show_season = show_season
		self.show_broadcast_details = show_broadcast_details
		

		