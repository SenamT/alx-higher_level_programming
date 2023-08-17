#include "lists.h"

/**
 * get_dnodeint_at_index - this wil return the nth node of a dlistint_t linked list
 * @head: this is the pointer for the start of the list
 * @index: this is the guide of node to look for, beginning from 0
 * Return: nth node or NULL
 **/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int size;
	dlistint_t *tmp;

	size = 0;
	if (head == NULL)
	return (NULL);

	tmp = head;
	while (tmp)
	{
	if (index == size)
	return (tmp);
	size++;
	tmp = tmp->next;
	}
	return (NULL);
}
