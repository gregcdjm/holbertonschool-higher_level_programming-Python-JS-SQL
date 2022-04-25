#include "lists.h"
/**
 *  check_cycle - main function
 *  @list: param 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1 = list;
	listint_t *temp2 = list;

	while (temp1 && temp2 && temp2->next)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;
		if (temp1 == temp2)
		{
			return (1);
		}
	}
	return (0);
}
