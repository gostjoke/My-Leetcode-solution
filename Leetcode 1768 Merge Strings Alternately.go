// 2026/03/12
import "strings"
func mergeAlternately(w1 string, w2 string) string {
    // ans := ""
    var builder strings.Builder
    i := 0

    for (i < len(w1) || i < len(w2)) {
        if i < len(w1) {
            // ans += string(w1[i])
            builder.WriteByte(w1[i])
        }
        if i < len(w2) {
            // ans += string(w2[i])
            builder.WriteByte(w2[i])
        }

        i ++
    }

    // return ans
    return builder.String()
}
