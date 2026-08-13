weather=(0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1)
#0=rainy...1=sunny
# sunny=weather.count(1)
# rainy=weather.count(0)
sunny=0
rainy=0
for daily_weather in weather:
    if daily_weather==0:
        rainy+=1
        
    else:
        sunny+=1
print("NO.of rainy days=",rainy)
print("No.of sunny days=",sunny)
    


if sunny>rainy:
    print("Sunny weather today")
else:
    print("Rainy weather today")