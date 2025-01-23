from ps6 import *

x = Message('Hello world')

x.apply_shift(3)

def test_apply_shift():
    """
    Unit test for the method apply shift
    """
    failure=False
    testcases = {
        ("hello world", 3) : "khoor zruog",
        ("Hello, world", 5) : "Mjqqt, btwqi",
        ("", 3) : "",
        ("Abcwxyz", 25) : "Zabvwxy",
        ("This is a Test!", 10) : "Drsc sc k Docd!",
        ("Massachusette", 0) : "Massachusette"
    }
    for testcase in testcases.keys():
        x = Message(testcase[0])
        x.apply_shift(testcase[1])
        if x.message_text != testcases[testcase]:
            print("FAILURE: test_apply_shift()")
            print("\tExpected", testcases[testcase], " but got '" + x.message_text + "' for word '" + testcase[0] + "', shift=" + str(testcase[1]))
            failure=True
    
    if not failure:
        print("SUCCESS: test_apply_shift()")

print("----------------------------------------------------------------------")
print("Testing apply_shift()...")
test_apply_shift()

