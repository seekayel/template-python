#from hello_world.app import say_hello

from hello_world import app

def test_hello_world():
    assert app.say_hello() == "Hello World"
