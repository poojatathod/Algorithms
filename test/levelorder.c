#include<stdio.h>
#include<stdlib.h>

typedef struct Tnode
{
    int data;
    struct Tnode *left;
    struct Tnode *right;
}tree;


typedef struct node
{
    int data;
    int level;
    struct node *next;
}list;




list * createlistnode(int data,int level)
{
    list *nn;
    nn=(list *)malloc(sizeof(list));
    nn->next=NULL;
    nn->data=data;
    nn->level=level;
    return nn;
}




list * insertfront(list *head,int data,int level)
{
  list *temp;
  temp=head;
  head=createlistnode(data,level);
  head->next=temp;
  return head;
}


void displayList(list *head)
{
    if(head)
    {
        fprintf(stdout,"[data=%d level=%d] -> ",head->data,head->level);
        displayList(head->next);
    }
}

int max ( int a , int b)
{
    if(a>b)
        return a;
    else 
        return b;
}


int heightOfTree(tree *root,int h)
{
    if(root)
    {
      return ( max ( heightOfTree(root->left,h+1) ,heightOfTree(root->right,h+1)) );
    }
    else
        return h;
}


void displayTreeListLevelWise(list *treeList,int level)
{
   if(treeList)
   {
       if(treeList->level==level)
       {
           fprintf(stdout,"[%d] ->",treeList->data);
       }
       displayTreeListLevelWise(treeList->next,level);
   }
}


list *treetolist(tree *root,list *treeList,int l)
{
    if(root)
    {
     treeList=insertfront(treeList,root->data,l);
     treeList=treetolist(root->left,treeList,l+1);
     treeList=treetolist(root->right,treeList,l+1);
     return treeList;
    }
    else
        return treeList;

}




tree *createTNode(int ino)
{
    tree *newn=NULL;
    newn=(tree *)malloc(sizeof(tree));
    newn->data=ino;
    newn->left=NULL;
    newn->right=NULL;
    return newn;
}


tree * insertToBST(tree *root,int data)
{   
    if(!root)
    {
        return createTNode(data);
    }
    else if(data<root->data)
    {
        root->left=insertToBST(root->left,data);
    }
    else if(data>root->data)
    {
        root->right=insertToBST(root->right,data);
    }
    return root;
}




void displayT(tree *root)
{
    if(root)
    {
        printf("%d ",root->data);
        displayT(root->left);
        displayT(root->right);
    }

}



void main()
{
    
    struct Tnode *root=NULL;
    list *treeList=NULL;
    int i;

    root=insertToBST(root,8);
    root=insertToBST(root,10);
    root=insertToBST(root,6);
    root=insertToBST(root,1);
    root=insertToBST(root,12);
    root=insertToBST(root,9);
    displayT(root);
    fprintf(stdout,"\nHeight= %d \n",heightOfTree(root,0));

    treeList = treetolist(root,treeList,1);

    for(i=1;i<=heightOfTree(root,0);i++)
        displayTreeListLevelWise(treeList,i);

}
