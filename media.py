import webbrowser


class Movie():
    
    """This a class to create movie objects"""
    
    # constructor for the class
    def __init__(self, title, story_line, poster_image_url, trailer_youtube_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    #Function to open youtube link
    def show_trailer(self):
        print "Now playing trailer of " + self.title
        webbrowser.open(self.trailer_youtube_url)
