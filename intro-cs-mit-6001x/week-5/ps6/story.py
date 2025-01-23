from ps6 import *

def decrypt_story():
    story = CiphertextMessage(text=get_story_string())
    return story.decrypt_message()

print()
print("-------------------------------------------------------")
print("Decrypting story...")
shift, decrypted_story = decrypt_story()

print()
print("The appropriate shift is " + str(shift))

print()
print("The decrypted story is presented below:")

print()
print(decrypted_story)
    
