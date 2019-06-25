
from flask import Flask, Response
import media
import fresh_tomatoes
from flask import Flask
from http.server import BaseHTTPRequestHandler, HTTPServer


avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")


toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=tN1A2mVnrOM")

#print(toy_story.storyline)
#print(toy_story.storyline)


mission_impossible_6 = media.Movie("Mission: Impossible – Fallout",
					 "Ethan Hunt and the IMF team join forces with CIA assassin August Walker to prevent a disaster of epic proportions",
					 "https://upload.wikimedia.org/wikipedia/en/f/ff/MI_%E2%80%93_Fallout.jpg",
					 "https://www.youtube.com/watch?v=P5_iNAWUUQA")

#print(mission_impossible_6.storyline)
#mission_impossible_6.show_trailer()


uri_surgical_strike = media.Movie("Uri: The Surgical Strike",
								  "Following the roguish terrorist attacks at Uri Army Base camp in Kashmir, India takes the fight to the enemy, in its most successful covert operation till date with one and only one objective of avenging their fallen heroes",
								  "https://upload.wikimedia.org/wikipedia/en/3/3b/URI_-_New_poster.jpg",
								  "https://www.youtube.com/watch?v=KiYdjJo663Q")

#print(uri_surgical_strike.storyline)
#uri_surgical_strike.show_trailer()


inception = media.Movie("Inception",
						"The story of a thief with a unique ability to steal information from his targets, by entering their dreams",
						"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
						"https://www.youtube.com/watch?v=d3A3-zSOBT4")

#print(inception.storyline)
#inception.show_trailer()

movies = [toy_story, avatar, mission_impossible_6, uri_surgical_strike, inception]

fresh_tomatoes.open_movies_page(movies)