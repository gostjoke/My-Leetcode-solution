// 2026/07/31

func scoreValidator(events []string) []int {
    score := 0
    counter := 0
    for _, i := range events {
        if counter == 10{
            break
        }

        switch i {
        case "WD":
            score +=1
        case "NB":
            score +=1
        case "1":
            score +=1
        case "2":
            score +=2
        case "3":
            score +=3
        case "4":
            score +=4
        case "5":
            score +=5
        case "6":
            score +=6
        case "W":
            counter += 1
        default:
            continue
        }
    }
    return []int{score, counter}
}
