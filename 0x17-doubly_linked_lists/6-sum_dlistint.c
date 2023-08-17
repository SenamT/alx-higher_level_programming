#include "lists.h"

/**
 * sum_dlistint - returns the sum of all the data (n),
 * of a doubly linked list
 *
 * @head: this will be the start of the list
 * Return: the sum of all the data or if list is,
 * empty 0
 */
int sum_dlistint(dlistint_t *head)
{
	int sum;

	sum = 0;

	if (head != NULL)
	{
		while (head->prev != NULL)
			head = head->prev;

		while (head != NULL)
		{
			sum += head->n;
			head = head->next;
		}
	}

	return (sum);
}
