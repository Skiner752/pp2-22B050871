def score(movies):
    if movies["imdb"] > 5.5:
        return True
    else:
        return False


def sublist(all_movies):
    return [movie for movie in all_movies if movie["imdb"] > 5.5]
        


def category_name(all_movies, category):
    return [categ for categ in all_movies if categ["category"] == category]



def average(all_movies):
    amount_of_movies = len(all_movies)
    a = 0
    for movie in all_movies:
        a += movie["imdb"] 
    return a/amount_of_movies


def category_average(all_movies , category):
    amount_of_movies_category = len([movie for movie in all_movies if movie["category"] == category])
    b = 0
    for movie in all_movies:
        if movie["category"] == category:
            b += movie["imdb"]

    return b/amount_of_movies_category



movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# for movie in movies:
#     print(score(movie))


# print(sublist(movies))


# print(category_name(movies , 'Romance'))

# print(average(movies))

# print(category_average(movies , 'Romance'))