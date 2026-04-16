from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def visitors():
    read_file = open("counter.txt", "r")
    visitorsCount = int(read_file.read())
    read_file.close()
    visitorsCount = visitorsCount + 1 

    write_file = open("counter.txt", "w")
    write_file.write(str(visitorsCount))
    write_file.close()

    return render_template("index.html", count = visitorsCount)

@app.route("/", methods = ["POST"])
def weather():
    read_file = open("counter.txt", "r")
    visitorsCount = int(read_file.read())
    read_file.close()

    lat = request.form["latitude"]
    long = request.form["longtitude"]

    api_url = "https://weather-l6tl.onrender.com/api/getCurrentWeather/" + lat + "/" + long

    response = requests.get(api_url)
    weather_data = response.json()
    print(weather_data)
    return render_template("index.html", weather = weather_data, count = visitorsCount)

if __name__ == "__main__":
    app.run(debug = False)
