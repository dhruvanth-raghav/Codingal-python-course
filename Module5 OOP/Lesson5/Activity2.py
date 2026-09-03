class India:
    def capital(self):
        print("New Delhi is the capital of india")

class USA:
    def capital(self):
        print("Washington D.C is the capital of USA")

class Japan:
    def capital(self):
        print("Tokyo is the capital of Japan")

#--------------------------------------------------------------

obj_ind=India()
obj_usa=USA()
obj_japan=Japan()

for country in [obj_ind,obj_usa,obj_japan]:
    print(type(country))
    country.capital()
    print()