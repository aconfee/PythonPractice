Node findInOrderSuccessor(Node x) {
    if(x == null) 
    return null;
    
    if(x.right != null)
    {
    x = x.right;
    while(x.left != null)
        x = x.left;
    
    return x;
    }      
    // I'm left child
    while(x.parent != null && x.key > x.parent.key)
    x = x.parent;
    
    return x.parent;      
}