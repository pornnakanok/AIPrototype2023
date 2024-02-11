import os
from flask import Flask, request, render_template

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        # Get the uploaded files
        file = request.files['file']
        text = request.form['text']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # Save the uploaded files
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        # Render a template with upload confirmation
        return render_template("home2.html", text=text, filename=file.filename)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <label for="text">Enter Text:</label><br>
      <input type="text" name="text" id="text"><br><br>
      <label for="file">Upload File:</label><br>
      <input type=file name=file id="file"><br><br>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
