from flask import Flask

def create_app(test_config=None):
  # set up app config and create instance of Flask
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

  # create route for hello world equivalent of app.route('/hello, (req, res) => {
  # res.send('Hello, world!;)}) in express
  @app.route('/hello')
  def hello():
    return 'Hello, world!'

  return app