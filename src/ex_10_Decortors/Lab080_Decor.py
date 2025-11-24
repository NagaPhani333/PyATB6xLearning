def before_after_ui_test(func):
    def test():
        print("Before Running UI Code")
        func()
        print("After Running UI Code")
    return test()


@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI Test")