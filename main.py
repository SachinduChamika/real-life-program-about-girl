Girls = []

try:
    NewGirl = str(input("Input Girl's name (If none, press enter): ")).lower()
    if NewGirl != "":
        if NewGirl in Girls:
            while NewGirl in Girls:
                NewGirl = str(input("Girl Entered is already in the List (If none, press enter): ")).lower()
        Girls.append(NewGirl)
    else:
        raise ValueError("No name provided")

except ValueError:
    pass

Friend = str(input("Input your friend's name: ")).lower()

if Friend in Girls:
    print("""1. Act like did nothing when done something wrong.
2. Act like we did everything when done something wrong.
3. Act like they did everything when done something correct.
4. Act like we did nothing when done something wrong.
5. If they ask something, we should tell it for sure.
6. If we ask something, they escape.Disclaimer: The above facts might not be true all the time but in most cases.""")
