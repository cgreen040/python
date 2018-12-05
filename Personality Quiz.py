import webbrowser as wb
import pyautogui as pg
import time as t
points = 0 
show = pg.prompt ("What is your favorite show? ")

if show == "Dora the Explorer":
      pg.alert ("SO GOOD!")
      points += 100
      t.sleep (5)
      wb.open ("https://www.youtube.com/watch?v=rGyLz5219Lg")
elif show == "Hannah Montana":
    pg.alert("I love the music!")
    points += 90
    wb.open ("https://www.youtube.com/watch?v=uVjRe8QXFHY")
elif show == "Peppa Pig":
      pg.alert("Peppa is my favorite!")
      points += 90
      wb.open ("https://www.youtube.com/watch?v=I2Q4MMC-XSQ")
elif show == "Mickey Mouse":
      pg.alert("I watch Mickey Mouse all the time!")
      points += 200
      wb.open ("https://www.youtube.com/watch?v=Yh83saHTYNY")
elif show == "Sofia the First":
      pg.alert("That is my second favorite show")
      points += 300
      wb.open ("https://www.youtube.com/watch?v=Iz7QXSOkBjA")
elif show == "Spongebob Squarepants":
      pg.alert("I love patrick too!")
      points += 200
      wb.open ("https://www.youtube.com/watch?v=r9L4AseD-aA")
else:

    pg.alert ("Your favorite show is " + str(show))
    
food = pg.prompt ("What is your favorite food?")

if food == "Pizza":
    pg.alert ("Pizza is so good!")
    points += 20
    wb.open ("https://www.myrecipes.com/recipe/ultimate-cheese-pizza")
elif food == "Salad":
    pg.alert("I love salad!")
    points += 10
    wb.open ("https://www.cookingclassy.com/caesar-salad-recipe-homemade-caesar-salad-dressing/")
elif food == "Chicken fingers":
    pg.alert("They're okay")
    points += 5
    wb.open ("http://www.layersofhappiness.com/homemade-cheddar-garlic-chicken-fingers/")
elif food == "Mac & Cheese":
    pg.alert("I love the cheddar kind")
    points += 400
    wb.open ("https://en.wikipedia.org/wiki/Macaroni_and_cheese")
elif food == "Hamburgers":
    pg.alert("I have hamburgers very often")
    points += 400
    wb.open ("https://en.wikipedia.org/wiki/Hamburger")
elif food == "Tacos":
    pg.alert("Tacos are super good")
    points += 20
    wb.open ("https://www.hellofresh.com/recipes/pineapple-poblano-beef-tacos-59a83c57a2882a59886519a2")
else:
    pg.alert("You like to eat " + food)

lastname = pg.prompt ("What is your lastname? ")

if lastname == "Green":
      pg.alert ("That is my favorite color! ")
      points += 100
      wb.open ("https://en.wikipedia.org/wiki/Green")
elif lastname == "chandler":
      pg.alert ("Hi Chandler Green")
      points + 400
      wb.open ("https://en.wikipedia.org/wiki/Matthew_Perry")
elif lastname == "Greene":
      pg.alert ("That is not how it is spelled")
      points - 200
elif lastname == "Greeeeen":
      pg.alert ("Still not it!")
      points - 300
elif lastname == "Gren":
      pg.alert ("Nope!")
      points -500
elif lastname == "Greennnn":
      pg.alert ("Nice try!")
      points -300
else:
      pg.alert ("Your lastname is " + lastname)

sport = pg.prompt("What is your favorite sport? ")

if sport == "Tennis":
      pg.alert ("Tennis is so fun!")
      points += 100
      t.sleep (4)
      wb.open ("https://www.youtube.com/watch?v=H7FGuJcOQBM")
elif sport == ("Soccer"):
      pg.alert ("I play soccer too!")
      points += 10
      wb.open ("https://www.youtube.com/watch?v=Tdn9r5X25XA")
elif sport == ("Squash"):
      pg.alert ("I want to start playing squash!")
      points += 90
      wb.open ("https://www.youtube.com/watch?v=Lbdp-HCjWw8")
elif sport == ("Lacrosse"):
      pg.alert ("I used to play lacrosse!")
      points += 5
      wb.open ("https://www.youtube.com/watch?v=-Ek8tghQy8Y")
elif sport == ("Crew"):
      pg.alert ("Crew requires a lot of strength!")
      points += 20
      wb.open ("https://www.youtube.com/watch?v=TG0sCWXpRf0?")
elif sport == ("Field Hockey"):
      pg.alert ("I used to play but it is not my favorite!")
      points += 2
      wb.open ("https://www.youtube.com/watch?v=H3bQ5CZPTJs")
elif sport == ("Water Polo"):
      pg.alert ("It seems so fun!")
      points += 5
      wb.open ("https://www.youtube.com/watch?v=hkZ2jWbEcBc") 
else:
      pg.alert ("Your favorite sport is " + sport)

candy = pg.prompt("What is your favorite candy? ")

if candy == "Twix":
      pg.alert ("I love twix too!")
      t.sleep (3)
      wb.open ("https://en.wikipedia.org/wiki/Twix")
elif candy == ("Kit Kat"):
      pg.alert ("I'm being that for halloween!")
      points += 100
      wb.open ("https://en.wikipedia.org/wiki/Kit_Kat")
elif candy == ("Twizzler"):
      pg.alert ("I love the red kind!")
      points += 100
      wb.open ("https://en.wikipedia.org/wiki/Twizzlers")
elif candy == ("Crunch"):
      pg.alert ("It's so good!")
      points += 100
      wb.open ("https://en.wikipedia.org/wiki/Nestl%C3%A9_Crunch")
elif candy == ("Milky Way"):
      pg.alert ("It's not my favorite")
      points -= 100
      wb.open ("https://en.wikipedia.org/wiki/Milky_Way_(chocolate_bar)")
elif candy == ("Skittles"):
      pg.alert ("They are okay")
      points -= 50
      wb.open ("https://en.wikipedia.org/wiki/Skittles_(confectionery)")
else:
      pg.alert ("Your favorite candy is " + candy)
pg.alert (points)


