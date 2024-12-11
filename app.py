from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with a question and buttons
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Are You Gay?</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-image: url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmp5Mm1pbmY5OGppanJxbzJ5ZXU0aGViZ3pybWhheGMzczZhOWt6MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10YWqUivkQPeeJWD3u/giphy.gif'); /* Updated GIF URL */
            background-size: cover;
            background-position: center;
            position: relative;
            overflow: hidden;
        }
        #question {
            color: white; /* Change text color */
            font-size: 3em; /* Increase font size */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* Add text shadow for better visibility */
            margin-bottom: 30px; /* Add some space below the question */
        }
        button {
            font-size: 1.5em; /* Increase button font size */
            padding: 15px 30px; /* Increase button padding for larger buttons */
            margin: 10px; /* Add margin around buttons */
            cursor: pointer; /* Change cursor to pointer on hover */
            border: none; /* Remove default border */
            border-radius: 5px; /* Add rounded corners */
            background-color: #007BFF; /* Button background color */
            color: white; /* Button text color */
            transition: background-color 0.3s; /* Smooth transition for hover effect */
        }
        button:hover {
            background-color: #0056b3; /* Darker shade on hover */
        }
        #no-button {
            position: absolute;
        }
    </style>
</head>
<body>
    <div>
        <h1 id="question">Are you gay?</h1>
        <button onclick="window.location.href='/support'">Yes</button>
        <button id="no-button" onclick="moveButton()">No</button>
    </div>

    <script>
        function moveButton() {
            const button = document.getElementById('no-button');
            const x = Math.random() * (window.innerWidth - 100);
            const y = Math.random() * (window.innerHeight - 50);
            button.style.left = x + 'px';
            button.style.top = y + 'px';
        }
    </script>
</body>
</html>
"""

# HTML template for the support page
SUPPORT_HTML = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>caught you!</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            position: relative; /* Allow positioning of the secret button */
        }
        h1 {
            color: #333;
            font-size: 3em; /* Increase font size for support message */
        }
        #secret-button {
            position: absolute; /* Position it absolutely */
            bottom: 20px; /* Position it near the bottom */
            right: 20px; /* Position it near the right */
            font-size: 0.7em; /* Small font size */
            padding: 5px 10px; /* Small padding */
            background-color: #28a745; /* Green background */
            color: white; /* White text */
            border: none; /* No border */
            border-radius: 5px; /* Rounded corners */
            cursor: pointer; /* Pointer cursor */
            display: block; /* Make it visible */
        }
        #secret-button:hover {
            background-color: #218838; /* Darker green on hover */
        }
    </style>
</head>
<body>
    <h1>dw haruki will support you!</h1>
    <button id="secret-button" onclick="window.location.href='/hehe'">Click Here</button>
</body>
</html>
"""

# HTML template for the Hehe page with moon GIF background and three paragraphs of text
HEHE_HTML = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>hehe</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-image: url('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHAwcTFzbTR0MDAzcG9jZHM1M2U5emEwcWZhczhzeDJzeGg2ZjU1OSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/FWtVYDHIxgGgE/giphy.gif'); /* Moon GIF URL */
            background-size: cover;
            background-position: center;
            color: white; /* Text color */
            text-align: center; /* Center text */
            padding: 20px; /* Add padding */
        }
        h1 {
            font-size: 2em; /* Increase font size for the message */
            margin-bottom: 20px; /* Space below the heading */
        }
        p {
            font-size: 1.2em; /* Font size for paragraphs */
            margin: 10px 0; /* Space between paragraphs */
        }
    </style>
</head>
<body>
    <h1>The Moon Will Stay Beautiful Forever, Isn't It?</h1>
    <p>You make me smile, you make me laugh,
You turn my day from dull to light.
With every word, you bring me peace,
You’re like my moon, far but bright.</p>
    <p>You’re my safe place, my closest but farthest friend,
The one I trust, the one I need.
But there’s a feeling in my heart,
A tiny hope, a little seed.</p>
    <p>I like you more than words can say,
But I’m too scared to let it show.
For now, I’ll stay here by your side,
And hope one day, you’ll come to know..</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/support')
def support():
    return render_template_string(SUPPORT_HTML)

@app.route('/hehe')
def hehe():
    return render_template_string(HEHE_HTML)

if __name__ == '__main__':
    app.run(debug=True)
