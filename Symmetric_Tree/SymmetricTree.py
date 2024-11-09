/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {

private:
    bool compare(TreeNode* left, TreeNode* right){
        if(left == nullptr && right == nullptr){
            return true;//base case
        }
        else if(left == nullptr || right == nullptr ||left->val != right->val){
            return false;
        }
        else{
            return compare(left->left, right->right)&&compare(left->right, right->left);
        }
    }

public:
    bool isSymmetric(TreeNode* root) {
        if(root == nullptr){
            return true;
        }
        else{
            return compare(root->left, root->right);
        }
    }
};