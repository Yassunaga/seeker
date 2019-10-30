from flask import Flask
from flask import request
from datetime import datetime
from graph import Graph
from flask_cors import CORS
from math import inf
import json
import re

app = Flask(__name__)
CORS(app)

@app.route("/graph/")
def grafos():
    return getGraph(False)

@app.route("/graph/clean/")
def grafoLimpo():
    return getGraph(True)

def getGraph(remove_infinite):
    graph = Graph.graph_from_file(Graph, "inputGraph.txt")
    graph = Graph.matrix_to_object(graph,remove_infinite)
    nodes = Graph.nodes_from_file(Graph, "inputGraph.txt")
    response = {
        "graph": graph,
        "nodes" : nodes
    }
    return response
