#include<stdio.h>
#include<stdlib.h>

typedef struct tree
{
int data;
struct tree *left;
struct tree *right;
}tree;

tree *create(int val)
{
tree *nn;
nn=(tree *)malloc(sizeof(tree));
nn->data=val;
nn->left=NULL;
nn->right=NULL;
return nn;
}



void inorder(tree *root)
{
if(root)
{
inorder(root->left);
printf("%d->",root->data);
inorder(root->right);
}
}



tree * insert(tree *root, int val)
{
if(!root)
{
root=create(val);
}
else if(root->data>val)
{
root->left=insert(root->left,val);
}
else if(root->data<val)
{
root->right=insert(root->right,val);
}

  return root;

}


//Input=a-b a-c b-d b-c a-f n-a
/*void immediate_child(TNODE tree,TNODE node)
{
printf("%d ",node->left->data);
printf("%d ",node->right->data);
}
*/
 void main()
{
    struct tree *root=NULL;
    root=create(100);
    root=insert(root,11);
    root=insert(root,12);
    root=insert(root,13);
    root=insert(root,14);
    root=insert(root,15);
    root=insert(root,16);
    return 0
}




                             




