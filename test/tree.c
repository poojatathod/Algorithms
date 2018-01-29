#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

typedef struct node
{
    char data;
    struct node *left;
    struct node *right;
}NODE;

typedef struct node *TNODE;

TNODE create_tree_node(char ch)
{
TNODE newn;
newn=(TNODE)malloc(sizeof(NODE));
newn->data=ch;
newn->left=NULL;
newn->right=NULL;
return newn;
}

TNODE insertnodeatleft(TNODE tree,char ch)
{   if (tree==NULL)
    {
        return create_tree_node(ch);
    }
    else
    {
    TNODE newn=create_tree_node(ch);
    tree->left=newn;
    return tree;
    }
}



TNODE insertnodeatright(TNODE tree,char ch)
{   
    
    if (tree==NULL)
    {
        return create_tree_node(ch);
    }
    else
    {
    TNODE newn=create_tree_node(ch);
    tree->right=newn;
    return tree;
    }
}

void display(TNODE *tree)
 {
    if(tree)
        {
        printf("%ch->",tree->data);
        display(tree->left);
        display(tree->right);
                            
        }
}



//Input=a-b a-c b-d b-c a-f n-a
void immediate_child(TNODE tree,TNODE node)
{
    printf("%c ",node->left->data);
    printf("%c ",node->right->data);
}

//void all_child(tree,node)
//{

//}

void main()
{
TNODE tree=NULL;
tree=create_tree_node('n');
display(tree);
printf("\n");
tree=insertnodeatleft(tree,'a');
tree=insertnodeatleft(tree,'b');
display(tree);
printf("\n");
tree=insertnodeatright(tree,'c');
}
