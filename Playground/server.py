from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def play():
    return render_template('play.html')

@app.route('/play/<number_of_boxes>')          # The "@" decorator associates this route with the function immediately following
def play_number(number_of_boxes):
    repeat = int(number_of_boxes)
    return render_template('play_number.html', repeat = repeat)

@app.route('/play/<number_of_boxes>/<color>')          # The "@" decorator associates this route with the function immediately following
def play_number_color(number_of_boxes,color):
    repeat = int(number_of_boxes)
    color = color
    return render_template('play_number_color.html', repeat = repeat, color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

