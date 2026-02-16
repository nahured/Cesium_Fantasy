from pubsub import pub

def get_image(img,**extra):
    print(img)



pub.subscribe(get_image,"generate_image")

