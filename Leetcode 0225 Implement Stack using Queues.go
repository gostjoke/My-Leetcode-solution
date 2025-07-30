// 20250729
type MyStack struct {
    q1 []int // main
    q2 []int
}


func Constructor() MyStack {
    return MyStack{}
}


func (this *MyStack) Push(x int)  {
    this.q2 = append(this.q2, x)
    for len(this.q1) > 0 {
        this.q2 = append(this.q2, this.q1[0])
        this.q1 = this.q1[1:]
    }
    this.q1, this.q2 = this.q2, this.q1
}


func (this *MyStack) Pop() int {
    a := this.q1[0]
    this.q1 = this.q1[1:]
    return a
}


func (this *MyStack) Top() int {
    return this.q1[0]
}


func (this *MyStack) Empty() bool {
    return len(this.q1) == 0
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
