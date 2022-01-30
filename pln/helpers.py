import json
import seaborn as sns
import matplotlib.pyplot as plt
from urllib.request import urlopen

def getJsonData(url):
    request = urlopen(url)
    json_parsed = json.loads(request.read())
    items = []
    for i in json_parsed:
        items.append(json_parsed[i])

    return json.dumps(items)

def plotGraph(
    data,
    title = "Graph title",
    xlabel = "x-label", ylabel = "y-label"):
    sns.countplot(data, label="Teste")
    plt.axis("equal")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def anotherFunc():
    return ''