#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - function that check if the list is a palindrome
 * @head: the list to check
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, k;
	listint_t *tmp = *head, *tmp2 = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (tmp->next->next)
	{
		tmp = tmp->next;
		i++;
	}
	k = i / 2;
	if (i % 2 != 0)
		j--;
	for (; j < k + 1; j++)
	{
		tmp = *head;
		for (i = k * 2; i - j != 0; i--)
		{
			tmp = tmp->next;
		}
		if (tmp->next->n != tmp2->n )
		{
			return (0);
			}
		tmp2 = tmp2->next;
	}
	return (1);
}
