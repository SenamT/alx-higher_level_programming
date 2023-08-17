#include "lists.h"

/**
 * free_dlistint - this will free a dlistint_t list
 * @head: this is the pointer forstart of list
 * Return: NULL
 **/
void free_dlistint(dlistint_t *head)
{
	if (head == NULL)
	return;

	while (head->next)
	{
	head = head->next;
	free(head->prev);
	}
	free(head);
}
