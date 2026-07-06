# This is the main application file that runs the Flask web server and handles user requests
# Which will include uploading files, chunking them, embedding the chunks, storing them in a vector database, and searching for similar chunks based on user queries.

from chromadb.app import app

if __name__ == "__main__":
    app.run(debug=True)
