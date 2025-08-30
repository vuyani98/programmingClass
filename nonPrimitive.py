#Non primitive data types

#List
aList = [1, 2, 3, 4, 5]
aList2  = [1, "hello", 3.5, True]


#print(f"Index number 2 is: {aList[2]}") #3
#print(aList[2])

#Lists are mutable (you can change them)
aList[2] = 10
#print(f"Index number 2 is now: {aList[2]}") #3
#print(aList[2])


#Tuple it is immutable (you cannot change them)
aTuple = (1, 2, 3, 4, 5)
#print(f"Index number 2 is: {aTuple[2]}") #3
#print(f"From index number 2 to the end: {aTuple[2:]}") #(3, 4, 5)

#aTuple[2] = 10
#print(aTuple)


#Dictionary
redditComment1 = { 
    "edited" : False, 
    "subreddit" : "Python", 
    "score" : 1000,
    "author" : "Vuvu", 
    "comment" : "This is a great post"
}

redditComment2 = { 
    "edited" : True, 
    "subreddit" : "JavaScript", 
    "score" : 100,
    "author" : "Gladys", 
    "comment" : "This is a great post too"
}

redditComment3 = { 
    "edited" : True, 
    "subreddit" : "JavaScript", 
    "score" : 100,
    "author" : "Glady2", 
    "comment" : "This is a great post too"
}

redditComment4 = { 
    "edited" : True, 
    "subreddit" : "JavaScript", 
    "score" : 100,
    "author" : "Glady3", 
    "comment" : "This is a great post too"
}

#this is a list of comments
comments = [redditComment1, redditComment2, redditComment3, redditComment4]

#print(f"First comment is : {comments[0]['comment']} by Author: {comments[0]['author']}")


#range 
aRange = range(1, 10) #1 to 9

#for (int number = 1; number < 10; number++) in C, C++, Java, JavaScript
# range(start, end, step)

for i in range(0, len(comments)):
    print(comments[i]['author'])