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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* ptr = head;//should not use head, or it will lose the beginning
        while(ptr != nullptr && ptr->next != nullptr){
            if(ptr->val == ptr->next->val){
                ptr->next = ptr->next->next;//skip the duplicated one
            }
            else{
                ptr = ptr->next;//go to the next node
            }
        }
        return head;
    }
};