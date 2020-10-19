/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */


int ht(node* root){
    if(root){
        return 1+max(ht(root->left), ht(root->right));
    }
    return -1;
}

void updateHt(node* root){
    if(root){
        root->ht = 1 + max(ht(root->left), ht(root->right)); 
    }
}

node* rotateL(node* root){
    node* temp = root->right;
    node* t = temp->left;
    
    root->right = t;
    temp->left = root;
    
    updateHt(temp);
    updateHt(root);
    
    return temp;
}

node* rotateR(node* root){
    node* temp = root->left;
    
    root->left = temp->right;
    temp->right = root;
    
    updateHt(temp);
    updateHt(root);
    
    return temp;
}

node * insert(node * root,int val)
{
    // print(root);
    // cout << endl << endl;
   if(!root){
       root = new node;
       root->val = val;
       root->ht = 0;
       root->left = root->right = nullptr;
       return root;
   }
    if(root->val < val){
        root->right = insert(root->right, val);
    }
    else if(root->val > val){
        root->left = insert(root->left, val);
    }
    
    updateHt(root);
    
    int bal = ht(root->left) - ht(root->right);
    
    
    //RR
    if(bal <= -2 and val > root->right->val){
        root = rotateL(root);
    }
    
    //LL
    if(bal >= 2 and val < root->left->val){
        root = rotateR(root);
    }
    
    //RL
    if(bal <= -2 and val < root->right->val){
        root->right = rotateR(root->right);
        root = rotateL(root);
    }
    
    //LR
    if(bal >= 2 and val > root->left->val){
        root->left = rotateL(root->left);
        root = rotateR(root);
    }
  
    return root;
}
