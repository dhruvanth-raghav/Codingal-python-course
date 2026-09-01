class Point:
    def __init__(self, x ,y):
        self.x=x
        self.y=y
    #Whenever you print the object, it will print what is returned by __str__()

    def __str__(self):
        return f"2D point is ({self.x},{self.y})"
#==============================================================================
p1=Point(5,12)
print(p1)

