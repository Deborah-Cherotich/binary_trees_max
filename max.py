class Node:
    def __init__(self, key):
        self.left = None    
        self.right = None   
        self.val = key      

def access_item(root, key):
    if root is None or root.val == key:   
        return root
    if root.val < key:                    
        return access_item(root.right, key)
    return access_item(root.left, key)    

root = Node(20)                 
root.left = Node(10)             
root.right = Node(30)            
root.left.left = Node(5)        
root.right.left = Node(15)       
root.right.right = Node(35)      

key = 35                       
result_node = access_item(root, key)  

if result_node is not None:
    print(f"Found node with value {key}")   
else:
    print(f"Node with value {key} not found")    
