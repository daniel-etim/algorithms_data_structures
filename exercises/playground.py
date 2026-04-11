score = int(input("Enter your score: "))

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                if score >= 50:
                    print("D")
                else:
                    if score >= 40:
                        print("E")
                    else:
                        if score >= 30:
                            print("F")
                        else:
                            print("YOUre doomed")