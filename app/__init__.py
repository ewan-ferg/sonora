import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
        )
    os.makedirs(app.instance_path, exist_ok=True)
    
    @app.route('/')
    def home_page():
        return render_template('index.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)