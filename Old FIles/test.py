Dick = {"hej":5}

def main():
    global Dick
    def deck():
        Dick["hej"] += 5
        print(Dick)
    deck()

main()
