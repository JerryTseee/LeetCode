/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ptr1 = l1;
        ListNode* ptr2 = l2;

        ListNode* head = nullptr;
        ListNode* tail = nullptr;
        int carry = 0;

        while(l1 != nullptr || l2 != nullptr){
            int num1 = l1 ? l1->val : 0;
            int num2 = l2 ? l2->val : 0;
            int sum = num1 + num2 + carry;//remember to add the carry
            
            if(head == nullptr){
                head = tail = new ListNode(sum % 10);
            }
            else{
                tail->next = new ListNode(sum % 10);
                tail = tail->next;
            }
            carry = sum > 9? 1 : 0;

            if(l1 != nullptr){
                l1 = l1->next;
            }
            if(l2 != nullptr){
                l2 = l2->next;
            }
        }
        //at the end check again the carry
        if(carry > 0){
            tail->next = new ListNode(carry);
        }
        return head;
    }
};