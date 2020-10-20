

// Complete the insertNodeAtTail function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
SinglyLinkedListNode* insertNodeAtTail(SinglyLinkedListNode* head, int data) {

	SinglyLinkedListNode* newNode=new SinglyLinkedListNode(data);
    if(head==NULL){
        return newNode;
    }
    SinglyLinkedListNode* temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    

    temp->next=newNode;

    return head;
}

