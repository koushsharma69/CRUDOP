from flask import Flask,jsonify

app=Flask(__name__)
books = [{
name: "Harry Potter and the Order of the Phoenix",
img: "https://bit.ly/2IcnSwz",
summary: "Harry Potter and Dumbledore's warning about the return of
Lord Voldemort is not heeded by the wizard authorities who, in turn, look to
undermine Dumbledore's authority at Hogwarts and discredit Harry."
}, {
name: "The Lord of the Rings: The Fellowship of the Ring",
img: "https://bit.ly/2tC1Lcg",
summary: "A young hobbit, Frodo, who has found the One Ring that
belongs to the Dark Lord Sauron, begins his journey with eight companions to
Mount Doom, the only place where it can be destroyed."
}, {
name: "Avengers: Endgame",
img: "https://bit.ly/2Pzczlb",
summary: "Adrift in space with no food or water, Tony Stark sends a
message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the
remaining Avengers -- Thor, Black Widow, Captain America, and Bruce Banner --
must figure out a way to bring back their vanquished allies for an epic showdown
with Thanos -- the evil demigod who decimated the planet and the universe."
}]

@app.route('/')
def index:
    return "Crud Operations"

@app.route("/books", methods=['GET'])
def get:
    return jsonify({'Books':books})

@app.route("/books",methods=['POST'])
def create():
    books = name: "Avengers: Endgame",
img: "https://bit.ly/2Pzczlb",
summary: "Adrift in space with no food or water, Tony Stark sends a
message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the
remaining Avengers -- Thor, Black Widow, Captain America, and Bruce Banner --
must figure out a way to bring back their vanquished allies for an epic showdown
with Thanos -- the evil demigod who decimated the planet and the universe."}
    books.append(books)
    return jsonify({'created': books})
    
    
@app.route("/books/<int:books_name>", methods=['PUT'])
def books_update(book_name):
    books['books_name']['summary'] = "Anything we can read"
    return jsonify({'books':books[book_name]})


@app.route("/books/<int:books_name>", methods=['DELETE'])
def delete(books_name):
    books.remove(books[books_name])
    return jsonify({'result': TRUE})

if __name__ = "__main__":
    app.run(debug=True)
