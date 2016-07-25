#include <stdlib.h>
#include <stdio.h> 

typedef struct Node
{
    int data;
    struct Node* next;
}Node;

Node* insert(Node *head,int data)
{
    Node* new_node = malloc(sizeof(Node));

    Node* tail = head;
    while(tail->next != NULL) {
      tail = tail->next;
    }

    tail->next = new_node;
    new_node->data = data;
    new_node->next = NULL;
    return head;
}

void display(Node *head)
{
  Node *start=head;
  while(start)
  {
    printf("%d ",start->data);
    start=start->next;
  }
}

int main()
{
  int T,data;
    scanf("%d",&T);
    Node *head=NULL;  
    while(T-->0){
        scanf("%d",&data);
        head=insert(head,data);
    }
    display(head);
}