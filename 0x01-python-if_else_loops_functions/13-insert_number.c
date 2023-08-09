#include "lists.h"

/**
 * insert_node - This will put a number into a singly-linked list which is sorted
 * @head: Points to the head of the list which is linked
 * @number: Number which needs to be put in
 *
 * Return: If function is unsuccessful - NULL.
 * Otherwise - a pointe for new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
