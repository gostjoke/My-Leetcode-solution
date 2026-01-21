// 2026/01/20 stack
func simplifyPath(path string) string {
    var st []string
    c := strings.Split(path, "/")
    // fmt.Printf("%v\n",c)
    for _, i := range c{
        // fmt.Printf("%v\n",i)
        if i == "" || i =="." {
            continue
        }
        if i == ".." {
            if len(st) != 0 {
                st = st[:len(st)-1]
            }
        } else {
            st = append(st, i)
        }
    }
    return "/" + strings.Join(st, "/")
}
