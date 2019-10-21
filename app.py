from flask import Flask
from datetime import datetime
from graph import Graph
from math import inf
import json
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME"

@app.route("/hello/<name>")
def hello(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    # return Graph.teste()
    return "Hello " + clean_name + " Its " + formatted_now

@app.route("/grafo/<size>")
def grafo(size):
    size = int(size)
    path = Graph.create_path_matrix(size)
    graph = Graph.create_graph(size)
    graph,y = Graph.mock_distances(graph, path)
    dist,x = Graph.floyd_warshall(graph, path)
    for i in range(5):
        for j in range(5):
            if dist[i][j] == inf: 
                dist[i][j] = 0
    x = json.dumps(dist)
    return x