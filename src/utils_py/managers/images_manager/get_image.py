from pubsub import pub

def get_image(img,**extra):
    print(img)


print("subscrito")
pub.subscribe(get_image,"generate_image")
#def subscriber():