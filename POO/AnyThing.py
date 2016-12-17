class AnyThing:
    """AnyThing Class for my tests"""

    def echo(message):
        """function that print a simple message"""
        print("{}".format(message))
    echo = staticmethod(echo)

AnyThing.echo("Hello World")

a = AnyThing()

print(a.__dict__)



