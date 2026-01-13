/**
 * 2026/01/13
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */
func dfs(root *Node){
    if root == nil || root.Left == nil{
        return 
    }
    root.Left.Next = root.Right 
    if root.Next != nil{
        root.Right.Next = root.Next.Left
    }
    dfs(root.Left)
    dfs(root.Right)
}

func connect(root *Node) *Node {
    dfs(root)
    return root
}
