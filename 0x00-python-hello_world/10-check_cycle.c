#include "lists.h"

/**
 * check_cycle - assesses if a linked list has a cycle
 * @list: this will be the linked list which needs to be check
 *
 * Return: 1 only if list has cycle, 0 if it does not have cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
