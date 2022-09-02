from urllib import request
from django.views.generic import ListView
from django.shortcuts import render


from .models import Book,Detail




def BulkInsert(request):

    

    

   

    

   

    context={}
    
    

    

       

    data = [
	{
		"id": 1,
		"title": "Brittany Martin",
		"author": "Colorado Wilson",
		"price": 3,
		"published_year": 2
	},
	{
		"id": 2,
		"title": "Lamar Cantrell",
		"author": "Nicholas Mathews",
		"price": 8,
		"published_year": 5
	},
	{
		"id": 3,
		"title": "Hannah Weber",
		"author": "Prescott Patton",
		"price": 3,
		"published_year": 6
	},
	{
		"id": 4,
		"title": "Stuart Michael",
		"author": "Harding Franco",
		"price": 4,
		"published_year": 5
	},
	{
		"id": 5,
		"title": "Justina Medina",
		"author": "Avram Williams",
		"price": 7,
		"published_year": 7
	},
	{
		"id": 6,
		"title": "Azalia Mayer",
		"author": "Jackson Cote",
		"price": 2,
		"published_year": 2
	},
	{
		"id": 7,
		"title": "Alfonso Warner",
		"author": "Kennan Page",
		"price": 5,
		"published_year": 6
	},
	{
		"id": 8,
		"title": "Vivien Barry",
		"author": "Peter Mcclain",
		"price": 1,
		"published_year": 6
	},
	{
		"id": 9,
		"title": "Bertha Gilmore",
		"author": "Felix Delacruz",
		"price": 9,
		"published_year": 2
	},
	{
		"id": 10,
		"title": "Jessica Michael",
		"author": "Mason Burt",
		"price": 2,
		"published_year": 6
	},
	{
		"id": 11,
		"title": "Talon Barrera",
		"author": "Lawrence Patton",
		"price": 8,
		"published_year": 3
	},
	{
		"id": 12,
		"title": "Shoshana Guzman",
		"author": "Amos Harrington",
		"price": 7,
		"published_year": 1
	},
	{
		"id": 13,
		"title": "Edan Gilbert",
		"author": "Rashad Lambert",
		"price": 7,
		"published_year": 0
	},
	{
		"id": 14,
		"title": "Forrest Hicks",
		"author": "Tucker Atkins",
		"price": 9,
		"published_year": 5
	},
	{
		"id": 15,
		"title": "Jeremy Blevins",
		"author": "Duncan Chavez",
		"price": 7,
		"published_year": 7
	},
	{
		"id": 16,
		"title": "Reagan Douglas",
		"author": "August Rhodes",
		"price": 8,
		"published_year": 3
	},
	{
		"id": 17,
		"title": "Trevor Cunningham",
		"author": "Burke Burt",
		"price": 5,
		"published_year": 4
	},
	{
		"id": 18,
		"title": "Clark Welch",
		"author": "Reed Keller",
		"price": 2,
		"published_year": 3
	},
	{
		"id": 19,
		"title": "Baxter Buckner",
		"author": "Orlando Cooley",
		"price": 9,
		"published_year": 2
	},
	{
		"id": 20,
		"title": "Cade Christensen",
		"author": "Harding Morse",
		"price": 6,
		"published_year": 6
	},
	{
		"id": 21,
		"title": "Derek Vang",
		"author": "Jameson Shaffer",
		"price": 1,
		"published_year": 7
	},
	{
		"id": 22,
		"title": "Veda Riley",
		"author": "Tad Fisher",
		"price": 5,
		"published_year": 2
	},
	{
		"id": 23,
		"title": "Calista Gay",
		"author": "Fitzgerald Conway",
		"price": 2,
		"published_year": 4
	},
	{
		"id": 24,
		"title": "Heather Murphy",
		"author": "Dane Clements",
		"price": 3,
		"published_year": 6
	},
	{
		"id": 25,
		"title": "Griffin Mercado",
		"author": "Ciaran Mayer",
		"price": 8,
		"published_year": 6
	},
	{
		"id": 26,
		"title": "Tobias Hayes",
		"author": "Zahir Warner",
		"price": 3,
		"published_year": 6
	},
	{
		"id": 27,
		"title": "Charlotte Bolton",
		"author": "Chandler Hamilton",
		"price": 5,
		"published_year": 5
	},
	{
		"id": 28,
		"title": "Mallory Cline",
		"author": "Luke Mcintosh",
		"price": 7,
		"published_year": 8
	},
	{
		"id": 29,
		"title": "Colton Morrison",
		"author": "Linus Chan",
		"price": 6,
		"published_year": 3
	},
	{
		"id": 30,
		"title": "Conan Klein",
		"author": "Elton Copeland",
		"price": 8,
		"published_year": 1
	},
	{
		"id": 31,
		"title": "Kimberley Garrison",
		"author": "Chaim Mcpherson",
		"price": 1,
		"published_year": 8
	},
	{
		"id": 32,
		"title": "Maryam Keith",
		"author": "Odysseus Bright",
		"price": 0,
		"published_year": 7
	},
	{
		"id": 33,
		"title": "Vera Heath",
		"author": "Callum Poole",
		"price": 6,
		"published_year": 4
	},
	{
		"id": 34,
		"title": "Cody Sullivan",
		"author": "Rashad Kidd",
		"price": 9,
		"published_year": 8
	},
	{
		"id": 35,
		"title": "Upton Bowen",
		"author": "Jerry Molina",
		"price": 9,
		"published_year": 7
	},
	{
		"id": 36,
		"title": "Tanisha Summers",
		"author": "Nehru Beasley",
		"price": 0,
		"published_year": 1
	},
	{
		"id": 37,
		"title": "Maite Shaw",
		"author": "Jasper Ruiz",
		"price": 9,
		"published_year": 2
	},
	{
		"id": 38,
		"title": "Tate Willis",
		"author": "Dorian Jackson",
		"price": 1,
		"published_year": 7
	},
	{
		"id": 39,
		"title": "Allistair Alexander",
		"author": "Gannon Bray",
		"price": 5,
		"published_year": 7
	},
	{
		"id": 40,
		"title": "Jessamine Gallagher",
		"author": "Declan Horton",
		"price": 4,
		"published_year": 9
	},
	{
		"id": 41,
		"title": "Zelda Diaz",
		"author": "Drake Lambert",
		"price": 9,
		"published_year": 5
	},
	{
		"id": 42,
		"title": "James Schroeder",
		"author": "Ignatius Ball",
		"price": 2,
		"published_year": 3
	},
	{
		"id": 43,
		"title": "Madaline Meyer",
		"author": "Gareth Phelps",
		"price": 4,
		"published_year": 5
	},
	{
		"id": 44,
		"title": "Celeste Cooley",
		"author": "Jerome Jacobs",
		"price": 4,
		"published_year": 8
	},
	{
		"id": 45,
		"title": "Kristen Small",
		"author": "Geoffrey Hunt",
		"price": 1,
		"published_year": 3
	},
	{
		"id": 46,
		"title": "Jorden Gregory",
		"author": "Aidan Battle",
		"price": 10,
		"published_year": 9
	},
	{
		"id": 47,
		"title": "India Boyd",
		"author": "Chaney Le",
		"price": 1,
		"published_year": 6
	},
	{
		"id": 48,
		"title": "Matthew Holloway",
		"author": "Timon Willis",
		"price": 7,
		"published_year": 8
	},
	{
		"id": 49,
		"title": "Ulla Black",
		"author": "Baker Montoya",
		"price": 2,
		"published_year": 7
	},
	{
		"id": 50,
		"title": "Galena Hamilton",
		"author": "Cooper Santana",
		"price": 3,
		"published_year": 10
	},
	{
		"id": 51,
		"title": "Britanney Rowe",
		"author": "Craig Hanson",
		"price": 1,
		"published_year": 8
	},
	{
		"id": 52,
		"title": "Lyle Horton",
		"author": "Chancellor James",
		"price": 1,
		"published_year": 8
	},
	{
		"id": 53,
		"title": "Yael Hunt",
		"author": "Burke Wade",
		"price": 7,
		"published_year": 9
	},
	{
		"id": 54,
		"title": "Lewis Franklin",
		"author": "Zeph Mendez",
		"price": 0,
		"published_year": 1
	},
	{
		"id": 55,
		"title": "Galvin Kaufman",
		"author": "Cole Rose",
		"price": 9,
		"published_year": 5
	},
	{
		"id": 56,
		"title": "Xander Cook",
		"author": "Blake Duke",
		"price": 8,
		"published_year": 9
	},
	{
		"id": 57,
		"title": "Kato Santiago",
		"author": "Garrison Sellers",
		"price": 3,
		"published_year": 7
	},
	{
		"id": 58,
		"title": "Skyler Cleveland",
		"author": "Barry Gallagher",
		"price": 2,
		"published_year": 1
	},
	{
		"id": 59,
		"title": "Xander Chaney",
		"author": "Logan David",
		"price": 6,
		"published_year": 6
	},
	{
		"id": 60,
		"title": "Cora Clements",
		"author": "Travis Jacobson",
		"price": 3,
		"published_year": 4
	},
	{
		"id": 61,
		"title": "Xavier Elliott",
		"author": "Buckminster Shelton",
		"price": 1,
		"published_year": 4
	},
	{
		"id": 62,
		"title": "Leslie Cline",
		"author": "Kareem Brown",
		"price": 8,
		"published_year": 7
	},
	{
		"id": 63,
		"title": "Howard Maxwell",
		"author": "Valentine Bolton",
		"price": 1,
		"published_year": 4
	},
	{
		"id": 64,
		"title": "Tyrone Rosario",
		"author": "Blake Foreman",
		"price": 8,
		"published_year": 7
	},
	{
		"id": 65,
		"title": "Kiara Garza",
		"author": "Lance Cox",
		"price": 9,
		"published_year": 2
	},
	{
		"id": 66,
		"title": "September Leon",
		"author": "Jonah Sweet",
		"price": 6,
		"published_year": 7
	},
	{
		"id": 67,
		"title": "Trevor Lawson",
		"author": "Joseph Le",
		"price": 4,
		"published_year": 2
	},
	{
		"id": 68,
		"title": "Hop Mckee",
		"author": "Chadwick Kent",
		"price": 5,
		"published_year": 5
	},
	{
		"id": 69,
		"title": "Nicholas Horn",
		"author": "Kermit Mcknight",
		"price": 5,
		"published_year": 2
	},
	{
		"id": 70,
		"title": "Dacey Armstrong",
		"author": "Macaulay Nash",
		"price": 9,
		"published_year": 5
	},
	{
		"id": 71,
		"title": "Finn Giles",
		"author": "Graiden Rodriquez",
		"price": 6,
		"published_year": 5
	},
	{
		"id": 72,
		"title": "Thor Page",
		"author": "Dante Lancaster",
		"price": 5,
		"published_year": 8
	},
	{
		"id": 73,
		"title": "Martina Mcfarland",
		"author": "Ignatius Livingston",
		"price": 9,
		"published_year": 1
	},
	{
		"id": 74,
		"title": "Isabelle Burgess",
		"author": "Yoshio Patrick",
		"price": 4,
		"published_year": 6
	},
	{
		"id": 75,
		"title": "Judith Mendoza",
		"author": "Amal Small",
		"price": 2,
		"published_year": 9
	},
	{
		"id": 76,
		"title": "Claudia Cross",
		"author": "Valentine Justice",
		"price": 5,
		"published_year": 0
	},
	{
		"id": 77,
		"title": "Rinah Dunn",
		"author": "Benjamin Foley",
		"price": 5,
		"published_year": 9
	},
	{
		"id": 78,
		"title": "Tasha Atkinson",
		"author": "Lee House",
		"price": 8,
		"published_year": 4
	},
	{
		"id": 79,
		"title": "Lesley Fulton",
		"author": "Kevin Glover",
		"price": 9,
		"published_year": 1
	},
	{
		"id": 80,
		"title": "Minerva Barton",
		"author": "George Brennan",
		"price": 9,
		"published_year": 2
	},
	{
		"id": 81,
		"title": "Connor Soto",
		"author": "Calvin Christensen",
		"price": 1,
		"published_year": 8
	},
	{
		"id": 82,
		"title": "Davis Lucas",
		"author": "Kareem Duran",
		"price": 7,
		"published_year": 8
	},
	{
		"id": 83,
		"title": "Conan Walter",
		"author": "Reese Brewer",
		"price": 3,
		"published_year": 2
	},
	{
		"id": 84,
		"title": "Ronan Bender",
		"author": "Randall Mcdonald",
		"price": 5,
		"published_year": 2
	},
	{
		"id": 85,
		"title": "Maxine Drake",
		"author": "Thaddeus Ellison",
		"price": 7,
		"published_year": 3
	},
	{
		"id": 86,
		"title": "August Noble",
		"author": "Yasir Hoffman",
		"price": 4,
		"published_year": 2
	},
	{
		"id": 87,
		"title": "Nathan Dorsey",
		"author": "Gabriel Bruce",
		"price": 7,
		"published_year": 6
	},
	{
		"id": 88,
		"title": "Savannah Morales",
		"author": "Allen Delgado",
		"price": 3,
		"published_year": 5
	},
	{
		"id": 89,
		"title": "Emery Francis",
		"author": "Dillon Farley",
		"price": 9,
		"published_year": 10
	},
	{
		"id": 90,
		"title": "Noah Harrington",
		"author": "Thomas Duncan",
		"price": 5,
		"published_year": 0
	},
	{
		"id": 91,
		"title": "Rooney Murphy",
		"author": "Shad Larson",
		"price": 9,
		"published_year": 8
	},
	{
		"id": 92,
		"title": "Kalia Chen",
		"author": "Dylan Richards",
		"price": 1,
		"published_year": 2
	},
	{
		"id": 93,
		"title": "Amelia Peters",
		"author": "Marshall Adams",
		"price": 4,
		"published_year": 6
	},
	{
		"id": 94,
		"title": "Cole Wong",
		"author": "Jordan Frazier",
		"price": 8,
		"published_year": 1
	},
	{
		"id": 95,
		"title": "Olympia Holden",
		"author": "Hashim Perry",
		"price": 3,
		"published_year": 6
	},
	{
		"id": 96,
		"title": "Donovan Zamora",
		"author": "Noble Avery",
		"price": 2,
		"published_year": 1
	},
	{
		"id": 97,
		"title": "Kibo Baird",
		"author": "Logan Webb",
		"price": 9,
		"published_year": 9
	},
	{
		"id": 98,
		"title": "Maggy Clarke",
		"author": "Kamal Carroll",
		"price": 7,
		"published_year": 8
	},
	{
		"id": 99,
		"title": "Whitney Raymond",
		"author": "Thane Ball",
		"price": 5,
		"published_year": 4
	},
	{
		"id": 100,
		"title": "Upton Bradley",
		"author": "John Harmon",
		"price": 7,
		"published_year": 1
	}
]
    for i in data:
        n=Book(title=i["title"],author=i["author"],price=i["price"],published_year=i["published_year"])
        n.save()

    context["dataset"] = Book.objects.all()
    context["newdataset"]= Detail.objects.select_related("name").all()
    context["newdataset1"]= Detail.objects.prefetch_related("name").all()

    return render(request, 'DisplayBookList.html', context)
   



        