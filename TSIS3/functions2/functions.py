def isGood(movie):
    return movie["imdb"] > 5.5


def areGood(movies):
    return list(filter(lambda movie: movie["imdb"] > 5.5, movies))


def collectByCategory(movies, category):
    return list(filter(lambda movie: movie["category"] == category, movies))


def averageScore(movies):
    totalScore = 0
    for movie in movies:
        totalScore += movie["imdb"]
    return totalScore / len(movies)


def averageScoreOfCategory(movies, category):
    totalScore = 0
    cnt = 0
    for movie in movies:
        if movie["category"] == category:
            totalScore += movie["imdb"]
            cnt += 1
    return totalScore / cnt
