
from flask import Flask, render_template, request, jsonify
import pickle
app = Flask(__name__)



@app.route('/')
def frame_1():
    return render_template('frame-1.html')

@app.route("/frame-2", methods=['GET'])
def frame_2():
    return render_template('frame-2.html')

# Move the '/submit' route definition to the top level
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    disease_name = request.form.get('diseaseName')
    disease_description = request.form.get('diseaseDescription')

    # Handle file upload
    if 'photo' in request.files:
        photo = request.files['photo']
        # Save the uploaded photo to a directory, e.g., 'uploads/'
        # You can use Flask's built-in functions to securely save and manage uploaded files
        photo.save('uploads/' + photo.filename)

        # Perform any required processing, e.g., machine learning prediction
        # Replace the following lines with your actual prediction logic
        prediction_result = "Healthy"  # Replace with your prediction result
    else:
        prediction_result = "No photo provided"

    # Return the prediction result as JSON
    return jsonify({'result': prediction_result})

# Rest of your route definitions

@app.route("/frame-3")
def frame_3():
  return render_template('frame-3.html')

@app.route("/frame-4")
def frame_4():
  return render_template('frame-4.html')

@app.route("/frame-5")
def frame_5():
  return render_template('frame-5.html')
@app.route("/frame-6")
def frame_6():
  return render_template('frame-6.html')
@app.route("/frame-7")
def frame_7():
  return render_template('frame-7.html')

if __name__ == '__main__':
    app.run(debug=True)
