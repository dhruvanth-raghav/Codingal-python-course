#STEP1- Create the class song - that represents the blueprint
#Class names start with a capital letter
class Song:
    #This is called a class property/variable
    medium = "audio"

#Object properties/variables
    #This function is called  CONSTRUCTOR
    #it is called immediately when you create an object
    def __init__(self, name, genre, artist, release_year):
        self.name= name
        self.genre= genre
        self.artist= artist
        self.release_year= release_year

#(Above is the class definition)
#=====================================================================
#(Below, lets create some objects from the class)
#NOTE: This is not a function call, this is object creation
#song1 is an object of class Song
song1= Song("Pride(In The Name Of Love)","Rock","U2",1984)
print("song1=",song1)
print("type(song1)=",type(song1))


print("medium property of song1 object=",song1.medium)

#this is the second object of class Song
song2= Song("Higher groung","Jazz","Steevie wonder",1973)

print(song2.medium)

print("===PROPERTIES OF SONG 1===")
print(song1.name)
print(song1.genre)
print(song1.artist)
print(song1.release_year)
print()

print("===PROPERTIES OF SONG2===")
print(song2.name)
print(song2.genre)
print(song2.artist)
print(song2.release_year)
print()