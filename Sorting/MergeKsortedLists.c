/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (listsSize == 0) return NULL;

    struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
        struct ListNode dummy;
        struct ListNode* ptr = &dummy;
        dummy.next = NULL;

        while (l1 && l2) {
            if (l1->val < l2->val) {
                ptr->next = l1;
                l1 = l1->next;
            } else {
                ptr->next = l2;
                l2 = l2->next;
            }
            ptr = ptr->next;
        }

        if (l1) ptr->next = l1;
        if (l2) ptr->next = l2;

        return dummy.next;
    }

    while (listsSize > 1) {
        int i = 0;
        int j = 0;

        for (i = 0; i < listsSize; i += 2) {
            struct ListNode* l1 = lists[i];
            struct ListNode* l2 = (i + 1 < listsSize) ? lists[i + 1] : NULL;
            lists[j++] = mergeTwoLists(l1, l2);
        }
        listsSize = j;
    }

    return lists[0];
}